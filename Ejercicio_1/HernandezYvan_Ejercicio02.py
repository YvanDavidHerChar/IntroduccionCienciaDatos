import numpy as np
import matplotlib.pyplot as plt


class PolyFit:
    def __init__(self, degree=0):
        self.degree = degree
        self.betas = np.zeros(degree)
    
    def y(self,x,w,m):
        y = np.zeros(len(x))
        for i in range(m):
            y += w[i]*x**i
        return y

    def err(self,y,t):
        err=0
        for i in range(len(y)):
            err += (y[i]-t[i])**2
        err = 1/2*err
        return err  

    def fit(self,X,Y):
        M = self.degree
        N = len(X)
        fig1 = plt.figure(figsize=(12,12))
        #Construir el sistema
        S = np.zeros(shape=(N,M))
        for j in range(M):
            S[:,j] = X[:]**(j)
        #Resolver el sistema
        S_1 = np.linalg.pinv(S)
        w = np.dot(S_1,Y)
        #Dar el beta
        self.betas = w

    def predict(self,X):
        w = self.betas
        m = self.degree
        LaPrediccion = self.y(X,w,m)
        return LaPrediccion

    def score(self,x_1, x_2):
        #Guardar el RMS
        RMS = np.zeros(self.degree())
        RMS = np.sqrt(2*self.err(y(x_1,w,i),x_2)/len(x_1))
        return RMS

    def graficarRMS(self,RMS):
        #Graficar el error
        fig2 =plt.figure(figsize=(12,12))
        plt.plot(range(len(RMS)),RMS, c='b')
        plt.savefig("LaSegunda.png", bbox_inches='tight')

    def graficarFit(self,X,Y):
        #Graficar los fits
        M = self.degree
        x = np.linspace(np.min(X),np.max(X),100)
        y = self.predict(x)
        plt.title('M='+ str(M))
        plt.plot(x,y,'r')
        plt.scatter(X,Y,s=80,marker='o', facecolors='none',edgecolor='b')
        plt.savefig("LaPrimera.png", bbox_inches='tight')   

        
                
datos = np.genfromtxt('numeros_20.txt')
DatosEntreno = datos[0:10]
X = DatosEntreno[:,0]
Y = DatosEntreno[:,1]
Entreno = PolyFit(3)
Entreno.fit(X,Y)
Entreno.graficarFit(X,Y)