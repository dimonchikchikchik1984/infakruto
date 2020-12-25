from zipfile import ZipFile
import os
import string
import shutil


class TextLoader(ZipFile):

    def __init__(self, file, path):
        super().__init__(file)
        self.file_in_dir = None
        self.extractall(path)
        self.path = path
        self.path_of_file = path + "\\sample\\"
        self.iter = iter(os.listdir(self.path_of_file))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __len__(self):
        file_count = len(os.listdir(self.path_of_file))
        return file_count

    def __iter__(self):
        return self

    def __del__(self):
        shutil.rmtree(self.path)

    def __next__(self):
        self.file_in_dir = next(self.iter)
        file = self.path_of_file + self.file_in_dir
        a = []
        with open(file, 'r', encoding='utf8') as f:
            for line in f:
                l = line.translate(str.maketrans('', '', string.punctuation))
                l = l.lower()
                a.append(l)

        with open(file, 'w', encoding='utf8') as f:
            f.writelines(a)

        f = open(file, 'r', encoding='utf8')
        return f


if __name__ == "__main__":
    where_from = r'C:/Users/ovsy2/Downloads/sample.zip'
    where_to = r'C:\Users\ovsy2\PycharmProjects\untitled2\lab9\hz'
    text_loader = TextLoader(where_from, where_to)
    print(len(text_loader))
    counter = 0
    for file in text_loader:
        counter += 1
    print(counter)