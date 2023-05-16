import numpy as np

# implement the function strange pattern

def strange_pattern(tup):
    array = np.arange(tup[0]*tup[1]).reshape(tup[0], tup[1])
    mask =  array%3 == 0
    return mask

if __name__ == "__main__":
    # use this for your own testing!
    pass

   # strange_pattern(8,8)
