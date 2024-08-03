import os
from FS import find_subfolders as fs
from RCTFN import rename_contents_to_folder_name as rctfn
from AFNTC import add_folder_name_to_contents as afntc

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

print("\n1. 폴더 안에 여러 폴더\n2. 폴더 안에 파일\n3. 폴더 안에 여러 폴더 이름 추가")

num=int(input('\nRCTFN@main > '))

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
elif ( num == 3):
    subfolders = []
    folder_path = input("Enter the folder path: ")
    subfolders = fs(folder_path)
    for subfolder in subfolders:
        print(subfolder)
        afntc(subfolder)
else:
    print("잘못된 입력입니다.")


os.system("pause")