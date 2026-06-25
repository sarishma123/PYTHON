P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate: "))
t = float(input("Enter the time: "))
N = int(input("Enter the compound frequency: "))

A = P * (1 + R / N) ** (N * t)

print("Compound Amount =", A)