from customtkinter import *
from PIL import Image, ImageTk


class Window(CTk):
    def __init__(self):
        super().__init__()
        self.title("my player")
        self.geometry("1024x640")
        self.grid_rowconfigure(0, weight=1)
        set_appearance_mode("dark")
        set_default_color_theme("lavender.json")

        self.play_pause_state = "pause"

        
        #обложка
        self.song_icon_frame = CTkFrame(self, fg_color="transparent")
        self.song_icon_frame.grid(row=0, column=0, padx=555, pady=(150, 0), sticky="nsw")

        self.my_image = CTkImage(dark_image=Image.open("images/cover.png"), size=(220, 220))
        self.image_label = CTkButton(self.song_icon_frame, image=self.my_image, command=None, text="", fg_color="transparent", hover="transparent")
        self.image_label.grid(row=0, column=2, padx=5, pady=0, columnspan=1)

        #фрейм, хранящий инфу песенки
        self.song_info_frame = CTkFrame(self, fg_color="transparent")
        self.song_info_frame.grid(row=0, column=0, padx=610, pady=(380, 0), sticky="nsw")

        self.music_name_label = CTkLabel(self.song_info_frame, text="Название песни", font=(None, 16), justify=CENTER)
        self.music_name_label.grid(row=1, column=2, padx=5, pady=5, columnspan=1)

        self.music_author_label = CTkLabel(self.song_info_frame, text="Исполнитель", font=(None, 13), justify=CENTER)
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
        if self.play_pause_state == "pause":
            self.play_btn.configure(text="⏸️")
            self.play_pause_state = "play"
            #Проигрывание музона

        elif self.play_pause_state == "play":
            self.play_btn.configure(text="▶️")
            self.play_pause_state = "pause"
            

if __name__ == "__main__":
    app = Window()
    app.mainloop()