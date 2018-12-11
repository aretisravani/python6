s=raw_input()
s=list(s)
for a in range(0,len(s)-1,2):
    s[a],s[a+1]=s[a+1],s[a]
print "".join(s)
