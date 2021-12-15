import math

def main():
    number = float(input("Float to round: "))
    return math.ceil(number/5) * 5

if __name__ == "__main__":
    print(main())