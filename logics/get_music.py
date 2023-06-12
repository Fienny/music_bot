import os
import pytube

# link = 'https://www.youtube.com/watch?v=G3-jWRbc3Uw'
def get_music(link):

    yt = pytube.YouTube(link)
    vid = yt.streams.filter(only_audio=True).first()

    out_file = vid.download()

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    return new_file


# get_music(link)

def delete_file(path):
    os.remove(path)
