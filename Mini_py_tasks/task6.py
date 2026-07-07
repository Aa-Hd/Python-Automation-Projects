#Write a python programe which takes an integer between 1 and 10000 and print it in words

number = int(input("Enter a number (1-10000): "))        #task 6

ones = ["","one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

if number == 10000:
    print("ten thousand")

else:
    if number >= 1000:
        print(ones[number//1000], "thousand", end=" ")
        number = number % 1000

    if number >= 100:
        print(ones[number//100], "hundred", end=" ")
        number = number % 100

    if number >= 20:
        print(tens[number//10], end=" ")
        number = number % 10

    elif number >= 10:
        print(teens[number-10], end=" ")
        number = 0

    if number > 0:
        print(ones[number], end="")