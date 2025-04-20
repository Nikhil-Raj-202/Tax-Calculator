def main():
    income = float(input("Enter your annual income (in lakh): "))

    if income <= 1200000:
        print("Total tax = 0")
    elif income <= 1600000:
        tax = (400000 * 0.0) + (400000 * 0.05) + (400000 * 0.10) + ((income - 1200000) * 0.15)
        print(f"Total tax = {tax}")
    elif income <= 2000000:
        tax = (400000 * 0.0) + (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + ((income - 1600000) * 0.20)
        print(f"Total tax = {tax}")
    elif income <= 2400000:
        tax = (400000 * 0.0) + (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + ((income - 2000000) * 0.25)
        print(f"Total tax = {tax}")
    else:
        tax = (400000 * 0.0) + (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (400000 * 0.25) + ((income - 2400000) * 0.30)
        print(f"Total tax = {tax}")

if __name__ == "__main__":
    main()

