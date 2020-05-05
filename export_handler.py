import PIL
from PIL import Image
from cv2 import cv2
import ffmpeg
from io import BytesIO

def save_frame_as_jpeg(in_filename, frame_num,out_filename):
    out, err = (
        ffmpeg
        .input(in_filename)
        .filter('select', 'gte(n,{})'.format(frame_num))
        .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
        .run(capture_stdout=True)
    )
    file_jpgdata = BytesIO(out)
    frame = Image.open(file_jpgdata)
    frame.save(out_filename)


def main(asset_list):
    #save_frame_as_jpeg('/home/jacobhansen/FeedNet V1/train/raw/GH010001.MP4',500,'/home/jacobhansen/export_frames/test.jpg')
    pass





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