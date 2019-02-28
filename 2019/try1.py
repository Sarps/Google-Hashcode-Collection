from FileHelper import Loader
import numpy as np

e = Loader("a_example.txt")
#e = Loader("e_shiny_selfies.txt")
# e = Loader("b_lovely_landscapes.txt")
# e = Loader("d_pet_pictures.txt")


metas, photos = [], []

for x in e.photos:
    if x[0] == 'H':
        horizontal = 0
    else:
        horizontal = 1
    metas.append([horizontal, x[1]])
    photos.append(x[2])
photos = np.array(photos)
metas = np.array(metas, dtype=int)

print('maximum tags', max(metas[:,1]))
#print(photos)
#print(metas)
#print(e.photos[1])
#max(elements, key=lambda e: int(e[0]))