import os
import shutil
source = "C:/Users/akshajaryash/Downloads"
destination1 = "C:/Users/akshajaryash/Desktop/Downloads_Image Files"
destination2 = "C:/Users/akshajaryash/Desktop/Downloads_Document Files"
destination3 = "C:/Users/akshajaryash/Desktop/Downloads_Other stuff"
list_of_files = os.listdir(source)
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    
    if extension == "":
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = source + '/' + file_name
        path2 = destination1 + '/' + "image_folder"
        path3 = destination1 + '/' + "image_folder" + '/' + file_name
        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2) 
            shutil.move(path1, path3)
    elif extension in ['.doc','.docx','.odt','.odp','.ppt','.pptx','.xlsx','.pdf']:
        path4 = source + '/' + file_name
        path5 = destination2 + '/' + "document_folder"
        path6 = destination2 + '/' + "document_folder" + '/' + file_name
        if os.path.exists(path5):
            shutil.move(path4, path6)
        else:
            os.makedirs(path5) 
            shutil.move(path4, path6)
    elif extension in ['.sldprt','.rtf','.ics','.exe','.txt','.sprite3','.zip','.mpp','.mp3','.mp4','.stl','.avi','.webm','.py','.json','.crdownload','.html','.dxf','.pub']:
        path7 = source + '/' + file_name
        path8 = destination3 + '/' + "other_stuff_folder"
        path9 = destination3 + '/' + "other_stuff_folder" + '/' + file_name
        if os.path.exists(path8):
            shutil.move(path7, path9)
        else:
            os.makedirs(path8) 
            shutil.move(path7, path9)

