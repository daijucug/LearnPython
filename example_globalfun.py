#!/usr/bin/env python

import numpy as np

class T1:
    ''' this is an test class for global funs '''
    def __init__(self):
        pass
    def call(self):
        hello()

def hello():
    print "hello world"

if __name__ == '__main__':
    t = T1()
    t.call()
