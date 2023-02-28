import os
from zipfile import ZipFile
from pathlib import Path

__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

""" clean_cache: takes no arguments and creates an empty folder named cache in the current directory. 
If it already exists, it deletes everything in the cache folder. """
def clean_cache():
    dirname = "\\files\\cache"
    cachedirname = "cache"
    path = Path(os.getcwd()+dirname)
    list_dir = os.listdir(path.parent)
    #print(list_dir)
    if cachedirname not in list_dir:
        os.mkdir(path)
    else:
        for file_name in os.listdir(path):
            file = str(path)+"\\"+ file_name
            if os.path.isfile(file):
                #print('Deleting file:', file)
                os.remove(file) 

#clean_cache()

""" cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments, 
in that order. The function then unpacks the indicated zip file into a clean cache folder.
You can test this with data.zip file. """
def cache_zip (zipfile_path, cache_dir_path):
    clean_cache()
    for file_name in os.listdir(cache_dir_path):
        file = cache_dir_path+"\\"+ file_name
        #print("test de file: " + file)
        if os.path.isfile(file):
            #print('Deleting file:', file)
            os.remove(file) 
    
    with ZipFile(zipfile_path,'r') as f:
        f.extractall(cache_dir_path)

#clean_cache()
# print(os.getcwd()+"\\files\\"+"data.zip")
#cache_zip(os.getcwd() + "\\files\\data.zip",os.getcwd()+"\\files\\cache\\")

""" cached_files: takes no arguments and returns a list of all the files in the cache. 
The file paths should be specified in absolute terms. Search the web for what this means! 
No folders should be included in the list. You do not have to account for files within folders within the cache directory. """
def cached_files():
    dirname = "files\\cache"
    path = os.getcwd()+"\\"+dirname
    files = [os.getcwd()+"\\"+dirname+"\\"+f for f in os.listdir(path) if os.path.isfile(path+"\\"+f) ]
    return files

#print(cached_files())

""" find_password: takes the list of file paths from cached_files as an argument. 
This function should read the text in each one to see if the password is in there. 
Surely there should be a word in there to indicate the presence of the password? 
Once found, find_password should return this password string. """
def find_password(cached_files = cached_files()):
    for filepath in cached_files:
        with open(filepath, 'r') as file:
            content = file.read()
            if "password" in content: #601.txt
                #break
                splittext = content.split('\n')
                for text in splittext:
                    if "password" in text:
                        text_with_password = text
                        break
                break
    splittext = text_with_password.split(' ')
    password = splittext[len(splittext)-1]
    return password


#print(find_password())
