#checking number odd or even #1

num = int(input("Enter a number: "));
mod = num % 2
if mod > 0:
    print("This is an odd number");
else:
    print("This is an even number");


#finding sum of numbers in an array #2
    
arr = [5, 9, 3, 4, 5];     
sum = 0;    
     
#Loop through the array to calculate sum of elements    
for i in range(0, len(arr)):    
   sum = sum + arr[i];    
     
print("Sum of all the numbers of the array: " + str(sum)); 


#finding largest in an array #3

#Initialize array     
arr = [25, 11, 7, 113, 56];     
         
#Initialize max with first element of array.    
max = arr[0];    
         
#Loop through the array    
for i in range(0, len(arr)):    
    #Compare elements of array with max    
    if(arr[i] > max):    
        max = arr[i];    
               
print("Largest number present in given array: " + str(max));   


#Sorting list of Integers in descending in an array #4

numbers = [2, 53, 11, 565]

# Sorting list of Integers in descending
numbers.sort(reverse = True)
  
print("Numbers sorted in descending order array: " + str(numbers));


#Multiply Every number in Array Item with each other in sequence order #5

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
 
list1 = [2, 3, 5]
list2 = [3, 5, 4]
print(multiplyList(list1))
print(multiplyList(list2))



# Code to remove duplicate numbers in array #6
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
duplicate = [2, 4, 10, 20, 5, 2, 20, 4, 90, 2, 4]
print(Remove(duplicate))


# Sum of the Odd Numbers when max number is given #7
maximum = int(input(" Please Enter the Maximum Value : "))
Oddtotal = 0

for number in range(1, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal))

