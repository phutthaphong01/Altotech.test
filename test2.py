import pandas as pd
import numpy as np
import plotly.express as px


meter_solar = 'meter_solar.xlsx'
df = pd.read_excel(meter_solar)
df

meter_solar = 'meter_solar.xlsx'
cols = [0,3]
df = pd.read_excel(meter_solar, usecols=cols)
df

meter_solar = 'meter_solar.xlsx'
cols = [0,3]
df = pd.read_excel(meter_solar, usecols=cols)
a = df.energy_total.mean()
print(a ,'kWh For mean in 10/09/2021-22/09/2021')