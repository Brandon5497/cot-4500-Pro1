#Approximation Algorithm
print("Approximation Algorithm")
x0 = float(input("Enter starting value: "))
tol = float(input("Enter tolerance value: "))
iter = 0
diff = x0
x = x0

while diff >= tol:
  iter += 1
  y = x

  x = (x / 2) + (1 / x)
  diff = abs(x - y)

print(f"Convergence after {iter} iterations\n")

#Bisection Method
print("Bisection Method")
expression = input("Enter a function (e.g., x**2 + x + 3): ")
tol = float(input("Enter tolerance value: "))
a = float(input("Enter left starting endpoint: "))
b = float(input("Enter right starting endpoint: "))

func = lambda x: eval(expression)
aVal = func(a)

i = 0
while(abs(b - a) > tol):
  i += 1
  p = (a + b) / 2
  pVal = func(p)

  if(((aVal) < 0) & ((pVal) > 0) | ((aVal) > 0) & ((pVal) < 0)):
    b = p
  else:
    a = p

print(f"Bisection method: {p}")