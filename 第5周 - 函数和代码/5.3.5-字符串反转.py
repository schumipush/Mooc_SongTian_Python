#将字符串s反转后输出 
#s[::-1] #索引字符、切片[M:N:K](从第M位开始，到N位前取切片，K是步长，如果是负数则实现逆序)

def reverse(s):
    if s=='':
        return s
    else:
        return reverse(s[1:]) + s[0]
print(reverse('abcd'))