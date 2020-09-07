import tkinter as tk
from tkinter import font as tkfont
from getId import Id_Collect
from games import Game
from wins import Win_Calc



class RiotApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, MenuPage, KillPage, DeathPage, CsPage, HonestPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


    class StartPage(tk.Frame):

        def __init__(self, parent, controller):
        
            tk.Frame.__init__(self, parent)
            c = DataCollected()
            self.controller = controller
            self.label = tk.Label(self, text="Enter summoner name:", width = 20, font = ("bold", 20))
            self.label.place(x=90,y=53)
            self.entry1 = tk.Entry(self)
            self.entry1.place(x=190,y=130)
            
            self.button = tk.Button(self, text="Search",width = 20, bg = 'brown', fg = 'white',
                                command=lambda: data_collected())
            self.button.place(x=180,y=200)

            def data_collected():
            
                name = self.entry1.get()
                Key = 'RGAPI-d50f2f74-2c9d-46e6-94d1-f2b3bd4755bf'
                ids = Id_Collect()
                a = ids.id_collected(name, Key)
                if a != 'NO':
                    controller.show_frame("MenuPage")
                    stat_list = c.collect_data(name)
                else:
                    controller.show_frame('StartPage')
        
            


class DataCollected():
    

    def collect_data(self, name):

        Key = 'RGAPI-d50f2f74-2c9d-46e6-94d1-f2b3bd4755bf'
        num_games = 20
        ids = Id_Collect()
        game = Game()
        wins = Win_Calc()
        accId = ids.id_collected(name, Key)
        game_list = game.find_game_ids(accId, Key, num_games)
        #global stat_list
        stat_list = game.game_data(game_list, Key, name, num_games)
        return stat_list

    #stat_list = []
        
    



class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Main Menu", font=controller.title_font)
        label.place(x=180,y=50)
        button = tk.Button(self, text="Kill Average",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("KillPage")).place(x=180,y=100)
        button = tk.Button(self, text="Death Average",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("DeathPage")).place(x=180,y=150)
        button = tk.Button(self, text="Cs Average",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("CsPage")).place(x=180,y=200)
        button = tk.Button(self, text="Honest Truth",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("HonestPage")).place(x=180,y=250)
        button = tk.Button(self, text="Back",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("StartPage")).place(x=180,y=300)


class KillPage(tk.Frame, DataCollected):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text= ' ', font = controller.title_font)
        label.pack(side = "top", fill ="x", pady=10)
        button = tk.Button(self, text = "Back", width = 20, bg = 'brown', fg = 'white',
                        command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)


class DeathPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back", width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)

class CsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="", font=controller.title_font)
        label.pack(side="top", fill = "x", pady = 10)
        button = tk.Button(self, text="Back", width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)


class HonestPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="", font=controller.title_font)
        label.pack(side = "top", fill = "x", pady = 10)
        button = tk.Button(self, text="Back", width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)


if __name__ == "__main__":

    root = RiotApp()
    root.geometry("500x500")
    root.mainloop()












    
    

    













