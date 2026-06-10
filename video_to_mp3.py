import os
import subprocess

files = os.listdir("videos")

for file in files:
    print(file)
    tutorial_number = file.split(" #")[1].split(".mp4")[0]
    print(tutorial_number)
    file_name = file.split(" !")[0]
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])


'''
file name could be 'Basic Structure of an HTML Website _ Sigma Web Development Course - Tutorial #3.mp4', 
from YOUTUBE from CodewithHarry web dev course. 
'''
