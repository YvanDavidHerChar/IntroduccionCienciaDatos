import numpy as np
import matplotlib.pyplot as plt
import sklearn.model_selection
import sklearn.linear_model

class ComparandoBetas:
    def __init__(self, degree=5):
        self.degree = degree
        
    def fit(self,X,Y):
        betas = np.zeros(self.degree)
        #Realizar el Fit
        regresion = sklearn.linear_model.LinearRegression()
        regresion.fit(X,Y)
        #Dar el beta
        betas[0] = regresion.intercept_
        betas[1:] = regresion.coef_
        return betas
        
    def losBetas(self, x, y, n=1000):
        d = self.degree
        betas = np.zeros(shape=(n,d))
        for i in range(n):
            betas[i,:] = self.fit(X,y)
        return betas

    
    def graficarbetas(self,X,Y):
        #Graficar los fits
        M = self.degree
        B = self.losBetas(X,Y)
        promedios = np.mean(B[:,1:], axis=0)
        varEsta = np.std(B[:,1:], axis=0)
        plt.figure(figsize=(12,12))
        for i in range(M-1):
            plt.subplot((M-1)/2,(M-1)/2,i+1)
            plt.title('Beta '+str(i+1) + ' Promedio='+ '{:.2f}'.format(promedios[i]) +' STD='+ '{:.2f}'.format(varEsta[i]))
            plt.hist(B[:,i+1])
            plt.savefig("Losbetas.png", bbox_inches='tight')   

                       
data = np.loadtxt("notas_andes.dat", skiprows=1)
Y = data[:,4]
X = data[:,:4]
Entreno = ComparandoBetas()
Entreno.graficarbetas(X,Y)
