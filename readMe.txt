Run createFrames.py 
to extract frames from the video and store in a folder called "frames".
Frames are extracted at intervals of 1 second. So a 156 second video will generate 157 (0-156) frames.

Run tagFrames.py 
This is the program that takes each frame and searches it on Google Image search. The search result is a 
webpage with few suggested links and a section that contains "similar images". Then the program automatically
clicks on this "similar images" link by identifying it by <div class="iJ1Kvb">. I tried this on
different accounts, computers and networks to make sure that the class_name does not change. Clicking on this
opens a Google Image search result page with similar images and descriptions/urls of these images.
Then the text of these urls/descriptions is matched with the input tags. If there is a match, the framename
is stored along with the tag in the frameInfo.txt file.

Run shortVideo.py
This program extracts the position of the frames from the frameInfo.txt file, and based on that makes 
subclips from the original video, then concatenates the subclips.

