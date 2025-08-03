print("_________________________________________________________________________________________________________________________________________________________")
print("-----------------------------------------------------------------!! OM GANESHAYE NAMAH !! ------------------------------PYTHON ")
print("__________________________________________________________________________________________________________________________________________________________")

# enter=input("which table you want to print? : ")
# number = int(enter)
# #loop
# for i in range (1,11):
#     print(number, "x", i, "=", number * i)

# for i in range(1, 11):
#     if i==5:
#         print("Skipping the number 5")
#         continue
#     else:
#         print(i)

# # whilw loop
# i = 1
# while i <= 10:
#     print("yes i is smaller then 10 ",i)
#     i += 1
# if i > 10:
#     print("sorry we cant print more numbers : ",i)

# n = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial =factorial* i  # i will add and updated the value of factorial
# print(f"The factorial of {n} is {factorial}")


# # code for find th perfect number
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n):  # we dont want to include the number itself so w cant use range(1, n+1)
#     if n%i==0:
#        sum += i  # sum will add the value of i and update the value of sum
# print(f"The sum of the factors of {n} is {sum}")
# if sum == n:
#     print(f"{n} is a perfect number")


# n = int(input("Enter a number: "))
# couont = 0
# for  i in range (1 , n + 1):
#     if n % i==0:
#         couont+= 1
# if couont == 2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

# a = "KABIR"
# for i in range(len(a)-1,-1, -1):
#    print(a[i])


# # code for palindrome checking
# a = "kabir"
# result = ""
# for i in range(len(a)-1, -1, -1):
#     result = result+ a[i]
# if a == result:
#     print(f"{a} is a palindrome")
# else:
#     print(f"{a} is not a palindrome")


# print(dir(str))  # this will show all the methods of string

#  while loop

# i = 1
# while i <= 10:
#     print("yes i is smaller then 10 ", i)
#

# random number guessing game .___________________________while loop game________________________________
# import random
# print("Welcome to the random number guessing game!")
# num = random.randint(1,10)

# trys= 0
# while True:
#     print("I have selected a number between 1 and 10. Can you guess it?")
#     quess = int(input("Enter your guess: "))
#     if quess == num:
#         trys+=1
#         print("Congratulations! You guessed the number correctly.")
#         break  # loop will end when we entter right numbeer
#     else:
#         trys+=1
#         print(f"Sorry, the number was {num}. Better luck next time!")
#         print(f" the number was {num}")

# _________________________________________________________________FUNCTION___________________________
# reusable code
# def funcname():
#     print("thsi is function")

# #  but it will run after wew call it. with the fnction name othervise it wont work
# funcname()

# _____function parameters and arguments
# a1 = int(input("rnter a:"))
# b1 = int(input("rnter b:"))

# def param(a, b):
#     print(f"the sum of two parameters {a+b}")
# param(a1, b1)

# type of arguments___________________
# default , positional , keyword arguments

# ____________Q. palindrom check from function?
# words = input("enter your word ")

# def palindrom(word):
#     rev = ""
#     for i in range(len(word)-1, -1, -1):
#         rev = rev+word[i]  # the otput store into rev
#     if rev == word:
#         print("yes palin")
#     else:
#         print("no palin")

# palindrom(words)

# ____________________________________________________________________Return____________
# def heloo():
#     return "helooform f'unction "
# print(heloo())  # caal the function but in printed form 