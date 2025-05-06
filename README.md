# 🛒 Retail Product Checkout System
A computer vision-based automated checkout system designed to detect and identify retail products in real-time using the YOLOv8 object detection model. This project simplifies the in-store checkout process by minimizing manual scanning and enabling faster, smarter retail experiences.

---
## 🔍 Overview

The system captures product images via uploaded input, detects the items using YOLOv5/YOLOv8, and automatically generates a product list along with corresponding prices. It mimics the behavior of a smart checkout counter, ideal for convenience stores or unmanned retail kiosks.

---
## 🎯 Features

- ✅ Real-time object detection using YOLOv8
- ✅ Automatic product name and price mapping
- ✅ Streamlined UI for image upload
- ✅ Real-time display of total cost

---
## 🧠 Tech Stack

- **YOLOv8** - PyTorch-based object detection model
- **OpenCV** - Real-time image processing
- **Python** - Core logic
- **Streamlit** or Flask - For web interface
- **LabelImg / Roboflow** - For dataset labeling and preprocessing (if custom dataset used)

---

## 🏗️ Architecture

1. **Image Input** - Live webcam feed or uploaded image
2. **Preprocessing** - Resize, normalize, format image
3. **Detection** - YOLOv8 model identifies product classes and bounding boxes
4. **Mapping** - Each detected class is mapped to a product name and price
5. **Checkout Summary** - List of detected items and total cost is displayed
