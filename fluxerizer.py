import random

src = "train/hybrid.txt"
dst = "train/hybrid_shuffled.txt"
lines = open(src).readlines()
random.shuffle(lines)
open(dst,'w').writelines(lines)