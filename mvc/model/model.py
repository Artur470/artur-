import os

PATH = 'C:\\Users\\HP\\PycharmProjects\\pythonProjectmuproject\\mvc\\model\\'


def save_data(f_name, data):
    with open(PATH+f_name,  'w') as f:
        f.write(data)

PATH = 'C:\\Users\HP\\PycharmProjects\\pythonProjectmuproject\\mvc\model\\'


def deleyt_file(f_name, data):
    os.remove(PATH+f_name)





