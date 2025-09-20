import face_recognition
import cv2
import os
import numpy as np

class SimpleFaceRec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for faster processing (optional, but good practice)
        self.frame_resizing_factor = 0.25 # Process 1/4th size images

    def load_encoding_images(self, image_path):
        """
        Loads example images and generates face encodings for them.
        The name of the person is taken from the image filename.
        """
        # Load images from specified path
        for filename in os.listdir(image_path):
            if filename.endswith((".jpg", ".png", ".jpeg", ".webp")):
                path = os.path.join(image_path, filename)
                img = cv2.imread(path)

                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # Get the name from the filename
                basename = os.path.basename(path)
                (name, ext) = os.path.splitext(basename)

                # Get face encoding for the image
                img_encodings = face_recognition.face_encodings(rgb_img)
                if img_encodings: # Ensure a face was found
                    self.known_face_encodings.append(img_encodings[0])
                    self.known_face_names.append(name)
                else:
                    print(f"No face found in {filename}. Skipping.")

        print(f"Found {len(self.known_face_names)} encoding images.")

    def detect_known_faces(self, frame):
        """
        Detects faces in the current frame and compares them to known faces.
        Returns face locations and corresponding names.
        """
        # Resize frame for faster face detection
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing_factor, fy=self.frame_resizing_factor)
        # Convert BGR to RGB
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find all the faces and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Compare current face with known faces
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the closest match if a match is found
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            face_names.append(name)

        scaled_face_locations = []
        for top, right, bottom, left in face_locations:
            top = int(top / self.frame_resizing_factor)
            right = int(right / self.frame_resizing_factor)
            bottom = int(bottom / self.frame_resizing_factor)
            left = int(left / self.frame_resizing_factor)
            scaled_face_locations.append((top, right, bottom, left))

        return scaled_face_locations, face_names