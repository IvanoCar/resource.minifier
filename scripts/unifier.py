from utils import natural_sort
from .minifier import Minfier
import os

class Unifier:
    
    def __init__(self):
        self.allowed_ext = ['js','css']

    def all_files_in_folder(self, dir_path, type, minify=True):
        type = type.lower()
        minifier = Minfier()
        if type not in self.allowed_ext:
            return

        result = ''
        for f in natural_sort(os.listdir(dir_path)):
            with open(os.path.join(dir_path, f), 'r') as s:
                fdata = s.read()
            if minify:
                fdata = minifier.minify(fdata, type)
            result += fdata
        
        with open(os.path.join(dir_path, 'joined.' + type), 'w', encoding='utf-8') as f:
            f.write(result)
    
    def all_file_paths(self, paths, type, minify=True):
        type = type.lower()
        minifier = Minfier()
        if type not in self.allowed_ext:
            return

        current_folder = os.path.abspath(os.path.dirname(os.path(__file__)))

        result = ''
        for f in paths:
            with open(f, 'r') as s:
                fdata = s.read()
            if minify:
                fdata = minifier.minify(fdata, type)
            result += fdata
        
        with open(os.path.join(current_folder, 'joined.' + type), 'w', encoding='utf-8') as f:
            f.write(result)


# Unifier().all_files_in_folder("_resources\css", 'css')
# Unifier().all_files_in_folder("_resources\js", 'js')
    