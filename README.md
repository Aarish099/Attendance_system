🎥 Face Recognition Attendance System
This project is a real-time face recognition-based attendance system that uses your webcam to detect and recognize faces, and automatically marks attendance in a CSV file. It leverages deep learning-based facial recognition for accurate and efficient identification.

🧠 How It Works
Face Encoding Generator:
A script scans through a given dataset of labeled images (sorted by folders named after each person), extracts facial features (encodings), and saves them in a pickle file for later use.

Real-Time Face Recognition:
Another script opens the webcam, detects faces frame by frame, matches them against the known encodings, and marks the user as present by recording their name with a timestamp in a .csv file. A name is marked only once per session.

Visualization:
The system draws bounding boxes around detected faces and displays their names directly on the video feed in real-time.

📂 Project Structure
dataset/ — Folder containing subfolders of known individuals' images

encodings.pickle — Serialized face encodings and corresponding names

attendance2.csv — File where attendance is logged

Main script — Handles webcam input, face recognition, and attendance logging

🔧 Technologies Used
face-recognition — Core library for face detection and encoding

dlib — Underlying face recognition engine

OpenCV — Used for capturing video, drawing boxes, and displaying output

NumPy — Array manipulation and distance calculations

pickle — Serializing and deserializing encodings

datetime — For timestamping attendance logs

✅ Features
Real-time face detection and recognition

Automatic attendance logging

Session-aware logging to avoid duplicate entries

Easy to extend with more individuals by adding images to the dataset

🚀 Use Cases
Classroom or lab attendance

Office employee check-in systems

Secure access logs for events or clubs

This project is a solid starting point for anyone exploring facial recognition or automating identity-based tasks with computer vision.
