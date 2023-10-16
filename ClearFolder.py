
import os
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(FILE_PATH)
import os
import glob
import time

EXCLUDE_LIST = ['.md', '.py', '.lnk']
TARGET_PATH_LIST = ['input','output',]



def clear_folder(target_folder, excluded_list=EXCLUDE_LIST):
    print('Clear folder:', target_folder)


    target_path = target_folder
    if os.path.isdir(target_path):
        target_path = os.path.join(target_path, '*')

    for x in glob.glob(target_path):
        base_name = os.path.basename(x)
        file_name, file_type = os.path.splitext(base_name)
        if file_type in excluded_list:
            continue

        if os.path.isdir(x):
            continue
            # shutil.rmtree(x)
        else:
            print('Remove:', base_name)
            os.remove(x)

def save_clear_folder(target_folder):
    target_folder = os.path.abspath(target_folder)
    base_dir = os.path.dirname(target_folder)
    base_name = os.path.basename(target_folder)
    
    if (os.path.exists(os.path.join(target_folder,'SAFE_LOCK'))) or (os.path.exists(os.path.join(target_folder,'safe_lock'))):
        print("Stop: safe lock found.")
        return False
    
    
    if base_name in TARGET_PATH_LIST:
        clear_folder(target_folder)
    else:
        print('Error: target_folder should be input or output folder.')
        return False
    # clear_folder(target_folder)

    return True


if __name__ == '__main__':
    print('\n')
    target_folder = FILE_PATH
    save_clear_folder(target_folder)
    print('\n')
    print('Done!')
    time.sleep(5)
