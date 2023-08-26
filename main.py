import PySimpleGUI as sg
import io, os
from PIL import Image

#ayout of the GUI window
layout = [
    [
        sg.Input(size=(25, 1), key="-FILE-"),
        sg.FileBrowse(file_types=[("All extensions (*.*)", "*.*")]),
        sg.Button("Load Image")
    ],
    [
        sg.Graph((500, 377), (0, 0), (400, 400), key="-GRAPH-",
                 enable_events=True, drag_submits=True, background_color="white", pad=(10, 10))
    ],
    [sg.Text(key='Info', size=(60, 1), text_color="red")]  # Information text display area
]

# GUI window
window = sg.Window("Image Viewer", layout)

# track rectangle drawing
dragging = False
start_point = end_point = prior_rect = None

# Main event loop
while True:
    event, values = window.read()

    # Exit the application if the window is closed
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # Load selected image when "Load Image" button is clicked
    if event == "Load Image":
        filename = values["-FILE-"]
        if os.path.exists(filename):

            # pillow to open all types of images
            image = Image.open(filename)
            image.thumbnail((500, 460))
            bio = io.BytesIO()

            # Convert and display image in the GUI
            image.save(bio, format="PNG")
            window["-GRAPH-"].draw_image(data=bio.getvalue(), location=(0, 400))

    # Handle rectangle drawing on the image
    if event == "-GRAPH-":
        x, y = values["-GRAPH-"]
        if not dragging:
            start_point = (x, y)
            dragging = True
            window.set_cursor("crosshair")
        else:
            end_point = (x, y)
        if prior_rect:
            window["-GRAPH-"].delete_figure(prior_rect)
        if None not in (start_point, end_point):
            prior_rect = window["-GRAPH-"].draw_rectangle(start_point, end_point, line_color='red')

    # Finalize rectangle drawing and update information
    if event.endswith('+UP'):
        window["Info"].update(value=f"Grabbed rectangle from {start_point} to {end_point}")
        start_point, end_point = None, None
        dragging = False
        window.set_cursor("arrow")

# close
window.close()
