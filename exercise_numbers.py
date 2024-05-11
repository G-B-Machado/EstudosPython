def main():
    show_successor(15)
    show_predecessor(15)
    verify_even_or_odd(15)
    verify_even_or_odd(14)

def show_successor(number):
    print(number+1)

def show_predecessor(number):
    print(number-1)

def verify_even_or_odd(number):
    if(number%2 == 0):
        print("The number is even")
    else:
        print("Number is odd")


main()