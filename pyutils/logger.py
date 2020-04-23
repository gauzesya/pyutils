# -*- coding: utf-8 -*-

class logger:

    def __init__(self, log_filename):
        self._f = open(log_filename, 'w')

    def __del__(self):
        self._f.close()

    def __call__(self, log, end='\n'):
        print(log, end=end)
        self._f.write(str(log)+end)


if __name__=='__main__':
    printl = logger('test.txt')
    printl('test')
    printl([1,2,3])

