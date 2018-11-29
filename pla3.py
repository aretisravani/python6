x=int(raw_input())
a=0
sum=0
y=x
while(x!=0):
	a=x%10
	sum=sum*10+a
	x=x/10
print sum	
