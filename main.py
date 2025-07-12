from file_lock import file_lock
from time import sleep


@file_lock
def print_file(filepath, mode='r', file=None):
    print(file.read())
    sleep(20)


def app():

    print_file('test.txt')


if __name__ == '__main__':
    app()
