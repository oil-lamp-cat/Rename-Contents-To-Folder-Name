import os
from FS import find_subfolders as fs
from RCTFN import rename_contents_to_folder_name as rctfn

print(""" 
.----------------.  .----------------.  .----------------.  .----------------.  .-----------------.  
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| |  _______     | || |     ______   | || |  _________   | || |  _________   | || | ____  _____  | |  
| | |_   __ \    | || |   .' ___  |  | || | |  _   _  |  | || | |_   ___  |  | || ||_   \|_   _| | |  
| |   | |__) |   | || |  / .'   \_|  | || | |_/ | | \_|  | || |   | |_  \_|  | || |  |   \ | |   | |  
| |   |  __ /    | || |  | |         | || |     | |      | || |   |  _|      | || |  | |\ \| |   | |  
| |  _| |  \ \_  | || |  \ `.___.'\  | || |    _| |_     | || |  _| |_       | || | _| |_\   |_  | |  
| | |____| |___| | || |   `._____.'  | || |   |_____|    | || | |_____|      | || ||_____|\____| | |  
| |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
'----------------'  '----------------'  '----------------'  '----------------'  '----------------'   
""")

print("1. multiple folders in a folder\n2. files in the folder")

num=int(input('RCTFN@main > '))

if (num == 1):
    subfolders = []
    folder_path = input("Enter the folder path: ")
    subfolders = fs(folder_path)
    for subfolder in subfolders:
        print(subfolder)
        rctfn(subfolder)
    
elif (num == 2):
    folder_path = input("Enter the folder path: ")
    rctfn(folder_path)
else:
    print("wrong input.")


os.system("pause")