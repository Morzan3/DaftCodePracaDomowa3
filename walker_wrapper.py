from file_walker import my_directory_walker_with_size_counting
import os

folder_info = None
folder_info = my_directory_walker_with_size_counting(os.path.dirname(__file__) + "/test dir")
new_folder_info = {}
for key, value in folder_info.items():
    new_folder_info[key.replace(os.path.dirname(__file__), "")] = value

def get_main_folder_size(folder_name):
    if folder_name[0] != "/":
        folder_name = "/" + folder_name
    if folder_name in new_folder_info:
        return new_folder_info[folder_name]

def get_parent(folder_name):
    absolute_parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__) +  "/{}".format(folder_name), os.pardir))
    parent_folder = absolute_parent_path.replace(os.path.dirname(__file__), "")
    return parent_folder

def get_children(folder_name):
    if folder_name[0] != "/":
        folder_name = "/" + folder_name
    children_files = {}
    children_folders = {}

    for key, value in new_folder_info.items():
        if key.startswith(folder_name) and key != folder_name:
            if os.path.isfile(os.path.dirname(__file__) + key):
                children_files[key[1:]] = value
            elif os.path.isdir(os.path.dirname(__file__) + key):
                children_folders[key[1:]] = value

    return children_files, children_folders

def check_if_exists(folder_name):
    if folder_name[0] != "/":
        folder_name = "/" + folder_name
    if folder_name not in new_folder_info:
        return False
    return True