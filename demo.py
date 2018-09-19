import numpy as np
import matplotlib.pyplot as plt

def integrate_riemann_left( f, a, b, N ):

    h = float(b-a)/N
    I = 0.0

    for k in range(N):
        x = a + k*h
        I += h * f(x)

    return I


def f1(x):
    return np.sin(x)

a = 0.0
b = np.pi/2
N = 100
exact = 1.0

I1 = integrate_riemann_left( f1, a, b, N )
print( I1, I1-exact )

Ns = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
err_list = []

for N in Ns:
    I = integrate_riemann_left( f1, a, b, N )
    err = I - exact
    err_list.append(err)

print( err_list )

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.plot( Ns, np.fabs(err_list) )

ax2 = fig.add_subplot(2,1,2)
ax2.plot( Ns, np.fabs(err_list) )
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xlabel(r"$N$")
ax2.set_ylabel(r"$L_1 = \int f(x) dx - $ true")

plt.savefig('left_riem_convergence.png')
plt.show()




    


