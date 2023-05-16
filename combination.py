import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array_one, array_two, axiss=0):
    array_one = np.squeeze(array_one)
    array_two = np.squeeze(array_two)
    a1 = array_one.ndim
    a2 = array_two.ndim
    if a1 == a2: 
        return (np.concatenate((array_one,array_two),axis=axiss))
    else:
        return ("No")


if __name__ == "__main__":
    # use this for your own testing!
    #combination([1,2],[3,4],0)
    pass

