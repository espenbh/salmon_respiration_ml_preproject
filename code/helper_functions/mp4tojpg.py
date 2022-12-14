import cv2
vidcap = cv2.VideoCapture('C:\\Users\\espebh\\Documents\\project\\data\\videos\\original videos\\2ttank9.avi')
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("C:\\Users\\espebh\\Documents\\project\\data\\videos\\split video\\frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    count += 1
    if not count % 100:
        print('Frame nr: ', count)


vidcap.release()  

# import numpy as np  
# import cv2  
  
# cap = cv2.VideoCapture('C:\\Users\\espebh\\Documents\\project\\data\\videos\\original videos\\4t tank 9.mp4')  
  
# while(cap.isOpened()):  
#     ret, frame = cap.read()  
# #it will open the camera in the grayscale mode  
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
  
#     cv2.imshow('frame',gray)  
#     if cv2.waitKey(1) & 0xFF == ord('q'):  
#         break  
  
# cap.release()  
# cv2.destroyAllWindows()  