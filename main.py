# Compare an image with every frame of a video to find the best match

import os
import operator
import cv2
from skimage import color
from skimage.metrics import structural_similarity as ssim


def parse_video(image,imgName):
    #iterate through video frames
    similarities = []
    
    
    frame_count = -1

    for f in os.listdir("frames"): 
        #increment frame counter
        frame_count += 1
        #resize current video frame
        small_frame = cv2.imread("frames\\"+f)
        small_frame = cv2.resize(small_frame, (10, 10))
        #convert to greyscale
        small_frame_bw = color.rgb2gray(small_frame)

        #compare current frame to source image
        similarity = ssim(image, small_frame_bw, gaussian_weights=True, sigma=1.5, use_sample_covariance=False, data_range=255)

        similarities.append([imgName,f,similarity])


        


        
        
        #sort similarities list
        #similarities = sorted(similarities, key=operator.itemgetter('similarity'), reverse=True)

    similarities.sort(key=lambda a: a[2])     

    return similarities

def main():    
    for f in os.listdir("tags") :
        img = cv2.imread("tags\\"+f)
        #shrink
        img = cv2.resize(img, (10, 10))
        #convert to b&w
        img = color.rgb2gray(img)
        print(parse_video(img,f))

if __name__ == '__main__':
    main()



    

