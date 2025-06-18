import math


def funcion_edo(c, t, x):
    # dR/dt = C + 0,2T + t^2
    # t asume el valor de x en nuestra EDO.
    # el parametro t es nuestro T en la EDO.
    # Tanto C como T son constantes que se definen en la función.
    # En este caso, C es la cantidad de personas en la cola que debemos observar en el vec estado.
    return c + 0,2*t + x**2


def nom_servidor(tipo):
    if tipo == 1:
        return "Envio de Paquete"
    return "Reclamaciones y Devoluciones"

def distribucion_uniforme(valor_inf, valor_sup, rnd):
    """
    Acá el enunciado no nos indica nada sobre el si R cambia exactamente para cada tipo de servidor, lo que tenemos
    es una distribución uniforme que va desde 100 a 300 que luego será utilizado para el calculo de Runge Kutta de 4to Orden.
    """
    return valor_inf + (rnd * (valor_sup - valor_inf))

def distribucion_exp_neg(mu, rnd):
    # mu = hace referencia a la media
    # rnd = el valor aleatorio.
    return -mu * math.log(1 - rnd)

class Servidor:
    def __init__(self, id, tipo, nombre, rnd, T, demora, hora_fin_atencion, estado):
        self.id = id
        self.tipo = tipo
        self.nombre = (nombre == nom_servidor(tipo))
        self.rnd = rnd # Falta poner la función para q me de un numero aleatorio acá jijo
        self.T = distribucion_uniforme(rnd)
        self.demora = demora # Falta hacer lo de runge kutta acá
        self.hora_fin_atencion = hora_fin_atencion
        self.estado = estado
    
class Cliente:
    def __init__(self, id, tipo_sv, estado, tiempo_llegada, inicio_atencion, fin_atencion):
        self.id = id
        self.tipo_sv = tipo_sv
        self.estado = estado
        self.tiempo_llegada = tiempo_llegada
        self.inicio_atencion = inicio_atencion
        self.fin_atencion = fin_atencion


def hs_a_min(mu, hs):
    """
    1 h -> 60 m
    n clientes
    """
    minutos = hs * 60
    return minutos/mu

def tipo_servicio(rnd):
    """
    Para el tipo de servicio se realizo una tabla de probabilidades ya que el enunciado indicaba que para Envio de Paquetes [1]
    cada uno de los empleados tiene una tasa de servicio de 10 clientes p/ hora.
    Mientras que para Reclamaciones y devoluciones, un solo empleado con una tasa de servicio de 7 clientes p/ hora.
    """
    if 0.742 <= rnd <= 1.00:
        return 2
    return 1

def llegadaCliente(tipo_servicio, reloj, rnd):
    """
    Para la llegada del cliente necesitamos saber el valor actual del reloj, y un valor aleatorio para indicar cuando 
    llegará este, todo esto en base al tipo de servicio que tiene. Los calculos de la media son calculados mediante una regla
    de tres, ya que pasamos de Horas a Minutos :)
    """
    if tipo_servicio == 1: # Esto equivaldría a que estamos ante Envio de Paquetes
        mu = 25
        horas = 1
        media_de_cliente_por_min = hs_a_min(mu, horas)
        llegada = distribucion_exp_neg(media_de_cliente_por_min, rnd)
        return reloj + llegada 
    else:
        mu = 15
        horas = 1
        media_de_cliente_por_min = hs_a_min(mu, horas)
        llegada = distribucion_exp_neg(media_de_cliente_por_min, rnd)
        return reloj + llegada       
    

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
