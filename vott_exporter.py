import os,sys
import file_handler,json_handler

targetFolderPath,targetRawPath,targetVottPath = file_handler.getFolderPath(sys.argv[1])
raw_videos = file_handler.getFolderContentPaths(targetRawPath)
raw_objects = file_handler.getJSONFilePaths(targetVottPath)

print(json_handler.returnJSON(raw_objects[0]))