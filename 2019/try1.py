from FileHelper import Loader
import numpy as np

e = Loader("a_example.txt")

print(e.photos[:,1])
print(e.photos[1])
#max(elements, key=lambda e: int(e[0]))