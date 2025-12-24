import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\himan\OneDrive\Documents\GitHub\PRODIGY_WD_01\PRODIGY_DS_01\API_SP.POP.TOTL_DS2_en_csv_v2_38144 (1).csv", encoding="latin1",skiprows=4)
population_2020 = df["2020"].dropna()

plt.figure()
plt.hist(population_2020, bins=20)
plt.xlabel("population")
plt.ylabel("Number of countries")
plt.title("Population Distributaion (2020)")
plt.show()