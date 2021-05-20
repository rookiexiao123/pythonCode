

import os

# 获得路径下的文件夹的所有文件（包括子文件夹）
def get_listfiles(path):
    Filelist = []
    for home, dirs, files in os.walk(path):
        for file in files:
            # 文件名列表，包含完整路径
            Filelist.append(os.path.join(home, file))
            #Filelist.append(file)
    return Filelist
