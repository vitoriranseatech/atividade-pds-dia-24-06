# importando a biblioteca nupy 
import numpy as np
from abc import ABC, abstractmethod 

#classe base veiculo com metodo abstrato calcular_custo 
class veiculo (ABC):
    @abstractmethod
    def calcular_custo(salf,distancia):
        pass
    
# Subclasse Carro
class carro(veiculo):
    def calcular_custo(self,distancia):
        return distancia * 0.5 #exemplo: custo de R$0,50 por km
        
#Subclasse Bicicleta 
class Bicicleta(veiculo):
    def calcular_custo (self, distancia):
        return distancia * 0.1 #exemplo: custo de R$0,10 pr km
        
#Subclasse Caminhao 
class Caminhao(veiculo):
    def calcular_custo(self, distancia):
        return distancia * 1.0 #exemplo: custo de R$1,00 por km
        
#Criando uma lista de veiculos 
veiculos = [carro(), Bicicleta(), Caminhao()]
distancia = 200 #exemplo de distancia 

#calculando os custos usando polimorfismo e armazenamento em um array numpy 
custos = np.array([veiculo.calcular_custo(distancia) for veiculo in veiculos])

#exibido os resultados 
print("custos de viagem para cada veiculo:", custos)
print("custos total da viagem", np.sum(custos))