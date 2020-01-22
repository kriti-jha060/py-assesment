
ASSESSMENT 1 IN PYTHON :


1)
name="kriti jha"
name1=name[::-1]
print(name1)


2)
str1 = "AccENtUre"
str2=str1.swapcase()
print(str2)


3)

word="accenture"
newdic={}
for i in word:
    newdic[i]=0
    for j in word:
        if i==j:
            newdic[i]=newdic.get(i)+1 
print(newdic)            

4)
print("List of generated numbers:")
for i in range(1,51):
    print(i)
print("list of even numbers:")
for i in range(1,51):
    if i %2  == 0:
        print(i)
print("list of odd numbers")      
for i in range(1,51):
    if i%2 != 0:
        print(i)


5)

for i in range(1,51):
    if i%3 ==0 and i%5 == 0:
        print(i, "fizz-buzz")
    elif i %3 == 0: 
        print(i , "fizz")
    elif i % 5 == 0:
        print(i , "buzz")

    else: 
        print(i)


6)

word="accenture"
c1=0
c2=0
c3=0
for x in word:
    if x=='a':
        c1=c1+1
    elif x=='e':
        c2=c2+1
    elif x=='u':
        c3=c3+1
        
print(c1,"a",c2,"e",c3,"u")


7)
a="ga24nbv2k6jg523jg2545lsfwe"
dig="1234567890"
count1=0
count2=0 
for i in a:
    if i in dig:
        count1=count1+1 
    else:
        count2=count2+1 
        
print("total digit ", count1)
print("total characters ", count2)

8)

number = []
for i in range(1,11):
    number.append(i)
print(number)
n = len(number)
sum = 9
for i in range(0,n):
    for j in range(0,n):
        if(number[i]+number[j] == sum):
            print(number[i]," ", number[j])


9)

print("enter two words to check for anagram")
word1 = input()
word2 = input()
if(sorted(word1)==sorted(word2)):
    print(word1," ",word2 ," are  anagram" )
else:
    print("the words are not  anagram")


10)

print("enter a number")
a=int(input())
x=0
for i in range(2,int(a-1)):
    if a%i == 0:
        print("it is not a prime number")
        x=1 
        break
else:
    print("it is a prime number")
l1=[]
if x==1:
    for j in range(2,int(a-1)):
        if a%j==0:
            l1.append(j)
    print("prime divisors of ",a)

    for y in l1:
        for j in range (2, int (y)):
            if y%j==0:
                break
        else:
            print(y)

    


11)

tup = (1,2,3,4,5)
L = list(tup)
L.append("a")
print(tuple(L))

12)

str1 = input()
str2 = str1[::-1]
if str1==str2:
    print("the string is pallindrome")
else:
    print("the string is not pallindrome")


13)

print("enter the number for multiplication table")
a= int(input())
print("multiplication table of ", a)
for i in range(1,11):
    print(a," x ",i ,"= ",a*i)

14)
print("fibonacci series till 50 :")
a =0
b =1 
c =0
while(c<50):
    print(c)
    c = a +b
    a = b
    b = c 

15)

sortsen= []
str1= "green-red-yellow-black-white"
sen=str1.split("-")
print(sen)
for i in sen:
    sortsen.append(i)
sortsen.sort()
print('-'.join(sortsen))

16)

L1 = [1,2,3,3,3,3,4,5]
L2 = []
for i in L1:
    if i not in L2:
        L2.append(i)
        
print(L2) 


17)

characters = "abcdefghijklmnopqrstuvwxyz"
word = "The quick brown fox jumps over the lazy dog"
for c in characters:
    if c not in word:
        print("it is not a pangram")
        break;
else: 
    print("it is a pangram")


18)

print("enter 5 integers")

num=[]
for i in range(0,5):
    new=int(input())
    num.append(new)
    max=0
    if (new%2 !=0) and (new > max):
        max=new

if max ==0:
    print("no odd number was entered")
else:
    print("largest odd integer is" , max)



19)

rad = int(input("Enter the radius in integer :"))
area = 3.14*rad*rad
print(area)  

20)

print("enter a number to find it's factorial :")
a=int(input())
fact=1

for i in range (1,a+1):
    fact =i*fact
    
print("factorial of",a ,"is" , fact)
