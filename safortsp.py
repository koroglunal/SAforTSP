"""
Created on Fri Jun 12 15:38:36 2020

@koroglunal: Unal KOROGLU 

University of Dokuz Eylul in Turkey
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SA(object):
    def __init__(self,n,maxit,maxitpermtemp,T0):
        self.n = n #number of citiy 
        self.maxit = maxit
        self.maxitpermtemp = maxitpermtemp
        self.x = np.random.randint(20,50,self.n)
        self.y = np.random.randint(20,50,self.n)
        self.D = np.zeros((self.n,self.n))
        self.tour = np.random.permutation(self.n)
        self.bestcost = np.zeros((self.maxit,1))
        self.sol = {"tour":self.tour,"cost":self.cost(self.tour)}
        self.T = T0
        self.T0 = T0
        for i in range(0,self.n-1):
            for j in range(self.n):
                self.D[i,j]=np.sqrt((self.x[i]-self.x[j])**2+(self.y[i]-self.y[j])**2)
                self.D[j,i]=self.D[i,j]
        
    
    def swap(self,route):
        ix=np.random.permutation(len(route))
        i1=ix[1]
        i2=ix[2]
        newroute = np.copy(route)
        newroute[i1],newroute[i2] = newroute[i2],newroute[i1]
        return newroute
    
    def cost(self,route):
        L=0 
        route = np.append(route,route[0])
        for i in range(self.n):
            L=L+self.D[route[i],route[i+1]]
        return L
    
    def main(self):
        
        sol_tour = self.tour
        sol_cost = self.cost(sol_tour)
        
        bestsol_tour = sol_tour 
        bestsol_cost = sol_cost
        
        for it in range(self.maxit):
            for it2 in range(self.maxitpermtemp):
                newsol_tour = self.swap(sol_tour)
                newsol_cost = self.cost(newsol_tour)
                
                if newsol_cost < sol_cost:
                    sol_cost = newsol_cost
                    sol_tour = newsol_tour

                else:
                    delta = (newsol_cost - sol_cost)
                    p = np.exp(-delta/self.T)
                    
                    if np.random.rand() < p:
                        sol_cost = newsol_cost
                        sol_tour = newsol_tour
             
                if sol_cost < bestsol_cost:
                    bestsol_cost = sol_cost
                    bestsol_tour = sol_tour
            
            self.bestcost[it] = bestsol_cost
            self.T = self.T*0.99
            
        self.draw(bestsol_tour)
        
    def draw(self,tour):
        
        sns.set()
        tour = np.append(tour,tour[0])
        plt.axes([0,0,2,1.3])
        plt.plot(self.x[tour],self.y[tour],'rD-',label="City")
        plt.title("Route")
        plt.legend(loc="best")
        plt.show()
        
        plt.axes([0,0,2,1.3])
        plt.plot(self.bestcost,'g',label="Cost(It)")
        plt.title("Cost(It)")
        plt.legend(loc="best")
        plt.show()                   
        
TSP = SA(20,1000,30,5000)
TSP.main()
