def check_prime(number):
    if number > 1:
        for num in range(2, number):
            if (number % num) == 0:
                return False
                break
        else:
            return True
    else:
        return False


flag = True

while(flag):
    user_input = input("Please enter the a number or q to quit: ")
    if user_input.lower() == 'q':
        flag = False
    else:
        try:
            if check_prime(int(user_input)):
                print("{} is a prime number".format(user_input))
            else:
                print("{} is not a prime number".format(user_input))
        except ValueError:
            print("Please enter the a valid input")
