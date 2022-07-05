import os

path = r'C:\Users\malysheve\Desktop\Python_lesson_7'
projectname = 'my_project'
folders = \
    [['settings', []],
     ['mainapp', []],
     ['adminapp', []],
     ['authapp', []]
     ]


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def build(root, data):
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            create_folder(path)
            build(path, d[1])


fullPath = os.path.join(path, projectname)
create_folder(fullPath)


build(fullPath, folders)
