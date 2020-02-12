import random
import sys

count = 0
while True:

    user_inp = input("Enter a number:\n")
    number = random.randint(1, 9)

    if str(user_inp) == "q":

        break
    elif int(user_inp) < number:
        print("too low")
        count +=1
    elif int(user_inp) > number:
        print("too high")
        count +=1
    elif int(user_inp) == number:
        print("exact right")
        count += 1
        break

print(count)

