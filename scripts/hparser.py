import os
import requests
from bs4 import BeautifulSoup


class HTMLparser:

    @staticmethod
    def parse_and_extract(html_file, root, ROOT_CSS, ROOT_JS):
        with open(html_file, 'rb') as f:
            html = BeautifulSoup(f.read().decode('utf-8'), 'html.parser')
            styles = html.find_all('link', {'rel':'stylesheet'})
            scripts = html.find_all('script')
        
        for c, style in enumerate(styles):
            link = style['href']

            if 'http' in link:
                fname = '%s REMOTE - %s' %  (c + 1, link.split('/')[-1])
                with open(os.path.join(ROOT_CSS, fname), 'w') as f:
                    data = requests.get(link).text
                    f.write(data)
            else:
                with open(os.path.join(root, link), 'r') as f:
                    data = f.read()
                fname = '%s LOCAL- %s' %  (c + 1, link.split('/')[-1])
                with open(os.path.join(ROOT_CSS, fname), 'w') as f:
                    f.write(data)
        

        for c, script in enumerate(scripts):
            link = script['src']

            if 'http' in link:
                fname = '%s REMOTE - %s' %  (c + 1, link.split('/')[-1])
                with open(os.path.join(ROOT_JS, fname), 'w') as f:
                    data = requests.get(link).text
                    f.write(data)
            else:
                with open(os.path.join(root, link), 'r') as f:
                    data = f.read()
                fname = '%s LOCAL- %s' %  (c + 1, link.split('/')[-1])
                with open(os.path.join(ROOT_JS, fname), 'w') as f:
                    f.write(data)
