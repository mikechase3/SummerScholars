'''Mike Chase's Summer Scholar Flashcards'''


from PIL.ImageTk import PhotoImage

'''
REQUIREMENTS
1. Photos should be 500x500 in PNG format.
2. 
'''

from typing import List, Dict
import random
import tkinter as tk
import pandas as pd
import os
from PIL import ImageTk, Image


def loadPhotos() -> Dict[str, PhotoImage]:
    """
    Loads the photos in the 'photos' directory.
    :return: dictionary of filenames without the jpg/png and the corresponding PhotoImage object.
    """
    photoImages: List[tk.PhotoImage] = []
    current_directory: os.path = os.getcwd()
    photos_dir: os.path = os.path.join(current_directory, "photos")

    # Load the photos into a dictionary. Key is filename. Value is the PhotoImage object.
    images = {}
    for file in os.listdir(current_directory):
        if file.endswith(".jpg") or file.endswith(".png"):
            # Load the image
            image: Image = Image.open(file)
            photo: ImageTk.PhotoImage = ImageTk.PhotoImage(image)
            # photo_name: str = file.strip(".png").strip(".jpg")
            print("ADDED")

            images[file] = photo

    return images
dict_photos = loadPhotos()

class QuestionAndAnswer(tk.Frame):
    # Instance Variables
    df = pd.read_excel("info.xlsx", header=0)
    num_rows = len(df)
    dict_photos = loadPhotos()

    # Constructor
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get a random row.
        random_row_num = random.randint(1, self.num_rows-1)  # Select a random row besides the header
        random_row = self.df.iloc[random_row_num].tolist()
        photo_path, fName, lName, fact = random_row  # Query from excel

        # Pack
        l_photo = tk.Label(self, image=self.dict_photos[photo_path])
        l_photo.pack(side=tk.LEFT)

        tk.Label(self, text=fName).pack()
        tk.Label(self, text=lName).pack()
        tk.Label(self, text=fact).pack()




# Instance Variables & Setup
root = tk.Tk()
score = tk.IntVar(root, 0)

# Header
f_header = tk.Frame(root)
l_title = tk.Label(f_header, text="GRILL Summer Scholars | 2023", justify=tk.CENTER)
l_title.config(font=("Arial", 10, "bold"))
l_title.pack(side=tk.LEFT)

l_score = tk.Label(f_header, text=("Score: {}".format(score.get())))
l_score.pack(side=tk.LEFT)
f_header.pack()

# Question Frame
qa = QuestionAndAnswer(root)
qa.pack()

root.mainloop()
