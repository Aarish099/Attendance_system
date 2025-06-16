import face_recognition
import face_recognition_models
import os
import pickle

dataset_dir = "dataset" 
encoding_file = "encodings.pickle"

known_encodings = []
known_names = []

for person_name in os.listdir(dataset_dir):
    person_dir = os.path.join(dataset_dir, person_name)
    for img_name in os.listdir(person_dir):
        img_path = os.path.join(person_dir, img_name)
        image = face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(person_name)

data = {"encodings": known_encodings, "names": known_names}

with open(encoding_file, "wb") as f:
    f.write(pickle.dumps(data))


print("✅ Encodings saved to encodings.pickle")

 









