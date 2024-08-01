#for(int i=0 ; i<3 ; i++)

for i in range(3): 
    print(i)

#for(int i=2 ; i<6 ; i++)
for i in range(2,6): 
    print(i)

#for(int i =5; i>1 ; i--)
for i in range(5,1, -1): 
    print(i)

#Division is decimal by default 
print(5/2)

#Double slash rounds down
print(5//2)

print(-3 // 2)

#modding is similar to most languages
print(10 % 3)
#answer : 1


#except for negeative values
print(-10 % 3)
#answer : 2

#to be consistent with other languages modulo 
import math 
print(math.fmod(-10,3))
#answer : -1.0

#more math helpers
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))

#max / min Int 

float("inf")
float("-inf")

#Arrays (called lists in python)

arr = [1, 2, 3]
print(arr)

#can be used as a stack

#pushing
arr.append(4)
arr.append(5)
print(arr)

#popping 
arr.pop()
print(arr)

#also can be used as array too 
arr.insert(1, 7)
print(arr)

arr[0] = 0 

#careFul: -1 is nout out of bounds, 
#it's the last value

print(arr[-1])

#slicing arrays 

arr = [1,2,3,4]
print(arr[1:3])

#Unpacking 

a , b , c = [1, 2, 3]

#loop through arrays
nums = [1,2,3]

#using index

for i in range(len(nums)): 
    print(nums[i])

#without index 

for n in nums: 
    print(n)

#with index and value
for i, n in enumerate(nums): 
    print(i,n)

#loop through multiple arrays simulatneously 
#with unpacking

nums1 = [1,2,3]
for n1,n2 in zip(nums1,nums2): 
    print(n1,n2)

#reverse an arrya 

nums = [1,2,3]
nums.reverse()
print(nums)

#sorting

arr = [3,4,5,1,3,12,4,5,7]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)


arr.sort(reverse=False)









