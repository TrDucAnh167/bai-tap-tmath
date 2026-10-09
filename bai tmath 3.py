a,b,c,d,e = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
s1 = a+b+c+d
s2 = b+c+d+e
s3 = a+c+d+e
s4 = b+d+e+a
s5 = a+b+c+e
if s1<s2 and s1<s3 and s1<s4 and s1<s5:
    print(s1)
if s2<s1 and s2<s3 and s2<s4 and s2<s5:
    print(s2)
if s3<s1 and s3<s2 and s3<s4 and s3<s5:
    print(s3)
if s4<s1 and s4<s3 and s4<s2 and s4<s5:
    print(s4)
if s5<s1 and s5<s3 and s5<s2 and s5<s4:
    print(s5)
if s1>s2 and s1>s3 and s1>s4 and s1>s5:
    print(s1)
if s2>s1 and s2>s3 and s2>s4 and s2>s5:
    print(s2)
if s3>s1 and s3>s2 and s3>s4 and s3>s5:
    print(s3)
if s4>s1 and s4>s3 and s4>s2 and s4>s5:
    print(s4)
if s5>s1 and s5>s3 and s5>s2 and s5>s4:
    print(s5)




    
