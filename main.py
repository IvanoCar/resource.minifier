from bs4 import BeautifulSoup
import os
import requests
import shutil

from scripts.utils import make_dir
from scripts.hparser import HTMLparser
# from unifier import Unifier
# from minifier import Minifier

'''
TODO:
- make command line app
'''


root = os.path.dirname(__file__)
ORESOURCES = os.path.abspath(os.path.join(root, '_resources'))
ROOT_CSS = os.path.abspath(os.path.join(ORESOURCES, 'css'))
ROOT_JS = os.path.abspath(os.path.join(ORESOURCES, 'js'))

make_dir(ORESOURCES)
make_dir(ROOT_CSS)
make_dir(ROOT_JS)


HTMLparser.parse_and_extract('index.html',root, ROOT_CSS, ROOT_JS)


# Unifier().all_files_in_folder("_resources/css", 'css', minify=True)
# r = Minfier().minify_from_file('index.html', 'html')
# with open('_index.html', 'w', encoding='utf-8') as f:
#     f.write(r)
