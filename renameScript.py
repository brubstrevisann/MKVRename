import os
import subprocess
import time

filelist = os.listdir('.')  # get files in current directory
for filename in filelist:
    if "1080" in filename: 
        position = filename.find('1080p')
        newname = filename[0:position] + "mkv"
        print(filename + " >>>>>>>>>>>>> FOI RENOMEADO PARA >>>>>>>>>>" + newname)
        os.rename(filename, newname)
        os.system("wsl mkvpropedit "+newname+" --delete title")
        # os.system("  mkvpropedit "+newname+" --edit info --set "+a+"title="+newname+a+"")
    if "720p" in filename:
        position = filename.find('720p')
        newname = filename[0:position] + "mkv"
        print(filename + ">>>>>>>>>>>>> FOI RENOMEADO PARA >>>>>>>>>> " + newname)
        os.rename(filename, newname)
        os.system("wsl mkvpropedit "+newname+" --delete title")
        # os.system("  mkvpropedit "+newname+" --edit info --set "+a+"title="+newname+a+"")

# subprocess.call(['./rename.sh'])
    

# os.system('sh rename.sh')




