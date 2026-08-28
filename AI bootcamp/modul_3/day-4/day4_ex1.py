import sympy as sp

#DEfine function
x = sp.Symbol('x')
f = sp.exp(-x)

# compute indefinite integral
indefinite_integral = sp.integrate(f, x)
print("Idefinite Integral:",indefinite_integral)

#Compute definite integral
definite_integral = sp.integrate(f,x,0,sp.oo)
print("Definite Integral: ",definite_integral)