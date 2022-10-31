from scipy.signal import lfilter
import matplotlib.pyplot as plt
import math
import numpy as np
import librosa as lb
from get_data import hourly_price_historical

df = hourly_price_historical("BTC","USD",2000,1,"h")
closeValue = []
for i in range(len(df)):
        closeValue.append([df["close"][i]])

n1 = 200
n2 = len(closeValue)
y  = np.asarray(closeValue[n1:n2]).flatten()

m=150 # longueur de chaque trame d analyse est m
NbTrames = math.floor((n2-n1+1)/m)

ordreAR=5   # ordre du modele AR
#Premiere trame
y1= np.transpose(y[1:m])

coeffsAR1 = lb.lpc(np.asarray(y1,float),order = ordreAR)

yf1=lfilter(coeffsAR1,1,y1)
residuel = y1-yf1 
residuel = np.transpose(residuel)  # erreur residuelle d estimation

plt.subplot(2,2,1)
plt.plot(y1)
plt.title(['Trame 1 (T1)'])

plt.subplot(2,2,2)
plt.plot(yf1)
plt.title(['Erreur sur T1'])

plt.subplot(2,2,3)
plt.plot(y1-yf1)
plt.title(['Estimee sur T1'])

plt.subplot(2,2,4)
plt.plot(np.correlate(yf1,yf1,"full"))
plt.title(['Correlation erreur sur T1'])

plt.show()
#####################################################################

Synth2 = np.transpose(lfilter([1],coeffsAR1,np.random.rand(len(y1))))
Synth3 = np.transpose(lfilter([1],coeffsAR1,yf1))


plt.plot(Synth2/max(abs(Synth2)))
plt.plot(Synth3/max(abs(Synth3)),'r')
plt.title('Syntheses')
plt.legend(['Synthèse par BBG', 'Synthèse par Erreur-residuelle'])
plt.show()
########################################################################""

NbTramesAffichees = 10  # doit etre inferieur a  NbTrames
m1=ordreAR+1 

for k in range(1,NbTrames-1):
    y2 = y[k*m -m1 + 1 : (k+1)*m]
    #calcul des coefficients d'un AR d'ordre n
    coeffsAR2 = lb.lpc(np.asarray(y2,float),order = ordreAR)
    yf2 = lfilter(coeffsAR2,1,y2)
    residuel2 = y2[m1:m1+m-1]-yf2[m1:m1+m-1]
    residuel = [residuel, residuel2]
    synth2= lfilter([1],coeffsAR2,np.random.rand(len(y2)))
    synth3= lfilter([1],coeffsAR2,yf2)
    synth2 = synth2[m1:m1+m-1]
    synth3 = synth3[m1:m1+m-1]
    Synth2 = [Synth2,synth2]
    Synth3 = [Synth3,synth3]
    if k <= (NbTramesAffichees-1) :
        
        plt.subplot(2,2,1)
        plt.plot(y2[m1:m1+m-1])
        plt.title(['Trame ' ,str(k)])
        plt.subplot(2,2,2)
        plt.plot(yf2[m1:m1+m-1])
        plt.title(['Erreur'])
        plt.subplot(2,2,3)
        plt.plot(residuel2)
        plt.title(['Estimee'])
        plt.subplot(2,2,4)
        plt.plot(np.correlate(yf2,yf2,"full"))
        plt.title(['Correlation erreur'])
        plt.show()
        
        plt.plot(synth2/max(abs(synth2))) 
        plt.plot(synth3/max(abs(synth3)),'r')
        plt.legend(['Synthèse par BBG', 'Synthèse par Erreur-residuelle'])
        plt.title('Syntheses de parole')
        plt.show()