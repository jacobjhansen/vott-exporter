import PIL
from PIL import Image
from cv2 import cv2
import ffmpeg
from io import BytesIO
import sys,os

def get_frame_as_jpeg(in_filename, frame_num):
    out, err = (
        ffmpeg
        .input(in_filename)
        .filter('select', 'gte(n,{})'.format(frame_num))
        .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
        .run(capture_stdout=True,quiet=True)
    )
    file_jpgdata = BytesIO(out)
    frame = Image.open(file_jpgdata)
    return frame

def save_img(item,target_raw_path):
    source = item.source
    time = item.timestamp
    frame = get_frame_as_jpeg(source,time)
    save_to_path = target_raw_path[:-4] +'/images/'+item.identifier+'.jpg'
    return_frame = frame
    frame.save(save_to_path)
    return return_frame

def save_label(item,target_raw_path):
    save_to_path = target_raw_path[:-4] +'/labels/'+item.identifier+'.txt'
    current_file = open(save_to_path,"w")
    for region in item.region_list:
        tag = str(region.tag).replace(' ','')
        left = round(region.x, 3)
        top = round(region.y, 3)
        right = round(left + region.width, 3)
        bottom = round(top + region.height, 3)

        current_line = tag + ' 0.00 0 0 ' + str(left) + ' ' + str(top) + ' ' + str(right) + ' ' + str(bottom) + ' 0 0 0 0 0 0 0'
        current_file.write(current_line+'\n')
    current_file.close()


def main(asset_list,target_raw_path):
    os.system('mkdir ' + target_raw_path[:-4] + '/categories')
    i=1
    list_length = len(asset_list)
    for item in asset_list:
        img_obj = save_img(item,target_raw_path)
        save_label(item,target_raw_path)
        print("Running... " + str(i) +'/'+str(list_length))
        sys.stdout.write("\033[F") # Cursor up one line
        i+=1

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