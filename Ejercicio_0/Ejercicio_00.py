import numpy as np
import matplotlib.pyplot as plt
datos = np.genfromtxt('numeros_20.txt');
N=4;
for i in range(2,(N+2)):
    datosAqui = datos[0:i]
    #Construccion de la matriz S
    S = np.ones(shape=(i,i))
    losx = i-1;
    for j in range(0, losx):
        S[:,j+1] = datosAqui[:,0]**(j+1)
    #Construccion del sistema matricial
    y = datosAqui[:,1]
    S_1 = np.linalg.inv(S)
    betas = np.dot(S_1,y)
    x = np.linspace(0,2,100)
    lasFun = np.zeros(100)
    for j in range(0,losx+1):
        lasFun =+ betas[j]*x**j   
        
    plt.subplot(N/2,N/2,losx)
    plt.title('M='+ str(losx))
    plt.plot(x,lasFun)
    plt.scatter(datosAqui[:,0],datosAqui[:,1])