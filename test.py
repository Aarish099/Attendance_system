import face_recognition
image = face_recognition.load_image_file("test.jpg")
encoding = face_recognition.face_encodings(image)[0]
print(encoding)
print(len(encoding))