import os
import shutil


def walk_folder(dir_path, dist_css, dist_js):
    for root, dirs, files in os.walk(dir_path):   
        if len(files) > 0:
            for file in files:
                root = os.path.abspath(root)
                if file[-4:] == '.css':
                    shutil.copy2(os.path.join(root, file), dist_css)
                elif file[-3:] == '.js':
                    shutil.copy2(os.path.join(root, file), dist_js)
