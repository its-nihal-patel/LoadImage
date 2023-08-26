# Image Viewer with PySimpleGUI

This is a Python script that demonstrates an image viewer application using the PySimpleGUI library. The application allows users to load an image, view it in a graphical interface, and draw rectangles on the image using mouse input.

## Features

- Load an image from the file system.
- Display the loaded image in a graphical window.
- Draw rectangles on the image using mouse input.
- Display information about the drawn rectangles.

## Prerequisites

- Python 3.x
- PySimpleGUI
- Pillow (PIL Fork)

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries using the following command:
   
   ```
   pip install PySimpleGUI Pillow
   ```

## Usage

1. Run the script using the command:
   
   ```
   python image_viewer.py
   ```
   
2. The GUI window will open with the following components:
   - An input field to provide the path to an image file.
   - A "Load Image" button to load the selected image.
   - A graphical area where the loaded image will be displayed.
   - A text area to display information about drawn rectangles.
   
3. Click the "Load Image" button and select an image file from your file system.

4. The loaded image will be displayed in the graphical area. You can use the mouse to draw rectangles on the image:
   - Click and hold the mouse to start drawing a rectangle.
   - Drag the mouse to define the rectangle's dimensions.
   - Release the mouse button to finalize the rectangle.

5. Information about the drawn rectangle will be displayed in the text area below the graphical window.

6. You can exit the application by clicking the "X" button in the top-right corner of the window or pressing the "Exit" button.

## Notes

- The PySimpleGUI library provides a simple way to create graphical user interfaces (GUIs) using Python.
- The Pillow library (PIL Fork) is used to manipulate and display images.

## Disclaimer

This script is provided for educational and demonstrative purposes. It's a basic implementation and may not cover all edge cases or provide a complete image viewer application.
