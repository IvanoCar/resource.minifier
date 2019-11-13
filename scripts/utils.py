import os
import re 


def make_dir(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError:  
            pass


def natural_sort( l ): 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)
