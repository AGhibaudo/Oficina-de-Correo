
def funcionEDO(c, t, x):
    # dR/dt = C + 0,2T + t^2
    # t asume el valor de x en nuestra EDO.
    # el parametro t es nuestro T en la EDO.
    # Tanto C como T son constantes que se definen en la función.
    # En este caso, C es la cantidad de personas en la cola que debemos observar en el vec estado.
    funcionValuada = c + 0,2*t + x**2
    return funcionValuada

class Cliente:
    def __init__(self, id, tipo, estado, tiempoLlegada, inicioAtencion, finAtencion):
        self.id = id
        self.tipo = tipo
        self.estado = estado
        self.tiempoLlegada = tiempoLlegada
        self.inicioAtencion = inicioAtencion
        self.finAtencion = finAtencion

class ServidorEnvio:
    def __init__(self, id, rnd, tUniforme, demora, horaFinAtencion, estado):
        self.id = id
        self.rnd = rnd
        self.tUniforme = tUniforme
        self.demora = demora
        self.horaFinAtencion = horaFinAtencion
        self.estado = estado

class ServidorReclamos:
    def __init__(self, id, rnd, tUniforme, demora, horaFinAtencion, estado):
        self.id = id
        self.rnd = rnd
        self.tUniforme = tUniforme
        self.demora = demora
        self.horaFinAtencion = horaFinAtencion
        self.estado = estado

def rungeKutta(f, x0, y0, h, n):
    """
    Runge-Kutta method for solving ordinary differential equations.
    
    Parameters:
    f : function - la función definida por la EDO
    x0 : float - valor de x
    y0 : float - valor de y
    h : float - tamaño del salto.
    n : int - cant de saltos.
    
    devuelve:
    Una lista de tuplas (x, y) representa la solución en cada paso
    """
    a, rnd, b, t = 0, 0, 0, 0
    C = 0 # Cantidad de personas en la cola.
    T = 0
    R = a + rnd(b-a)
    result = [(x0, y0)]
    for i in range(n):
        k1 = h * f()
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)
        
        y_next = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_next = x0 + h
        
        result.append((x_next, y_next)) 
        
        x0, y0 = x_next, y_next
    
    return result



def tiempoEntreLlegadas(t1, t2):
    pass

def tiempoEsperaAcum():
    pass

def tiempoUsoServidorEnvioAcum():
    pass

def tiempoUsoServidorReclamosAcum():
    pass


def vectorEstado():
    pass