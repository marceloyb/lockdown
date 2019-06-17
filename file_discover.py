import os

def discover(path):

    extensions = [
        'c', 'cpp', 'java', 'py', #codigo fonte
        'jpg', 'jpeg', 'png', 'bmp', 'gif', #imagens
    ]

    for dirpath, dirs, files in os.walk(path):
        for i in files:
            file_path = os.path.abspath(os.path.join(dirpath, i))
            yield file_path
