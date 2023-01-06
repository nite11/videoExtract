#source https://www.geeksforgeeks.org/moviepy-concatenating-multiple-video-files/

# Import everything needed to edit video clips
from moviepy.editor import *
import re

position=[]

with open('frameInfo.txt','r') as f:
    lines=f.readlines() 
for line in lines:
    position.append(int(re.sub("\D", "", line)))

position.sort()

i=0
while i<len(position)-1:
    if position[i]+5>position[i+1]:
        position.pop(i+1)
        #print(position)
    else:
        i+=1
#print(position)


# loading video dsa gfg intro video
clip = VideoFileClip("video\Sumida.mp4")
clips=[]

for j in range(len(position)):
    #print(position[j]+5)
    clips.append(clip.subclip(position[j]-5, position[j]+5))  #write code for clip from start or end of video

# concatenating both the clips
final = concatenate_videoclips(clips)
#writing the video into a file / saving the combined video
final.write_videofile("shortVideo.mp4")



