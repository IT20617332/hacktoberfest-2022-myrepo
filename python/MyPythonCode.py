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
