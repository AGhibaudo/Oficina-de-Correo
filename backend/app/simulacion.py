import random
from copy import copy
from typing import List, Dict, Any
from models import Cliente, Servidor
from utilities import rungeKutta, funcionEDO, media_entre_llegadas, distribucion_exp_neg
import random
import math
import pandas as pd
from collections import deque
from datetime import timedelta


def minutos_a_hora_minuto(mins):
    return str(timedelta(minutes=round(mins)))

class SimuladorCorreo:
    def __init__(self, lineas, lim_inf_exp, lim_sup_exp, param_t):
        self.lineas = lineas
        self.lim_inf_exp = lim_inf_exp
        self.lim_sup_exp = lim_sup_exp
        self.param_t = param_t

        self.reloj = 0.0
        self.iteracion = 0
        self.cola = deque()
        # Acá debería ir inicializado todo lo que deberia estar en la primera linea del vector !!!!!!!!!!!!
        



