# Smart Attendance System using Face Recognition

## 📌 Overview

The **Smart Attendance System** leverages **facial recognition technology** to automate the process of marking attendance. Traditional methods like roll calls and sign-in sheets are slow, error-prone, and vulnerable to manipulation. Our system uses **Python, OpenCV, and machine learning algorithms** to detect and recognize faces in real-time, record attendance, and generate reports automatically.

This project provides an efficient, secure, and user-friendly solution suitable for **educational institutions, organizations, and enterprises**.

---

## 🚀 Features

* Real-time face detection and recognition
* Automatic attendance marking with **CSV export**
* User-friendly **Flask web interface**
* Dataset creation & training functionality
* High accuracy with KNN (K-Nearest Neighbors) classifier
* Robust performance across varying lighting and facial orientations

---

## 🛠️ Tech Stack

**Languages & Frameworks**

* Python
* Flask (for web interface)

**Libraries & Tools**

* OpenCV (face detection & image processing)
* NumPy & Pandas (data handling)
* scikit-learn (KNN model for recognition)
* Joblib (model persistence)
* HTML, CSS, JavaScript (frontend)

**Database & Storage**

* Attendance stored in **CSV files**
* Face dataset stored in **local directories**

---

## 💻 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Smart-Attendance-System.git
cd Smart-Attendance-System
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Access the System

Open your browser and go to:

```
http://127.0.0.1:5000/
```

## 📷 Usage

* **Add New User** → Enter name & ID → Capture dataset using webcam
* **Train Model** → System trains KNN model on stored faces
* **Start Attendance** → Recognizes faces in real-time → Marks attendance in `Attendance/` folder

Attendance is saved in CSV format:

```
Attendance-<date>.csv
```

## 📊 System Requirements

### Hardware

* Processor: Intel i5 or higher
* RAM: 8 GB+
* Webcam: 720p or higher

### Software

* OS: Windows 10 / Linux / macOS
* Python 3.7+
* Libraries: OpenCV, scikit-learn, Pandas, Flask

## 📌 Results

* ✅ Faster & more accurate attendance marking
* ✅ Reduced errors compared to manual methods
* ✅ Increased security with biometric authentication

## 📝 Future Enhancements

* Cloud database integration
* Mobile app support
* Advanced deep learning models (CNN, FaceNet)
* Multi-camera support

## 👨‍💻 Contributors

  Pavithra G 
  Noor Hafsa
  Spoorthi S V 
  Gauri Sharma 

Guided by **Prof. Swathy J, Dept. of CSE, CITech**

## 📚 References

* [OpenCV Documentation](https://docs.opencv.org/)
* [scikit-learn](https://scikit-learn.org/stable/)
* [Flask](https://flask.palletsprojects.com/)

🔥 With this project, attendance tracking becomes **automated, reliable, and secure**.
