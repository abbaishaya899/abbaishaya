p = float(input("Enter p: "))

r = float(input("Enter r: "))

t = float(input("Enter t: "))

n = float(input("Enter n: "))

SI = str(p * (1 + r * t))
CI = p * (1 + r/n) ** n * t

print("Yusuf and sons "+ SI)
