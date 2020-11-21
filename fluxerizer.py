import random

src = "train/new_hybrid_shuffled.txt"
dst = "train/new_hybrid_shuffled.txt"
lines = open(src, encoding="utf-8").readlines()
lines_cut = []
#use for deleting short lines, 0 to ignore
for l in lines:
    if (len(l) > 0):
        lines_cut.append(l)
random.shuffle(lines_cut)
open(dst,'w').writelines(lines_cut)