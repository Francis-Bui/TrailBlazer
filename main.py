import imageio
from algo import find_path, Point
from tmap import Map
import io
import os
import PySimpleGUI as sg
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]


def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("x,y"),
            sg.Input(size=(10, 1), key="coordOne"),
            sg.Text("x,y"),
            sg.Input(size=(10, 1), key="coordTwo"),
            sg.Text("Scale/pixel"),
            sg.Input(size=(5, 1), key="scale"),
            sg.Text("Height scale"),
            sg.Input(size=(5, 1), key="height_scale"),

            [
                sg.Text("Image File"),
                sg.Input(size=(25, 1), key="-FILE-"),
                sg.FileBrowse(file_types=file_types),
                sg.Button("Load Image"),
            ],
        ],
    ]
    window = sg.Window("Image Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            coordOne = values["coordOne"]
            coordTwo = values["coordTwo"]
            pixel_scale = int(values["scale"])
            height_scale = int(values["height_scale"])
            c1 = [int(i) for i in coordOne.split(', ')]
            c2 = [int(i) for i in coordTwo.split(', ')]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
                img = imageio.imread(filename)  # 512x1024x3 array
                topo_map = Map(img, height_scale, pixel_scale)
                secondOne = False

                path = find_path(topo_map, Point(
                    c1[0], c1[1]), Point(c2[0], c2[1]))
                dist = len(path)  # multiply
                an_array = np.array(path)
                plt.imshow(an_array)
                plt.show()
                # Construct the shortest path
    window.close()


if __name__ == "__main__":
    main()


def main():
    elements = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), enable_events=True, key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
        ],
    ]
    window = sg.Window("Image Viewer", elements)