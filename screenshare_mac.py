import cv2
import time
from PIL import Image
import numpy as np
import os
import pyautogui
import tkinter as tk
from tkinter import ttk
import mss
import pygetwindow as gw


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
        if os.name == 'posix':  # Check if the OS is macOS
            screen = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}  # Update with your screen dimensions
        else:
            screen = gw.getWindowsWithTitle(app.selected_screen)[0]

        # Initialize the screen capture
        with mss.mss() as sct:
            while True:
                # Capture the selected screen
                screenshot = sct.shot(output=f"{folder}/frame.jpg")

                # Read the saved screenshot
                pil_img = Image.open(screenshot)

                # Convert the PIL image back to an OpenCV image
                frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

                # Display and save the frame as an image file
                cv2.imshow("Screen Sharing Preview", frame)
                print("Saved current frame")
                path = f"{folder}/frame.jpg"
                cv2.imwrite(path, frame)

                # Check if the user pressed the 'q' key
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            # Close all windows
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()