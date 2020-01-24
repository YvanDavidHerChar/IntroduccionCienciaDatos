import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt('numeros_20.txt')
DatosEntreno = datos[0:10]
DatosTest = datos[11:20]

def y(x,w,m):
    y = np.zeros(len(x))
    for i in range(m):
        y += w[i]*x**i
    return y
    
def err(y,t):
    err=0
    for i in range(len(y)):
        err += (y[i]-t[i])**2
    err = 1/2*err
    return err  

def solver(M):
    
    TraErr = np.zeros(M)
    TesErr = np.zeros(M)
    
    fig1 = plt.figure(figsize=(12,12))
    for k in range(M):
        i = k+1
        #Construir el sistema
        S = np.zeros(shape=(i,i))
        for j in range(i):
            S[:i,j] = DatosEntreno[:i,0]**(j)
        #Resolver el sistema
        S_1 = np.linalg.inv(S)
        w = np.dot(S_1,DatosEntreno[:i,1])
        #Guardar el RMS
        TraErr[k] = err(y(DatosEntreno[:,0],w,i),DatosEntreno[:,1])
        TesErr[k] = err(y(DatosTest[:,0],w,i),DatosTest[:,1])
        
        #Graficar los fits
        x = np.linspace(np.min(DatosEntreno[:,0]),np.max(DatosEntreno[:,0]),100)
        plt.subplot(M/2,M/2,i)
        plt.title('M='+ str(k))
        plt.plot(x,y(x,w,i),'r')
        plt.scatter(DatosEntreno[:,0],DatosEntreno[:,1],s=80,marker='o', facecolors='none',edgecolor='b')
    plt.savefig("LaPrimera.png", bbox_inches='tight')   
    #Graficar el error
    fig2 =plt.figure(figsize=(12,12))
    plt.plot(range(M),TraErr, c='b')
    plt.plot(range(M),TesErr, c='r')
    plt.savefig("LaSegunda.png", bbox_inches='tight')
        
solver(4)