
import pandas as pd
from scipy.signal import welch
window_data = pd.read_csv(r'C:\Users\Emad\Desktop\window_data.csv',header=None)

#window_data = data.loc[window_start: window_end]
Fxx, Pxx = welch(x=window_data, window='hamming',fs=256, nperseg=128,nfft=256,noverlap=64, axis=0)
#Fxx, Pxx = welch(x=window_data, fs=256, axis=0)

print Fxx