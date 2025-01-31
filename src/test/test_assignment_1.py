import sympy as sp
import math

#Approximation Algorithm
print("Approximation Algorithm")
x0 = 1.5
tol = 0.000001
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

#expression = input("Enter a function (e.g., x**2 + x + 3): ")
tol = 0.001
a = -4
b = 7

#func = lambda x: eval(expression)
#aVal = func(a)

i = 0
while(abs(b - a) > tol):
  i += 1
  p = (a + b) / 2
  #pVal = func(p)

  if(((a**3 - a**2 + 4) < 0) & ((p**3 - p**2 + 4) > 0) | ((a**3 - a**2 + 4) > 0) & ((p**3 - p**2 + 4) < 0)):
    b = p
  else:
    a = p

print(f"Bisection method iterations: {p}\n")



# Fixed-point Iteration
print("Fixed-point Iteration")

p0 = 1.5
tol = 0.000001
n0 = 50 
#expression = input("Enter a function (e.g., math.tan(x), x**2 + 3*x + 1): ")

func = lambda x: eval(expression, {"x": x, "math": math}) 

i = 1
while i <= n0:
    p = math.sqrt(10 - p0*p0*p0) / 2
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

expression = "cos(x) - x"
f = sp.sympify(expression)

f_prime = sp.diff(f, x)

prev = (math.pi) / 4
tol = 0.0001
n0 = 50

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






