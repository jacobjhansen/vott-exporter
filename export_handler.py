import PIL
import cv2

def return_frame(videopath,frame_number):
    cap = cv2.VideoCapture(videopath)
    cap.set(cv2.CV_CAP_PROP_POS_FRAMES, frame_number-1)
    res, frame = cap.read()


def main(asset_list):
    return_frame(asset_list[0].source,asset_list[0].timestamp)




# import cv2
#
## Opens the Video file
# cap= cv2.VideoCapture('C:/New/Videos/Play.mp4')
# i=0
# while(cap.isOpened()):
#    ret, frame = cap.read()
#    if ret == False:
#         break
#    cv2.imwrite('kang'+str(i)+'.jpg',frame)
#    i+=1
#
# cap.release()
# cv2.destroyAllWindows()