from re import A

from cv2 import sort


def sortstr(str):
    char = list(str)
    char.sort()
    print(char)    
sortstr("vedant")        
