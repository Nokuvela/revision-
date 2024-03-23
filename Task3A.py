 
 
import pandas as pd
insurance =pd.read_csv("c:/Users/CC/Downloads/motor_insure.csv/motor_data11-14lats.csv")

print("the first 10:")

print(insurance.head(10))

print(insurance[insurance['SEATS_NUM']>40][['MAKE','USAGE']])

import matplotlib.pyplot as plt

insurance['EFFECTIVE_YR']=pd.to_numeric(insurance['EFFECTIVE_YR'],errors='coerce')

plt.figure(figsize=(10, 6))

plt.plot(insurance['EFFECTIVE_YR'],insurance['CARRYING_CAPACITY'] ,color ="orange",alpha = 0.5)
plt.title('EFFECTIVE YEAR vs.CARRYING CAPACITY')
plt.xlabel('EFFECTIVE YEAR')
plt.ylabel('CARRYING CAPACITY')
plt.grid(True)
plt.show()




