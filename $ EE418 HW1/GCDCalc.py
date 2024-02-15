import math

def gcd(*args):
    num_args = len(args)
    if num_args < 2:
        raise ValueError("At least two numbers are required to compute the GCD.")
    gcd_value = math.gcd(args[0], args[1])
    for i in range(2, num_args):
        gcd_value = math.gcd(gcd_value, args[i])
    return gcd_value

def get_user_inputs():
    try:
        num_inputs = int(input("Enter the number of inputs: "))
        if num_inputs < 2:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid number greater than 1.")
        return get_user_inputs()  # Recursive call to get valid input
    return [int(input(f"Enter number {i + 1}: ")) for i in range(num_inputs)]

# Get user inputs
user_inputs = get_user_inputs()

# Compute and print GCD
gcd_result = gcd(*user_inputs)
print(f'GCD = {gcd_result}')
