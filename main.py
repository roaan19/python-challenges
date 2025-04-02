#operator residence
a=19
l=18

result=l**2+a/l+a*2
print(result)

#divisible number 
m=10
r=2

if m%r==0:
    print("m is divisible by r ")
else:
    print("m is not divisible by r ")

#correct mean
mean1=28
wrongnumber = 19
correctnumber=20
totalnumbers=40
sum=mean1*totalnumbers
print("the incorrect sum is ", sum)

sum2=sum-wrongnumber+correctnumber
print("the sum is ",sum2)

mean2=sum2/totalnumbers
print("the correct mean is ",mean2)

#average speed 
s1=int(input("enter the speed1"))
s2=int(input("enter the speed2"))
s3=int(input("enter the speed3"))

average=(s1+s2+s3)/3

if s1<average:
    print("speed1 is slower than average with the difference of ",average - s1)
if s2<average:
    print("speed2 is slower than average with the difference of ",average - s2)
if s3<average:
    print("speed3 is slower than average with the difference of ",average - s3)
