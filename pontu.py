import tkinter as tk
from PIL import Image, ImageTk
class PlayerActor:
    def __init__(self):
        self.__main_window = tk.Tk()
        self.__main_window.title("Pontu!!")
        self.__size = 2
        self.__main_window.geometry(f"{450*self.__size}x{450*self.__size}")
        self.__main_window["bg"] = "red"
        self.__is_crown_turn = True
        self.__main_frame = tk.Frame(self.__main_window,
                                     bg="red")

        # pyimage1
        self.__empty_rock = self.resize("images/rock.png")
        # pyimage2
        self.__v_bridge = self.resize("images/bridge_v.png")
        # pyimage3
        self.__h_bridge = self.resize("images/bridge_h.png")
        # pyimage4
        self.__water = self.resize("images/water.png")
        # pyimage5
        self.__skull_rock = self.resize("images/skull_rock.png")
        # pyimage6
        self.__crown_rock = self.resize("images/crown_rock.png")

        self.__board_view = []
        for y in range(9):
            line = []
            for x in range(9):
                img = None
                if x % 2 == 0 and y % 2 == 0:
                    img = self.__empty_rock 
                elif y % 2 == 0:
                    img = self.__v_bridge
                elif x % 2 == 0:
                    img = self.__h_bridge
                else:
                    img = self.__water 
                label = tk.Label(self.__main_frame,
                                 bd=0,
                                 relief="solid",
                                 image=img)
                label.grid(row = x, column = y)
                label.bind("<Button-1>", lambda event, line = y+1,
                        column=x+1: self.click(event, line, column))
                line.append(label)
            self.__board_view.append(line)

        self.__main_frame.grid(row=0, column=0)
        self.__main_window.mainloop()
    
    def click(self, event, linha, coluna):
        label=self.__board_view[linha-1][coluna-1]
        if label['imag'] == "pyimage2" or label['imag'] == "pyimage3":
            label['imag'] = self.__water
        if label['imag'] == "pyimage1":
            replace = self.__crown_rock if self.__is_crown_turn else self.__skull_rock
            label['imag'] = replace
            self.__is_crown_turn = not self.__is_crown_turn

    def resize(self, file_path:str):
        img = Image.open(file_path)
        img = img.resize((50*self.__size, 50*self.__size))
        img = ImageTk.PhotoImage(img)
        return img

PlayerActor()
