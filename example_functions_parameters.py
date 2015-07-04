#!/usr/bin/env python

def fun1(*args, **kwargs):
    print len(args)
    print args
    print len(kwargs)
    print kwargs
    args[0][0]=5
    return args[0]

def main():
    x = [1,3,4]
    y = fun1(x,a =1,b=2,c=4)
    print y
if __name__ == '__main__':
    main()

