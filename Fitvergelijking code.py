import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd

data = pd.read_csv('datacsv.csv', sep=',')

# Constanten
n_glas = 1.49
n_lucht = 1.00029
d = 3e-3
lapda = 532e-9
i_theorie = np.radians(np.linspace(0, 15, 1000))

# Datareading
column_names = ['hoeken', 'franjes'] 
data.columns = column_names
i_praktijk = np.radians(data['hoeken'])
fringes_praktijk = data['franjes']

# Combineer hoeken en fringes in een dictionary voor gemakkelijke verwerking
data_dict = {}
for hoek, fringes in zip(i_praktijk, fringes_praktijk):
    if hoek not in data_dict:
        data_dict[hoek] = [fringes]
    else:
        data_dict[hoek].append(fringes)

# Bereken het gemiddelde aantal fringes voor elke unieke hoek
unieke_hoeken = np.array(list(data_dict.keys()))
gemiddelde_fringes = np.array([np.mean(data_dict[hoek]) for hoek in unieke_hoeken])

# Definieer de functie op basis van de gegeven formule
def theoretische_fringes(i, n_glas, d, lapda):
    r = np.arcsin(((n_lucht * np.sin(i)) / n_glas))
    term1 = (2 * d) / lapda
    term2 = n_glas / np.cos(r)
    term3 = np.tan(i) * np.sin(i)
    term4 = np.tan(r) * np.sin(i)
    term5 = (n_glas - 1)
    term6 = 1 / np.cos(i)
    
    return term1 * (term2 + term3 - term4 - term5 - term6)

# Definieer de functie voor de fit op basis van praktijkmetingen
def fit_func(i, n):
    return theoretische_fringes(i, n, d, lapda)

# Bereken de theoretische waarden voor de hele reeks invalshoeken
theoretische_waarden = theoretische_fringes(i_theorie, n_glas, d, lapda)

# Pas de brekingsindex toe op basis van praktijkmetingen
brekingsindex, a = curve_fit(fit_func, i_praktijk, fringes_praktijk)

# Haal de standaarddeviaties uit de covariantiematrix
std_dev = np.sqrt(np.diag(a))

# Bereken het 95% betrouwbaarheidsinterval
bbi = 1.96 * std_dev 

# Bereken de standaardfout
standaard_fout = std_dev[0] / np.sqrt(len(i_praktijk))

# Bereken de praktische waarden voor de invalshoeken
praktijk_waarden = theoretische_fringes(unieke_hoeken, brekingsindex, d, lapda)

# Plot de resultaten met foutenbalken
plt.scatter(np.degrees(unieke_hoeken), gemiddelde_fringes, c='red', marker='x', label='Praktijk')
plt.plot(np.degrees(i_theorie), theoretische_waarden, label='Theorie')
plt.plot(np.degrees(unieke_hoeken), praktijk_waarden, c='red')
plt.xlabel('Invalshoek (graden)')
plt.ylabel('Aantal fringes')
plt.title('Plot van Fit Vergelijking met Betrouwbaarheidsinterval')
plt.legend()
plt.show()

print(f"Berekende brekingsindex n: {brekingsindex[0]}")
print(f"Standaarddeviatie: {std_dev[0]}")
print(f"Betrouwbaarheidsinterval (95%): {bbi[0]}")
print(f"Standaardfout: {standaard_fout}")
