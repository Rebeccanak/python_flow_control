 Write a function that uses while, if and continue statements 
# to print all the even numbers between 0 and 50. 
def even_numbers():
    x=0
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(x)
    


# Write a function that takes an integer argument 
# and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def number_is_prime(number):
    if number>=1:
        for i in range(2,number):
            if (number%2)==0:
                print(number,"Is not prime")
                break
        else:
            print(number, "Prime")


# Write a function that takes a list of integers as input 
# and prints the sum of all the even numbers in the list.
def sum_of_all_even(numbers):
    total=0
    for i in numbers:
        if i%2==0:
            total+=i
    print(total)