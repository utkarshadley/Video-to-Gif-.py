from moviepy.editor import *

video= VideoFileClip("ride.mp4").subclip(10,16)
video.write_gif("test2.gif")