#Start

num: int = int (input("Please enter a number"));
if num % 5 == 0 and num % 3 == 0:
    print("Fizz Buzz");
elif num % 3 == 0:
    print ("Buzz");
elif num % 5 == 0:
    print("Fizz");
else:
    print ("Not a shred of Fizz and not a flake of Buzz");

#End
