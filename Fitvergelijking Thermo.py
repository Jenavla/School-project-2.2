import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

# Constanten
l_0 = 10e-2
lambda_ = 532e-9  
delta_T = np.linspace(0, 100, 1000)
alpha = 12e-6

# Definieer de functie op basis van de gegeven formule
def theoretische_fringes(alpha, l_0, lambda_, delta_T):
    return (2 * alpha * l_0 * delta_T) / lambda_

# Bereken de theoretische waarden voor de hele reeks invalshoeken
theoretische_waarden = theoretische_fringes(alpha, l_0, lambda_, delta_T)

# Plot de resultaten met foutenbalken
plt.plot(delta_T, theoretische_waarden, label='Theorie')
plt.xlabel('Delta T')
plt.ylabel('Aantal franjes')
plt.title('Plot van theoretische fit')
plt.legend()
plt.show()

