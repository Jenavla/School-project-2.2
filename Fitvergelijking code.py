import numpy as np
import matplotlib.pyplot as plt

# Definieer de functie op basis van de gegeven formule
def fit_vergelijking(n_glas, d, i, r, lapda):
    term1 = (2 * d) / lapda
    term2 = n_glas / np.cos(r)
    term3 = np.tan(i) * np.sin(i)
    term4 = np.tan(r) * np.sin(i)
    term5 = (n_glas - 1)
    term6 = 1 / np.cos(i)
    
    print(np.max(term1 * (term2 + term3 - term4 - term5 - term6)))
    
    return term1 * (term2 + term3 - term4 - term5 - term6)

# Constanten
n_glas = 1.49
n_lucht = 1.00029
d = 3e-3
lapda = 532e-9
i = np.radians(np.linspace(0, 15, 1000))
r = np.arcsin(((n_lucht * np.sin(i)) / n_glas))

# Bereken het aantal fringes op basis van de functie
aantal_fringes = fit_vergelijking(n_glas, d, i, r, lapda) 

# Plot de resultaten
plt.plot(np.degrees(i), aantal_fringes)
plt.xlabel('Invalshoek (graden)')
plt.ylabel('Aantal fringes')
plt.title('Plot van Fit Vergelijking')
plt.ylim()
plt.xlim(0, 15)
plt.show()
