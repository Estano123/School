set terminal png
set output 'Methods.png'
set title 'iteratios vs Method'
set xlabel 'Iteration'
set ylabel 'f(x)'
set grid
plot 'data.dat' using 1:2 with lines lc 4 title 'bisection', \
'data.dat' using 1:3 with lines lc 3 title 'Secant', \
'data.dat' using 1:4 with lines lc 7 title 'Newton',\
'data.dat' using 1:5 with lines lc 8 title 'fixed Point'

set output 'euler_plot.png'
set title 'Euler Method for Non-Linear ODE'
set xlabel 'Step Size'
set ylabel 'Exact value & Approximation'
set grid
plot 'euler_method.dat' using 1:2 with lines lc 10 lt 6 title 'Approximated value',\
'euler_method.dat' using 1:3 with lines lt 1 lc 8 title 'exact Temperature'