import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
   
    if isinstance(loc, scale, lower_bound, upper_bound, (int, float)):
        if lower_bound <= upper_bound:
            array = np.random.normal(loc, scale, size=100)
            for element in array:
                if (element <=upper_bound) & (element>=lower_bound):
                    array=np.array(element)
                    mean=np.mean(array)
                    std = np.std(array)
                else:
                    pass
        else:
            print("input is invalid pleat check the valuse")
        return ((mean, std))   
        
    else:
        print("input is invalid")


        
if __name__ == "__main__":
        pass
    # use this for your own testing!

   # print(gaussian_analysis(0, 3, 1, 3))
    
    
