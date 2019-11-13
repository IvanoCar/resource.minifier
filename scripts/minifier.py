import requests

class Minfier:

    def __init__(self):
        self.html_minifier = 'https://html-minifier.com/raw'
        self.css_minifier = 'https://cssminifier.com/raw'
        self.js_minifier = 'https://javascript-minifier.com/raw'


    def minify_from_file(self, file, type):
        type = type.lower()

        if type not in ['js', 'css', 'html']:
            return

        data = {'input': open(file, 'rb').read()}

        if type == 'html':
            url = self.html_minifier
        elif type == 'css':
            url = self.css_minifier
        else:
            url = self.js_minifier           
            
        response = requests.post(url, data=data).text.replace('\n', '')

        return response

    def minify(self, raw, type):
        type = type.lower()

        if not type in ['js', 'css', 'html']:
            return

        data = {'input': raw}

        if type == 'html':
            url = self.html_minifier
        elif type == 'css':
            url = self.css_minifier
        else:
            url = self.js_minifier           
            
        response = requests.post(url, data=data).text.replace('\n', '')

        return response
