import subprocess
import os, glob
print("***************Welcome to Vision Computers Auto-Setup Wizard******************")

for file in glob.glob("src/*"):
    file_name=file.strip('src')
    if file!='zzzzz.txt':
        print ("Installing.....",file_name)
        subprocess.call([file], shell=True)
        print ("Installed {} \n............................\n".format(file_name))
print("All Software Insatlled Sucessfully")
exit()
    
