import json

class Concesionaria():
    def __init__(self) -> None:
        self.stock_autos = []
        self.autos_disponibles = Auto.mostrar_caracteristicas

    def leer_archivos_json(self,ruta,modo):
        with open (ruta,modo) as archivo:
            lista_autos = json.load(archivo)["autos"]
        return lista_autos
    
    def recorrer_lista(self,lista_autos):
        for auto in lista_autos:
            color = auto.get("color")
            marca = auto.get("marca")
            auto_disponible = Auto(color,marca)
            self.stock_autos.append(auto_disponible)    
            
    def mostrar_autos_disponibles(self):
        for auto in self.stock_autos:
            caracteristicas = self.autos_disponibles(auto)
            print(caracteristicas)

class Auto():
    def __init__(self,color_auto,marca_auto) -> None:
        self.color = color_auto
        self.marca = marca_auto
    
    def mostrar_caracteristicas(self):
        return(f"La marca es{self.marca} y el color es {self.color}")


PATH = "./SEMANA 11/Poo_practica/"
informacion_autos = Concesionaria()
lista_autos = informacion_autos.leer_archivos_json(f"{PATH}modelos_autos.json", "r")
informacion_autos.recorrer_lista(lista_autos)
informacion_autos.mostrar_autos_disponibles()




