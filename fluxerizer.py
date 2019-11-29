import random

src = "train/hybrid_shuffled_monolithic.txt"
dst = "train/hybrid_shuffled_monolithic.txt"
lines = open(src).readlines()
random.shuffle(lines)
open(dst,'w').writelines(lines)