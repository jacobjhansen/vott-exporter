import PIL
from PIL import Image
from cv2 import cv2
import ffmpeg
from io import BytesIO
import sys,os
import subprocess

def save_img(item,target_raw_path):
    source = item.source
    file_name = source.split('/')[-1][:-4]
    time = int(item.timestamp)
    time += 1 #Account for 1 based indexing on output, vs 0 based indexing on assets
    image_source = target_raw_path+'/'+file_name+'t='+str(time)+'.png'
    frame = Image.open(image_source)
    try:
        save_categories(item,frame,target_raw_path)
    except:
        pass
    save_to_path = target_raw_path[:-4] +'/images/'+item.identifier+'.jpg'
    frame.save(save_to_path)
    pass

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

def batch_frame_export(target_raw_path):
    command = 'ffmpeg -i '+target_raw_path+' -vf fps=1 '+target_raw_path[:-4]+ 't=%d.png'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.returncode)

def save_categories(item,frame,target_raw_path):
    f1or region in item.region_list:
        save_string = target_raw_path[:-4] + '/categories/' + str(region.tag) +'/'+region.identifier+'.jpeg'
        imcrop = frame
        rectbox = (region.x,region.y,region.x+region.width,region.y+region.height)
        croppedimg = imcrop.crop(rectbox)
        croppedimg.save(save_string)
    
def garbage_collector(target_raw_path):
    filelist = [ f for f in os.listdir(target_raw_path) if f.endswith(".png") ]
    for f in filelist:
        os.remove(os.path.join(target_raw_path, f))

def main(asset_list,target_raw_path,raw_videos):
    raw_image_list = []
    os.system('mkdir ' + target_raw_path[:-4] + '/categories')

    tag_list = ['cow','fence-panels', 'building', 'trailer', 'vehicle', 'fences', 'person', 'fence-post','farm-animal','gate', 'grain-auger', 'bale', 'water-tank']

    for item in tag_list:
        os.system('mkdir ' + target_raw_path[:-4] + '/categories/' + item)

    #for video in raw_videos:
        #raw_image_list = batch_frame_export(video)

    i = 1
    list_length = len(asset_list)
    for item in asset_list:
        save_img(item,target_raw_path)
        save_label(item,target_raw_path)
        print("Running... " + str(i) +'/'+str(list_length))
        sys.stdout.write("\033[F") # Cursor up one line
        i+=1
    print("Running garbage collection...")
    garbage_collector(target_raw_path)