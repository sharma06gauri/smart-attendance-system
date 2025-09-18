import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import csv
import tkinter as tk
from tkinter import messagebox

# GUI for notifications
root = tk.Tk()
root.withdraw()

# The PDF report indicates that the project uses OpenCV and face_recognition.
# This code is a reconstruction of a typical face recognition attendance system based on the report's description.

def show_message(title, message):
    """
    Displays a message box to the user.
    """
    messagebox.showinfo(title, message)

def load_images_from_folder(folder):
    """
    Loads images from a folder and encodes them for face recognition.
    """
    print("Loading known faces...")
    images = []
    class_names = []
    my_list = os.listdir(folder)
    for cl in my_list:
        cur_img = cv2.imread(f'{folder}/{cl}')
        if cur_img is not None:
            images.append(cur_img)
            class_names.append(os.path.splitext(cl)[0])
    return images, class_names

def find_encodings(images):
    """
    Generates face encodings for a list of images.
    """
    encode_list = []
    print("Encoding loaded faces...")
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Handle cases where no face is detected in the image
        try:
            encode = face_recognition.face_encodings(img)[0]
            encode_list.append(encode)
        except IndexError:
            print(f"No face found in one of the images.")
            continue
    return encode_list

def mark_attendance(name):
    """
    Marks attendance in a CSV file.
    """
    with open('Attendance.csv', 'r+') as f:
        my_data_list = f.readlines()
        name_list = []
        for line in my_data_list:
            entry = line.split(',')
            name_list.append(entry[0])
        if name not in name_list:
            now = datetime.now()
            dt_string = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dt_string}')
            show_message("Attendance Marked", f"Attendance marked for {name}.")

def main():
    """
    Main function to run the attendance system.
    """
    path = 'ImagesAttendance' # This folder should contain your student images
    if not os.path.exists(path):
        os.makedirs(path)
        show_message("Error", f"Folder '{path}' not found. Please create it and add images of students.")
        return

    images, class_names = load_images_from_folder(path)
    if not images:
        show_message("Error", f"No images found in '{path}' folder. Please add student images to proceed.")
        return

    encode_list_known = find_encodings(images)
    if not encode_list_known:
        show_message("Error", "Could not encode any faces. Please ensure your images contain clear faces.")
        return

    print("Encoding Complete. Starting real-time detection...")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        show_message("Error", "Could not open webcam. Please check if a camera is connected and drivers are installed.")
        return

    # Create or clear the Attendance.csv file
    with open('Attendance.csv', 'w') as f:
        f.write('Name,Time')

    while True:
        try:
            success, img = cap.read()
            if not success:
                print("Failed to grab a frame from the camera.")
                break

            img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)

            faces_in_frame = face_recognition.face_locations(img_small)
            encodes_in_frame = face_recognition.face_encodings(img_small, faces_in_frame)

            for encode_face, face_loc in zip(encodes_in_frame, faces_in_frame):
                matches = face_recognition.compare_faces(encode_list_known, encode_face)
                face_distance = face_recognition.face_distance(encode_list_known, encode_face)
                match_index = np.argmin(face_distance)

                if matches[match_index]:
                    name = class_names[match_index].upper()
                    y1, x2, y2, x1 = face_loc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    mark_attendance(name)

            cv2.imshow('Face Recognition Attendance System', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
