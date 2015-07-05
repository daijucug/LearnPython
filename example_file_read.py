#!/usr/bin/env python
import numpy as np
_DEBUG=True
def load_file( file_name="" ):
    fid = open( file_name , "r") # using "w" to create
    result = []
    result_lists = []
    for line in fid.readlines():
        nums = line.split(" ")
        for num in nums:
            result.append( int(num) )
        result_lists.append( list(map(int, line.split(" "))))
    fid.close()
    return result, result_lists

def main():
    file_name = "number.txt"
    result, result_lists = load_file(file_name)
    print result
    print result_lists

if __name__ == "__main__":
    import pdb
    pdb.set_trace()
    main()


