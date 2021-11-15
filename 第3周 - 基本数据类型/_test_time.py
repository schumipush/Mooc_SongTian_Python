import time
a  = time.perf_counter()
a1 = time.time()
b  = time.perf_counter()
for ii in range(10):
    c  = time.time()
b1 = time.time()
print(b-a,b1-a1,"\n"
,a,b,'\n'
,a1,b1)