import cv2
import os

def extract_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open the video file.")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:  # If no more frames, break
            break

        # Create a filename for the frame
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpeg")

        # Save the frame as a BMP image
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    print(f"Extraction complete. Frames are saved in '{output_folder}'.")

# Usage
video_path = r"C:\Users\malik\Downloads\Indian rhino's night behaviour - Deba Kumar Dutta (240p, h264).mp4"
output_folder = "./Output"  # Replace with the full path to your desired output folder
extract_frames(video_path, output_folder)
