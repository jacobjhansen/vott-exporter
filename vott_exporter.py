import os,sys
import file_handler,json_handler,export_handler

targetFolderPath,targetRawPath,targetVottPath = file_handler.getFolderPath(sys.argv[1])

# List of Video Paths
raw_videos = file_handler.getFolderContentPaths(targetRawPath)

# List of JSON File Paths
raw_objects = file_handler.getJSONFilePaths(targetVottPath)

# List of Asset Objects
asset_list = json_handler.return_asset_list(raw_objects,raw_videos)

export_handler.main(asset_list,targetRawPath)