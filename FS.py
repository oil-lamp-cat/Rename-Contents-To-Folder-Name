import os

def find_subfolders(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return []
    
    if not os.path.isdir(folder_path):
        print(f"The path '{folder_path}' is not a directory.")
        return []
    
    subfolders = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            subfolders.append(item_path)
    
    return subfolders

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    subfolders = find_subfolders(folder_path)
    print("Subfolders found:")
    for subfolder in subfolders:
        print(subfolder)
