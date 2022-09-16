import tkinter as tk
class PlayerActor:
    def __init__(self):
        self.__main_window = tk.Tk()
        self.__main_window.title("Pontu!!")
        self.__main_window.geometry("485x485")
        self.__main_window["bg"] = "red"
        self.__is_crown_turn = True
        self.__main_frame = tk.Frame(self.__main_window,
                                     bg="red")

        # pyimage1
        self.__empty_rock = tk.PhotoImage(file="images/rock.png")
        # pyimage2
        self.__v_bridge = tk.PhotoImage(file="images/bridge_v.png")
        # pyimage3
        self.__h_bridge = tk.PhotoImage(file="images/bridge_h.png")
        # pyimage4
        self.__water = tk.PhotoImage(file="images/water.png")
        # pyimage5
        self.__skull_rock = tk.PhotoImage(file="images/skull_rock.png")
        # pyimage6
        self.__crown_rock = tk.PhotoImage(file="images/crown_rock.png")

        self.__board_view = []
        for y in range(9):
            line = []
            for x in range(9):
                if x % 2 == 0 and y % 2 == 0:
                    label = tk.Label(self.__main_frame,
                                     bd=2,
                                     relief="solid",
                                     image=self.__empty_rock)
                elif y % 2 == 0:
                    label = tk.Label(self.__main_frame,
                                     bd=2,
                                     relief="solid",
                                     image=self.__v_bridge)
                elif x % 2 == 0:
                    label = tk.Label(self.__main_frame,
                                     bd=2,
                                     relief="solid",
                                     image=self.__h_bridge)
                else:
                    label = tk.Label(self.__main_frame,
                                     bd=2,
                                     relief="solid",
                                     image=self.__water)
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

PlayerActor()
