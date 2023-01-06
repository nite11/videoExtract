#source https://www.geeksforgeeks.org/moviepy-concatenating-multiple-video-files/

# Import everything needed to edit video clips
from moviepy.editor import *
import re

position=[]

with open('frameInfo.txt','r') as f:
    lines=f.readlines() 
for line in lines:
    position.append(int(re.sub("\D", "", line)))  #to get the frame number which is equivalent 
                                                    #to seconds from start of the video

position.sort()

#to consolidate all the positions within 5 seconds of each other into a single position
i=0
while i<len(position)-1:
    if position[i]+5>position[i+1]:
        position.pop(i+1)
    else:
        i+=1



# loading video dsa gfg intro video
clip = VideoFileClip("video\Sumida.mp4")
clips=[]

#cutting 10 second subclips from 5 seconds before the position to 5 seconds after the position.
#further code has to be written here to handle, for example, if first or last frame of the video is tagged
for j in range(len(position)):
    clips.append(clip.subclip(position[j]-5, position[j]+5))  

# concatenating both the clips
final = concatenate_videoclips(clips)
#writing the video into a file / saving the combined video
final.write_videofile("shortVideo.mp4")



