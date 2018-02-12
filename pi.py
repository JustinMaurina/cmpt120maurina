# pi.py
# Approximates the value of pi
# JA: You also had to print the difference between the calculated value
# and math.pi
def main ():
    n = int(input("Enter the number of terms to use:"))

    pi = 0
    sign = 1
    for i in range(1, n * 2 + 1, 2):
        term = 4/ i * sign
        pi = pi + term
        sign = sign * -1

    print("The approximated value of pi is:", pi)
main()
        
        
