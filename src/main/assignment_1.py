import sympy as sp
import math

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

print(f"Bisection method: {p}\n")



# Fixed-point Iteration
print("Fixed-point Iteration")

p0 = float(input("Enter initial approximation: "))
tol = float(input("Enter tolerance value: "))
n0 = int(input("Enter max # of iterations: "))  
expression = input("Enter a function (e.g., math.tan(x), x**2 + 3*x + 1): ")

func = lambda x: eval(expression, {"x": x, "math": math}) 

i = 1
while i <= n0:
    p = func(p0)
    if abs(p - p0) < tol:
        print(f"Converged to: {p}")
        break
    i += 1
    p0 = p

    if i > n0:
        print("Max iterations reached, no convergence.")



# Newton-Raphson method
print("\nNewton-Raphson Method")

x = sp.symbols('x')

expression = input("Enter a function (e.g., tan(x), x**2 + 3*x + 1): ")
f = sp.sympify(expression)

f_prime = sp.diff(f, x)

prev = float(input("Enter initial approximation: "))
tol = float(input("Enter tolerance value: "))
n0 = int(input("Enter max # of iterations: "))

i = 1
while i <= n0:
    
    func_value = f.subs(x, prev)  
    derivative_value = f_prime.subs(x, prev)  
    
    if derivative_value != 0: 
        next_value = prev - func_value / derivative_value  
        
        if abs(next_value - prev) < tol:  
            print(f"Converged to: {next_value}")
            break
        i += 1
        prev = next_value
    else:
        print("Unsuccessful: Derivative is zero.")
        break 

if i > n0:
    print("Unsuccessful: Max iterations reached.")





