import numpy as np
from scipy.integrate import solve_ivp

from values import val

# Differential equation
def eq(t, tab):
    nbObj = len(tab)

    der = np.zeros_like(tab, dtype=float)

    # Derivation
    for i in range(nbObj):
        # x to v
        der[i][0] = tab[i][3]
        der[i][1] = tab[i][4]
        der[i][2] = tab[i][5]

        # v to a
        others = [k for k in range(nbObj) if k != i]
        a = np.zeros(3, dtype=float)
        for j in others:
            r = [tab[j][0] - tab[i][0], tab[j][1] - tab[i][1], tab[j][2] - tab[i][2]]
            for k in range(len(r)):
                a[k] += val['cavendish'] * tab[j][6] * r[k] / np.linalg.norm(r)**3
        
        der[i][3] = a[0]
        der[i][4] = a[1]
        der[i][5] = a[2]
    
    return der

# Reshapes array for eq and solve_ivp
def trad(t, tab, nbObj):
    n = np.reshape(tab, (nbObj, 7))
    r = eq(t, n)
    n = np.reshape(r, nbObj*7)
    return n

# Calculates the trajectories
def traj(values):
    nbObj = len(values['init'])

    sol = solve_ivp(lambda t, tab: trad(t, tab, nbObj), [0, values['length']], \
                    np.reshape(values['init'], nbObj*7), \
                    rtol = values['solveivp']['rtol'], \
                    atol = values['solveivp']['atol'], \
                    max_step = values['solveivp']['max-step'])
    
    points = np.zeros((nbObj, 3, len(sol.t)))
    for i in range(len(sol.t)):
        for j in range(nbObj):
            for k in range(3):
                points[j][k][i] = sol.y[j*7 + k][i]
    
    return points