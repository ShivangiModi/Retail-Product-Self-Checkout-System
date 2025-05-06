from flask import Flask, render_template, request, redirect, url_for
import os
import mysql.connector
from ultralytics import YOLO
from PIL import Image
import io
import base64

app = Flask(__name__)

# Load model
model = YOLO("best.pt")  # Ensure this model file is in the container

# Configure MySQL connection
db_config = {
    "host": "34.70.220.45",  # Or use the internal IP / connection name if in GCP
    "user": "root",
    "password": "root",
    "database": "retail_products"
}

# Product prices for mock billing
product_prices = {
    "lays": 1.50,
    "oreo": 2.00,
    "sprite": 1.75,
    "cocacola": 1.75,
    "detergent": 4.25
}

def connect_to_database():
    return mysql.connector.connect(**db_config)

def save_to_db(product_name, price):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO billing (product, price) VALUES (%s, %s)"
    cursor.execute(query, (product_name, price))
    connection.commit()
    cursor.close()
    connection.close()

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            image = Image.open(image_file.stream)
            results = model(image)

            product_set = set()
            for result in results:
                for box in result.boxes:
                    cls = int(box.cls[0])
                    label = model.names[cls]
                    product_set.add(label)

            bill = []
            total = 0.0
            for product in product_set:
                price = product_prices.get(product.lower(), 0)
                bill.append({'product': product, 'price': price})
                save_to_db(product, price)
                total += price

            # Convert image to base64 for display
            img_io = io.BytesIO()
            image.save(img_io, 'JPEG')
            img_io.seek(0)
            img_base64 = base64.b64encode(img_io.getvalue()).decode()

            return render_template('payment.html', bill=bill, total=total, image=img_base64)

    return render_template('upload.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Required for Cloud Run
    app.run(host='0.0.0.0', port=port, debug=False)
