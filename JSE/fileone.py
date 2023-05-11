import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


MTN = pd.read_csv('Downloads/MTN.JO.csv', index_col='Date', parse_dates=True)
NDB = pd.read_csv('Downloads/NED.JO.csv', index_col='Date', parse_dates=True)
ZAR = pd.read_csv('Downloads/ZAR=X.csv', index_col='Date', parse_dates=True)
FSR = pd.read_csv('Downloads/FSR.JO.csv', index_col='Date', parse_dates=True)
ABG = pd.read_csv('Downloads/ABG.JO.csv', index_col='Date', parse_dates=True)

# print(MTN.head())
# plt.plot(MTN['Close'])
# plt.show()

print(FSR.head())
plt.figure('Banks and MTN share price')
plt.title('South AFrican Banks + MTN')
plt.plot(ABG['Close'], color='red', label='ABSA')
plt.plot(NDB['Close'], color='green', label='NEDBANK')
plt.plot(MTN['Close'], color='yellow', label='MTN')
plt.plot(FSR['Close'], color='blue', label='FirstRand')
plt.legend()
plt.figure('South African Rand')
plt.title('South AFrican RAND')
plt.plot(ZAR['Close'], label='ZAR', color='indigo')

plt.show()
