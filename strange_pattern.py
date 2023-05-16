import numpy as np

# implement the function strange pattern

def strange_pattern():
    array = np.arange(width*hight).reshape(hight, width)
    mask =  array%3 == 0 
    return mask
    


if __name__ == "__main__":
    # use this for your own testing!

    pass
