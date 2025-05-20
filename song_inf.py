import eyed3
from PIL import Image

def get_song_info(song_name):
    audio_file = eyed3.load(song_name)
    
    result = [
            audio_file.tag.artist,
            audio_file.tag.album,
            audio_file.tag.title,    
        ]


    return result