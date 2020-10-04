#I am writig a code for finding Minimum Maximum, Average and Range of given set of numbers
Input_1=int(input("Enter a number 1:"))
Input_2=int(input("Enter a number 2:"))
Input_3=int(input("Enter a number 3:"))
Input_4=int(input("Enter a number 4:"))
Input_5=int(input("Enter a number 5:"))
minimum=min(Input_1,Input_2,Input_3,Input_4,Input_5)
print ("Minimum number is:"+ str(minimum))
maximum=max(Input_1,Input_2,Input_3,Input_4,Input_5)
import statistics
Sum=Input_1,Input_2,Input_3,Input_4,Input_5
Average=statistics.mean(Sum)
print ("Maximum number is:"+ str(maximum))
print ("The average of the numbers is: "+ str(Average))
print ("Range of the numbers is: "+str(maximum-minimum))
