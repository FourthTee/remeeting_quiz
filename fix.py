
from functools import reduce
import time

def function(data):
    ss, s, n = reduce(lambda a, b: map(sum, zip(a,b)), [(x*x, x, 1) for x in data])
    return (ss - s*s/n) / n

# This is the new improved function
def function2(data):
    ss = 0
    s = 0
    n = 0
    for i in data:
        ss += i*i
        s += i
        n += 1
    return (ss - s*s/n) / n


#Testing if the runtime for fucntion 2 is better than function 1
a = [1, 2, 3, 6, 5, 34, 5, 6, -1, 18, 19]
start = time.time()
f1 = function(a)
end = time.time()
print("f1 runtime:" + str(end - start))
start = time.time()
f2 = function2(a)
end = time.time()
print("f2 runtime:" + str(end - start))
