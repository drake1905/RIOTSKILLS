import tkinter as tk
from tkinter import font as tkfont
from getId import id_collected
from games import Game
from wins import is_player_good


class RiotApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.stat_list = []
        self.statList = tk.IntVar()
        self.statList.set(1)
        self.honest = " "
        self.honest_label = tk.StringVar()
        self.honest_label.set(" ")
        self.entry = " "

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #Making the other frames of the class with references of this class
        for F in (StartPage, MenuPage, KillPage, DeathPage, CsPage, HonestPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    #Raising frames when call uponed
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    #Using uses a function to determine if user is real and advance to next frame while collecting data
    def data_collected(self,controller):
            
            name = self.entry.get()
            key = 'RGAPI-02a1fc2f-1afa-4fa3-bd27-12e267e3c5b6'
            id_list = id_collected(name, key)
            if id_list != 'NO':
                self.show_frame("MenuPage")
                self.stat_list,self.honest = self.collect_data(name, key)
            else:
                self.show_frame('StartPage')

    #This will collect data from riot api
    def collect_data(self, name, key):
        num_games = 20
        game = Game()
        accId = id_collected(name, key)
        game_list = game.find_game_ids(accId, key, num_games)
        stat_list = game.game_data(game_list, key, name, num_games)
        honest = is_player_good(stat_list[5])
        return stat_list,honest

    #Setting label for other classes via IntVar and StringVar
    def make_stat_list(self, label_switch):

        if label_switch == 1:
            self.statList.set(self.stat_list[1])
        elif label_switch == 2:
            self.statList.set(self.stat_list[0])
        elif label_switch == 3:
            self.statList.set(self.stat_list[4])
        elif label_switch == 4:
            self.honest_label.set(self.honest)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text="Enter summoner name:", width = 20, font = ("bold", 20))
        self.label.place(x=90,y=53)

        controller.entry = tk.Entry(self)
        controller.entry.place(x=190,y=130)
        
        self.button = tk.Button(self, text="Search",width = 20, bg = 'brown', fg = 'white',
                            command=lambda: controller.data_collected(self))
        self.button.place(x=180,y=200)

class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Main Menu", font=controller.title_font)
        label.place(x=180,y=50)

        button = tk.Button(self, text="Kill Average",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: [controller.show_frame("KillPage"), controller.make_stat_list(label_switch = 1)]).place(x=180,y=100)
        button = tk.Button(self, text="Death Average",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: [controller.show_frame("DeathPage"), controller.make_stat_list(label_switch = 2)]).place(x=180,y=150)
        button = tk.Button(self, text="Cs Average",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: [controller.show_frame("CsPage"), controller.make_stat_list(label_switch = 3)]).place(x=180,y=200)
        button = tk.Button(self, text="Honest Truth",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: [controller.show_frame("HonestPage"), controller.make_stat_list(label_switch = 4)]).place(x=180,y=250)
        button = tk.Button(self, text="Back",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("StartPage")).place(x=180,y=300)

class KillPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text = 'Kills Average', width=20,font=("bold", 20))
        self.label.place(x=90, y=100)

        self.label1 = tk.Label(self, textvariable =controller.statList, width=20,font=("bold", 20))
        self.label1.place(x=90, y=150)

        self.button = tk.Button(self, text = "Back", width = 20, bg = 'brown', fg = 'white',
                        command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)

class DeathPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text = 'Deaths Average', width=20,font=("bold", 20))
        self.label.place(x=90, y=100)

        self.label2 = tk.Label(self, textvariable=controller.statList, width=20,font=("bold", 20))
        self.label2.place(x=90, y=150)

        self.button = tk.Button(self, text="Back", width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)

class CsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text = 'Cs Average', width=20,font=("bold", 20))
        self.label.place(x=90, y=100)

        self.label3 = tk.Label(self, textvariable= controller.statList, width=20,font=("bold", 20))
        self.label3.place(x=90,y=150)

        self.button = tk.Button(self, text="Back", width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)

class HonestPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.label = tk.Label(self, text = 'Honest Truth', width=20,font=("bold", 20))
        self.label.place(x=90, y=100)

        self.label4 = tk.Label(self, textvariable =controller.honest_label, width=20,font=("bold", 20))
        self.label4.place(x=90,y=150)
        
        self.button = tk.Button(self, text = "Back", width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)

if __name__ == "__main__":
    root = RiotApp()
    root.geometry("500x500")
    root.mainloop()









    
    

    













