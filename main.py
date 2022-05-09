class Asiento:
    def __init__(self,color, precio,registro):
        self.color = color
        self.presio = precio
        self.registro = registro
    def cambiarColor(self, color):
        if color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco":
            self.color=color
       
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):
        for i in range(len(self.asientos)):
            if self.asientos[i]!=None:
                Auto.cantidadCreados=Auto.cantidadCreados+1
    def verificarIntegridad(self):
        for i in range(len(self.asientos)):
            if self.asientos[i]!=None:
                if self.asientos[i].registro==self.motor.registro:
                    continue
                else:
                    return "Las piezas no sonoriginales"
        if self.registro==self.motor.registro:
            return "Auto original"
class Motor:
    def __init__(self, numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo =tipo
    if __name__ == "__main__":
        a1 = Asiento("blanco", 5000, 435)
        a2 = Asiento("blanco", 5000, 435)
      
        a1.cambiarColor("naranja")
        a2.cambiarColor("verde")
      
        ok = False
      
        if(a1.color == "blanco" and a2.color == "verde"):
             ok = True
        print(ok)