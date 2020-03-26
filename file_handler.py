import sys,os

def getFolderPath(folder_name):
    dirpath = os.getcwd()
    dirpath += '/' + str(folder_name)

    try:
        os.listdir(dirpath)
        assert verifyProjectFolder(dirpath) == True,'Given folder is not a valid Project Folder'
        assert verifyTrainFolder(dirpath+'/train') == True,'Given folder is not a valid Project Folder'
        raw_path = dirpath + '/train/raw'
        vott_path = dirpath + '/vott'
        return dirpath,raw_path,vott_path
    except:
        raise ValueError('The Specified Folder does not exist')

def getFolderContents(folder_path):
    return os.listdir(folder_path)

def getFolderContentPaths(folder_path):
    items = os.listdir(folder_path)
    return_list = []
    for item in items:
        item = folder_path + '/' + item
        return_list.append(item)
    return return_list

def verifyProjectFolder(folder_path):
    contents = os.listdir(folder_path)
    assert 'train' in contents, "Specified folder is not a valid Project Folder. Does not contain training folder."
    assert 'val' in contents, "Specified folder is not a valid Project Folder. Does not contain validation folder"
    assert 'vott' in contents, "Specified folder is not a valid Project Folder. Does not contain vott folder"
    return True
    
def verifyTrainFolder(folder_path):
    contents = os.listdir(folder_path)
    assert 'images' in contents, "Specified folder is not a valid Train Folder. Does not contain images folder."
    assert 'labels' in contents, "Specified folder is not a valid Train Folder. Does not contain labels folder"
    assert 'raw' in contents, "Specified folder is not a valid Train Folder. Does not contain raw folder"
    return True