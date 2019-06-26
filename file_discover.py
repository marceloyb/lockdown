import os

def discover(path):

    extensions = [
        # '.c', '.cpp', '.java', '.py', #codigo fonte
        # '.jpg', '.jpeg', '.png', '.bmp', '.gif', #imagens
        # '.txt', '.doc', '.docx', '.pdf', #texto
    ]

    for dirpath, dirs, files in os.walk(path):
        for i in files:
            file_path = os.path.abspath(os.path.join(dirpath, i))
            filename, file_extension = os.path.splitext(file_path)
            if file_extension in extensions:
                yield file_path