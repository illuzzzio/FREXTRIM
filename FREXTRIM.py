from moviepy import VideoFileClip
import cv2



Que = input("Do you want to extract audio from a video file?  trim it or want each frame from the video? press e for extraction, t for trimming and f for frame extraction...  ").lower()

my_aud="aud.mp3"
trim_file="trimmed.mp4"

def extraxt():
    video = VideoFileClip(test_video)
    audio = video.audio
    audio.write_audiofile(my_aud)
    print("Audio extracted successfully!")
    video.close()
    audio.close()

def trimmer(test_video,start,end):
    video = VideoFileClip(test_video)
    trimmed_clip = video.subclipped(start,end)
    trimmed_clip.write_videofile(trim_file)
    video.close()
    trimmed_clip.close()  
    print("Video trimmed successfully!")


import cv2

def framecap(test_video):
    video_capture = cv2.VideoCapture(test_video)
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))  # Frames per second
    success, image = video_capture.read()
    count = 0
    sec_count = 0

    while success:
        if count % fps == 0:  # Capture one frame every second
            cv2.imwrite(f'frame_{sec_count}.jpg', image)
            sec_count += 1
        success, image = video_capture.read()
        count += 1

    video_capture.release()
    print(f"Extracted {sec_count} frames (1 per second) from {test_video}")

 
if(Que=="e"):
  test_video = input("Enter the path to the video file in mp4 format: ") 
  extraxt()


elif(Que=="t"):
    test_video = input("Enter the path to the video file in mp4 format: ")
    start = input("Enter a start time in seconds")
    end = input("Enter a end time in seconds")
    trimmer(test_video,int(start),int(end))


elif(Que=="f"):
    test_video = input("Enter the path to the video file in mp4 format: ")
    framecap(test_video)

else:
    print("Invalid input. Please enter 't' , 'e' or 'f'.")
    exit()





