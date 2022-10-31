from xml.sax import default_parser_list
from scipy.signal import lfilter
import matplotlib.pyplot as plt
import math
import numpy as np
import librosa as lb


def AR_model(df, resp, symbol, comparative_symbol):
    details = True
    if resp == "n":
        details = False

    closeValue = []
    for i in range(len(df)):
        closeValue.append([df["close"][i]])

    n1 = 200
    n2 = len(closeValue)
    y = np.asarray(closeValue[n1:n2]).flatten()

    m = 150  # longueur de chaque trame d'analyse 
    NbTrames = math.floor((n2 - n1 + 1) / m)

    ordreAR = 5  # ordre du modèle AR

    # Premiere trame
    y1 = np.transpose(y[1:m])

    coeffsAR1 = lb.lpc(np.asarray(y1, float), order=ordreAR)

    yf1 = lfilter(coeffsAR1, 1, y1)
    residuel = y1 - yf1
    residuel = np.transpose(residuel)  # erreur residuelle d'estimation

    m1 = ordreAR + 1

    for k in range(1, NbTrames):
        y2 = y[k * m - m1 + 1: (k + 1) * m]
        # calcul des coefficients d'un AR d'ordre n
        coeffsAR2 = lb.lpc(np.asarray(y2, float), order=ordreAR)
        yf2 = lfilter(coeffsAR2, 1, y2)
        residuel2 = y2[m1:m1 + m - 1] - yf2[m1:m1 + m - 1]
        residuel = np.append(residuel, residuel2)

        if details:
            fig, ax = plt.subplots(2, 2)
            fig.tight_layout(h_pad=2)

            plt.subplot(2, 2, 1)
            plt.plot(y2[m1:m1 + m - 1])
            plt.title(['Trame ' + str(k)])

            plt.subplot(2, 2, 2)
            plt.plot(yf2[m1:m1 + m - 1])
            plt.title(['Erreur'])

            plt.subplot(2, 2, 3)
            plt.plot(residuel2)
            plt.title(['Estimee'])

            plt.subplot(2, 2, 4)
            plt.plot(np.correlate(yf2, yf2, "full"))
            plt.title(['Correlation erreur'])

            plt.show()

    # Suppression de termes pour faire concorder les courbes
    residuel = np.delete(residuel, 0)
    y = np.delete(y, list(range(14)))
    df = df.iloc[214:]

    # Tracé de la courbe réelle (bleu) et de son estimation (rouge)
    plt.plot(df.timestamp, df.close)
    plt.plot(df.timestamp, residuel, 'r', alpha=0.5)
    plt.title("Auto-Regressive Model")
    plt.xlabel("Timestamp")
    plt.ylabel(comparative_symbol)
    plt.legend([symbol, 'Estimated with the AR model'])
    plt.xticks(rotation=60)
    plt.show()
