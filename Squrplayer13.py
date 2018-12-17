num=int(raw_input())
total=0
while(num!=0):
	temp=num%10
	total=total+(temp*temp)
	num=num//10
print  total
