# -*- coding: utf-8 -*-
import sys
import os.path


def open_file(file_name):
    if os.path.isfile(file_name):
        try:
            file = open(file_name, encoding='utf-8')
            file.close()
        except IOError:
            return False
        return True
    else:
        return False


if __name__ == '__main__':
    sys.path.append('..')
    from src.startwindow import StartWindow
    path = '../verbs.txt'
    check = open_file(path)
    if check is True:
        with open(path, encoding='utf-8') as fin:
            strokes = fin.readlines()
        lines = [line.strip() for line in strokes]
        fin.close()
        app = StartWindow(lines)
        app.mainloop()
    else:
        print('Файл не открыт. Завершена работа программы.')
