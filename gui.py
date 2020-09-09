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
                            command=lambda: data_collected(self,controller))
        self.button.place(x=180,y=200)

        def data_collected(self,controller):
        
            name = self.entry1.get()
            Key = 'RGAPI-446824c1-a469-4c6c-95ca-4a5b911ba745'
            ids = Id_Collect()
            a = ids.id_collected(name, Key)
            if a != 'NO':
                controller.show_frame("MenuPage")
                stat_list = c.collect_data(name, Key)
            else:
                controller.show_frame('StartPage')

class DataCollected():
    
    def collect_data(self, name, Key):

        num_games = 20
        ids = Id_Collect()
        game = Game()
        wins = Win_Calc()
        accId = ids.id_collected(name, Key)
        game_list = game.find_game_ids(accId, Key, num_games)
        global stat_list
        stat_list = game.game_data(game_list, Key, name, num_games)
        return stat_list

class MenuPage(tk.Frame,DataCollected):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Main Menu", font=controller.title_font)
        label.place(x=180,y=50)
        button = tk.Button(self, text="Kill Average",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: [controller.show_frame("KillPage"), change_label]).place(x=180,y=100)
        button = tk.Button(self, text="Death Average",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("DeathPage")).place(x=180,y=150)
        button = tk.Button(self, text="Cs Average",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("CsPage")).place(x=180,y=200)
        button = tk.Button(self, text="Honest Truth",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("HonestPage")).place(x=180,y=250)
        button = tk.Button(self, text="Back",width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("StartPage")).place(x=180,y=300)
        def change_label():
            self.label1.configure(text=stat_list[0])

class KillPage(tk.Frame, DataCollected):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text = 'Kills Average', width=20,font=("bold", 20))
        self.label.place(x=90, y=100)
        self.label1 = tk.Label(self, text = ' ', width=20,font=("bold", 20))
        self.label1.place(x=90, y=150)
        self.label1.after(1000, self.refresh_label)
        self.button = tk.Button(self, text = "Back", width = 20, bg = 'brown', fg = 'white',
                        command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)
    def refresh_label(self):
        self.label1.configure(text = stat_list[1])
        self.label1.after(1000,self.refresh_label)

class DeathPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text = 'Deaths Average', width=20,font=("bold", 20))
        self.label.place(x=90, y=100)
        self.label2 = tk.Label(self, text="", width=20,font=("bold", 20))
        self.label2.place(x=90, y=150)
        self.label2.after(1000, self.refresh_label)
        self.button = tk.Button(self, text="Back", width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)
    def refresh_label(self):
        self.label2.configure(text = stat_list[0])
        self.label2.after(1000,self.refresh_label)

class CsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text = 'Cs Average', width=20,font=("bold", 20))
        self.label.place(x=90, y=100)
        self.label3 = tk.Label(self, text="", width=20,font=("bold", 20))
        self.label3.place(x=90,y=150)
        self.label3.after(1000, self.refresh_label)
        self.button = tk.Button(self, text="Back", width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)
    def refresh_label(self):
        self.label3.configure(text = stat_list[4])
        self.label3.after(1000,self.refresh_label)

class HonestPage(tk.Frame):

    def __init__(self, parent, controller):
        wins = Win_Calc()
        self.honest = wins.is_player_good(stat_list[5])
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text = 'Honest Truth', width=20,font=("bold", 20))
        self.label.place(x=90, y=100)
        self.label4 = tk.Label(self, text = " ", width=20,font=("bold", 20))
        self.label4.place(x=90,y=150)
        self.label4.after(1000, self.refresh_label(self.honest))
        self.button = tk.Button(self, text = "Back", width = 20, bg = 'brown', fg = 'white',
                           command=lambda: controller.show_frame("MenuPage")).place(x=180,y=300)
    def refresh_label(self, honest):
        self.label4.configure(text = honest)
        self.label4.after(1000,self.refresh_label)


if __name__ == "__main__":

    stat_list = [1,1,1,1,1,1,1]
    root = RiotApp()
    root.geometry("500x500")
    root.mainloop()









    
    

    













