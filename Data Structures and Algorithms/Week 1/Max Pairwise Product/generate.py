import random
import sys

n = int(sys.argv[1])
myseed = int(sys.argv[2])
random.seed(myseed)

print (n)
print(' '.join([str(random.randint(1,1000)) for i in range(n)]))