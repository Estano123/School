import numpy as np


#TASK 1
#-------------------------------------------------------------------------------------------
def f(x):
    fx = (x**3) - (3*(x**2)) + x - 1
    return fx

def df(x):
    dfx = 3*(x**2) - (6*x) + 1
    return dfx
N = 100 # Maximum number of iterations
tol=1e-6
# BISECTION METHOD
def bisection_method(a, b):
    iterations = []
    n = 0
    if f(a) * f(b) < 0:  
        while (abs(b - a) > tol) and (n < N):
            c = (a + b) / 2
            iterations.append(f(c))
            if f(c) == 0: 
                break
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
            n += 1
        return iterations
    else:
        print("Invalid interval. f(a) and f(b) must have opposite signs.")
 

#SECANT METHOD
def secant_method(x0, x1, tol=1e-6):
    iterations = []
    n = 0
    while (abs(x1 - x0) > tol) and (n < N): 
        f0, f1 = f(x0), f(x1)
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        iterations.append( f(x2))  
        x0, x1 = x1, x2
        if abs(f(x2))<tol:
            break
        n += 1
    return iterations


# Newton-Raphson method
def newton_raphson(x0, tol=1e-6):
    iterations = []
    c = True
    while c:
        x1=x0 - f(x0) / df(x0)
        iterations.append(f(x1))  
        if (abs(f(x0)) <tol) :
            c = False
            
        x0 = x1
    return iterations



#FIXED POINT METHOD
def psi(x):
    return (x**2 -x+1)**(1/3)

def fixed_point_method(x0, tol=1e-6):
    iterations = []
    x1 = psi(x0)
    c = True
    
    while c:
        x1 = psi(x0)
        iterations.append(f(x1))  # Append iteration number and function value
        if (abs(x1 - x0) < tol):
            c = False
        x0 = x1
    return iterations

# File output 
def file_output_combined_table(filename, bisection_iterations, secant_iterations, newton_raphson_iterations, fixed_point_iterations):
    with open(filename, "w") as file:
        file.write(f"{'Iteration':<15}{'fx_Bisection':<15}{'fx_Secant':<15}{'fx_Newton':<15}{'fx_Fixed Point':<15}\n")
        
        max_iterations = max(len(bisection_iterations), len(secant_iterations), len(newton_raphson_iterations), len(fixed_point_iterations))

        for i in range(max_iterations):
            if i < len(bisection_iterations):
                bisection_value = f"{bisection_iterations[i]:.11f}"
            else:
                bisection_value = "---"  
            if i < len(secant_iterations):
                secant_value = f"{secant_iterations[i]:.11f}"
            else:
                secant_value = "---"  
            if i< len(newton_raphson_iterations):
                newton_value = f"{newton_raphson_iterations[i]:.11f}"
            else:
                newton_value = "---"
            if i< len(fixed_point_iterations):
                fixed_point_value = f"{fixed_point_iterations[i]:.11f}"
            else:
                fixed_point_value = "---"
            
            file.write(f"{i + 1:<15}{bisection_value:<15}{secant_value:<15}{newton_value:<15}{fixed_point_value:<15}\n")

bisection_results = bisection_method(2,3)
secant_first = secant_method(2,3)
newton_first = newton_raphson(2)
fixed_point_first = fixed_point_method(2)

# Write results to a single file in table format
file_output_combined_table("data.dat", bisection_results, secant_first, newton_first, fixed_point_first)

#------------------------------------------------------------------------------------------
#TASK2
#Euler Method
def euler_method():
    dT = lambda x: -2.2067*(10**-12)*(x**4 - 81*(10**8))
    init_T0 = 1200
    T0 = 1200
    t0 = 0
    solution = []
    r = []
    h = [30,60,120,240,480]
    hr = []
    for j in h:
        for i in range(j,480+1, j):
            t0 += j
            Ti = T0 + dT(T0)*j
            T0 = Ti
            if i == 480:
                solution.append(T0)
                T0 = init_T0
    for k in range(len(solution)-1,-1,-1):
        r.append(solution[k])
        hr.append(h[k])

    return (hr,r)
stepsize, solution = euler_method()
exact_euler = [1635.4,537.26,100.80,32.607,14.806]
with open("euler_method.dat", "w") as file:
    file.write("#Step Size \t #Approx_Temperature \t #Exact_Temperature\n")
    for i, j, k in zip(stepsize, solution,exact_euler):
        file.write(f"{i}\t {j} \t {k}\n")


#--------------------------------------------------------------------------------------------------

#TASK 3 Challenge
def gaussian_elimination(A, b):
    n = len(A)

    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    b[i], b[k] = b[k], b[i]
                    break
            else:
                raise ValueError("Matrix is singular or nearly singular.")
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
    # Back Substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum_ax = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - sum_ax) / A[i][i]

    return np.array(x).reshape(-1, 1)
    
A = [
    [17, 14, 23],
    [-7.54, -3.54, 2.7],
    [6, 1, 3]
]
b = [22.5, 2.352, 14]
k = np.array(np.linalg.solve(A, b)).reshape(-1,1)
print(f"[Numpy solution:] \n{k}\n")
solution = gaussian_elimination(A, b)
print( f"With Naive Gaussian Elimination \n[X] = \n{solution}\n")     