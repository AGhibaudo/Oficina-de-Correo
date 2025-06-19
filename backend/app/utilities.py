import math

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
    def __init__(self, id, tipo, nombre, T, rnd, R, demora, hora_fin_atencion, estado):
        self.id = id
        self.tipo = tipo
        self.nombre = nombre
        self.T = T # Este parámetro es fijo según lo detallado con el profe ["A mi criterio podríamos poner q sea un parámetro que ingrese el usuario - Alan"]
        self.rnd = rnd # Falta poner la función para q me de un numero aleatorio acá jijo
        self.R = R # R hace referencia a una distribución uniforme de la velocidad de tiempo de atención.
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
    return round(minutos/mu, 2)


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
    if tipo_servicio == 1: # Esto equivaldría a que estamos ante Envío de Paquetes
        mu = 25
        horas = 1
        media_de_cliente_por_min = hs_a_min(mu, horas)
        llegada = distribucion_exp_neg(media_de_cliente_por_min, rnd)
        return reloj + llegada 
    else: # Esto equivaldría a que estamos ante un Reclamo o Devolución. 
        mu = 15
        horas = 1
        media_de_cliente_por_min = hs_a_min(mu, horas)
        llegada = distribucion_exp_neg(media_de_cliente_por_min, rnd)
        return reloj + llegada       


def funcionEDO(C, T, t):
    """
    Detalles de los parámetros de la función:
    C: Cantidad de clientes en la cola en ese instante es decir vec_estado.cola_sv[i]
    T: Parámetro constante - (Sigo sosteniendo que el usuario lo podría cambiar como param pero seguiría siendo cte)
    t: Equivale al tiempo, que de nuestro runge kutta, haría referencia a "x"
    """
    return C + 0.2*T + t**2


def rungeKutta(f, C, R):
    h = 1 # Por enunciado contemplamos que el salto se realiza cada 1 minuto.
    T = 2 # Para mi T puede ser un parámetro configurable x el usr.
    """
    Para integrar dR/dt = f(C, T, t) con R(0) = 0 -> Condición inicial
    si tenemos q guardar (t, R) -> (x, y) en cada iteración hasta que nuestro R 
    actual supere al por parámetro para conseguir el valor de t
    """
    vec_rk4 = []
    R_act = 0.00
    t = 0.00
    while R_act <= R:
        vec_rk4.append({'t': round(t, 4), 'R': round(R_act, 4)})

        # Coeficientes
        k1 = f(C, T, t)
        k2 = f(C, T, t + h/2)
        k3 = f(C, T, t + h/2)
        k4 = f(C, T, t + h)

        # Incremento de R (y)
        delta_R = (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        R_act += delta_R
        t += h

    vec_rk4.append({'t': round(t, 4), 'R': round(R_act, 4)})
    return vec_rk4, round(t, 4)

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
