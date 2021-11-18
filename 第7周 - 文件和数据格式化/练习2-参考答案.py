f = open("latex.log")
cc = 0
d = {}
for i in range(26):
    d[chr(ord('a')+i)] = 0
for line in f:
    for c in line:
        d[c] = d.get(c, 0) + 1
        cc += 1
print("共{}字符".format(cc), end="")
for i in range(26):
    if d[chr(ord('a')+i)] != 0:
        print(",{}:{}".format(chr(ord('a')+i), d[chr(ord('a')+i)]), end="")

'''
输出：
共244019字符,a:9620,b:525,c:8769,d:1046,e:15585,f:8653,g:4548,h:8882,i:17587,j:62,k:122,l:9090,m:736,n:25730,o:13812,p:961,q:132,r:13755,s:12948,t:14049,u:4850,v:294,w:427,x:276,y:359,z:4
'''