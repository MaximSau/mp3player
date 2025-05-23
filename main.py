from customtkinter import *
from PIL import Image
from song_inf import *
from pygame import mixer


class ScrollableLabelButtonFrame(CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, number, item, image=None):
        label = CTkLabel(self, text=number, image=image, compound="left", padx=5, anchor="w")
        if len(item) > 21:
            button = CTkButton(self, text=item[:21:]+"...", width=190, height=28, font=(None, 14), fg_color="transparent")
        else:
            button = CTkButton(self, text=item, width=190, height=28, fg_color="transparent")
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item=None, number=None):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return


class Window(CTk):
    def __init__(self):
        super().__init__()
        self.title("my player")
        self.geometry("1024x640")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        set_appearance_mode("dark")
        set_default_color_theme("lavender.json")

        self.play_pause_state = "play"
        mixer.init()


        #Выбор папки с песенками
        self.browse_frame = CTkFrame(self, fg_color="transparent")
        self.browse_frame.grid(row=0, column=0, padx=0, pady=(7, 0), sticky="nsw")
        self.browse_button = CTkButton(self.browse_frame, text="📁", command=None, font=(None, 16), width=270, height=30)
        self.browse_button.grid(row=0, column=0, padx=5, pady=5)

        self.song_info = get_song_info('test.mp3')


        #тут скроллбар
        self.scrollbar = ScrollableLabelButtonFrame(self.browse_frame, height=550, width=260, fg_color="transparent")
        self.scrollbar.grid(row=2, column=0, padx=5, pady=5)
        for i in range(100):
            self.scrollbar.add_item(number=i, item="124124125")

        
        #обложка
        self.song_icon_frame = CTkFrame(self, fg_color="transparent")
        self.song_icon_frame.grid(row=0, column=0, padx=555, pady=(150, 0), sticky="nsw")

        self.my_image = CTkImage(dark_image=Image.open("images/cover.png"), size=(220, 220))
        self.image_label = CTkButton(self.song_icon_frame, image=self.my_image, command=None, text="", fg_color="transparent", hover="transparent")
        self.image_label.grid(row=0, column=2, padx=5, pady=0, columnspan=1)

        #фрейм, хранящий инфу песенки
        self.song_info_frame = CTkFrame(self, fg_color="transparent")
        self.song_info_frame.grid(row=0, column=0, padx=610, pady=(380, 0), sticky="nsw")

        self.music_name_label = CTkLabel(self.song_info_frame, text=self.song_info[-1], font=(None, 16), justify=CENTER)
        self.music_name_label.grid(row=1, column=2, padx=5, pady=5, columnspan=1)

        self.music_author_label = CTkLabel(self.song_info_frame, text=self.song_info[0], font=(None, 13), justify=CENTER)
        self.music_author_label.grid(row=2, column=2, padx=5, pady=5, columnspan=1)

        #Фрейм, хранящий кнокпи переключения музыки
        self.player_buttons_frame = CTkFrame(self, fg_color="transparent")
        self.player_buttons_frame.grid(row=0, column=0, padx=550, pady=(500, 0), sticky="nsw")

        self.play_btn = CTkButton(self.player_buttons_frame, text="▶️", command=self.play_song, height=50, font=(None, 20), width=20, corner_radius=180)
        self.play_btn.grid(row=1, column=2, padx=5, pady=10, columnspan=1)

        self.next_btn = CTkButton(self.player_buttons_frame, text="⏩", command=None, height=40, font=(None, 20), width=10, corner_radius=180)
        self.next_btn.grid(row=1, column=3, padx=5, pady=10, columnspan=1)

        self.back_btn = CTkButton(self.player_buttons_frame, text="⏪", command=None, height=40, font=(None, 20), width=10, corner_radius=180)
        self.back_btn.grid(row=1, column=1, padx=5, pady=10, columnspan=1)
        

    def play_song(self):
        mixer.music.load('test.mp3')
        mixer.music.play()
        if self.play_pause_state == "pause":
            self.play_btn.configure(text="⏸️")
            self.play_pause_state = "play"
            #Проигрывание музона
            mixer.music.unpause()

        elif self.play_pause_state == "play":
            self.play_btn.configure(text="▶️")
            self.play_pause_state = "pause"
            mixer.music.load('test.mp3')
            mixer.music.pause()


            

if __name__ == "__main__":
    app = Window()
    app.mainloop()
