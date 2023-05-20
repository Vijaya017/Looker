from tkinter import ttk
import tkinter as tk
from google_images_search import GoogleImagesSearch
import requests
from PIL import ImageTk, Image
from io import BytesIO


class Searchingengine:
    def __init__(self):
        self.gis = GoogleImagesSearch("YOUR API ID","YOUR USER KEY")
        self.root = tk.Tk()
        self.root.geometry("800x800")
        self.root.title("Looker - Look what you want")
        self.root.resizable(False, False)
        self.root.config(background='#4682B4')

        self.entry=tk.Entry(self.root, width=50,foreground="#1c1d1d",font=("Arial",16))
        self.entry.insert(0,"type to search")
        self.entry.pack(padx=30,pady=30)

        self.button = ttk.Button(self.root, command=self.getimage,text="Search")
        self.button.pack()

        self.labels=[]
        for i in range (2):
            label=tk.Label(self.root,height=50,width=50)
            label.pack()
            self.labels.append(label)


        self.root.mainloop()

    def getimage(self):
        query = self.entry.get()
        self.gis.search({'q': query, 'num': 2})

        counter=0

        for result in self.gis.results():
            imagedata=requests.get(result.url).content
            img=ImageTk.PhotoImage(Image.open(BytesIO(imagedata)))
            self.labels[counter].config(image=img)
            self.labels[counter].image=img
            counter+=1

if __name__ == '__main__':
    engine = Searchingengine()


