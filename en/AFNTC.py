import os

def add_folder_name_to_contents(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    
    if not os.path.isdir(folder_path):
        print(f"The path '{folder_path}' is not a directory.")
        return
    
    folder_name = os.path.basename(folder_path)
    contents = os.listdir(folder_path)
    
    for i, item in enumerate(contents):
        old_item_path = os.path.join(folder_path, item)
        if os.path.isfile(old_item_path):
            file_name, file_extension = os.path.splitext(item)
            new_item_name = f"{folder_name}_{i}_{file_name}_{file_extension}"
        else:
            new_item_name = f"{folder_name}_{i}_{file_name}"
        
        new_item_path = os.path.join(folder_path, new_item_name)
        os.rename(old_item_path, new_item_path)
        print(f"Renamed '{old_item_path}' to '{new_item_path}'")