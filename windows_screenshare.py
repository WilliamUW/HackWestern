import cv2
import time
from PIL import Image
import numpy as np
import os
import pygetwindow as gw
import tkinter as tk
from tkinter import ttk
import pyautogui

# Folder
folder = "frames"

# Create the frames folder if it doesn't exist
frames_dir = os.path.join(os.getcwd(), folder)
os.makedirs(frames_dir, exist_ok=True)

class ScreenCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Capture App")

        self.selected_screen = None

        # Get available screens
        self.screens = gw.getAllTitles()

        # Screen selection label
        screen_label = tk.Label(root, text="Select Screen:")
        screen_label.grid(row=0, column=0, padx=10, pady=10)

        # Screen selection dropdown
        self.screen_var = tk.StringVar(root)
        self.screen_var.set(self.screens[0])  # Default to the first screen
        screen_dropdown = ttk.Combobox(root, textvariable=self.screen_var, values=self.screens)
        screen_dropdown.grid(row=0, column=1, padx=10, pady=10)

        # Start button
        start_button = tk.Button(root, text="Start Capture", command=self.start_capture)
        start_button.grid(row=1, column=0, columnspan=2, pady=10)

    def start_capture(self):
        self.selected_screen = self.screen_var.get()
        self.root.destroy()  # Close the UI window

def main():
    root = tk.Tk()
    app = ScreenCaptureApp(root)
    root.mainloop()

    if app.selected_screen:
        # Get the selected screen dimensions
        screen = gw.getWindowsWithTitle(app.selected_screen)[0]
        screen_width, screen_height = screen.size

        # Initialize the video capture
        cap = cv2.VideoCapture(0)  # Use 0 for the default camera

        # Wait for the camera to initialize and adjust light levels
        time.sleep(2)

        while True:
            # Capture the selected screen
            screenshot = pyautogui.screenshot(region=(screen.left, screen.top, screen_width, screen_height))
            frame = np.array(screenshot)

            # Convert the frame to a PIL image
            pil_img = Image.fromarray(frame)

            # Convert the PIL image back to an OpenCV image
            frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

            # Display the frame with custom dimensions
            frame = cv2.resize(frame, (400, 300))  # Resize the frame to 400x300

            # Display the frame
            cv2.imshow("Screen Sharing Preview", frame)

            # Save the frame as an image file
            print("Saved current frame")
            path = f"{folder}/frame.jpg"
            cv2.imwrite(path, frame)

            # Check if the user pressed the 'q' key
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the camera and close all windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
