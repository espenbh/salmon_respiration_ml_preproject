import cv2
start_frame = 5000
num_frames_in_video = 1000
vidcap = cv2.VideoCapture('C:\\Users\\espebh\\Documents\\project\\data\\videos\\4t tank 9.MP4')
vidcap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
success, image = vidcap.read()
while success:
    if vidcap.get(cv2.CAP_PROP_POS_FRAMES) % 100 == 0:
        print(vidcap.get(cv2.CAP_PROP_POS_FRAMES)) 
    cv2.imwrite("C:\\Users\\espebh\\Documents\\project\\data\\videos\\split video\\frame%d.jpg" % vidcap.get(cv2.CAP_PROP_POS_FRAMES), image)     # save frame as JPEG file      
    success,image = vidcap.read()
    if vidcap.get(cv2.CAP_PROP_POS_FRAMES) > start_frame + num_frames_in_video:
        break
vidcap.release()  