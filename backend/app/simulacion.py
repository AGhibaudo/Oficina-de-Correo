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


class Cliente:
    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id
        self.estado = 'EN SISTEMA'
        self.reloj_llegada = None
        self.reloj_inicio = None
        self.reloj_fin = None

    def nombre(self):
        return f'{self.tipo}{self.id}'



class SimuladorCorreo:
    def __init__(self, lineas, lim_inf_exp, lim_sup_exp, param_t):
        self.lineas = lineas
        self.lim_inf_exp = lim_inf_exp
        self.lim_sup_exp = lim_sup_exp
        self.param_t = param_t

        # PRIMERAS COLUMNAS
        self.reloj = 0.0
        self.iteracion = 0

        # INICIALIZACION COLAS
        self.cola_ep = deque()
        self.cola_ryd = deque()
        # cada cola tiene: 

        # # LLEGADA CLIENTES ENVIOS Y PAQUETES
        # self.rnd_llegada_ep = None
        # # self.dist_llegada_ep = None
        # self.tiempo_entre_lleg_cli_ep = 0.0
        # self.tiempo_prox_lleg_cli_ep = 0.0

        # # LLEGADA CLIENTES RECLAMOS Y DEV
        # self.rnd_llegada_ryd = None
        # # self.dist_llegada_ryd = None
        # self.tiempo_entre_lleg_cliente_ryd = 0.0
        # self.tiempo_prox_lleg_cliente_ryd = 0.0

        # VER VER 
        self.llegada_cli_ep = self.generar_llegada(25)
        self.llegada_cli_ryd = self.generar_llegada(15)
        self.registrar_estado('INICIO', {})

        # ESTADISTICOS
        self.acum_espera_ep = 0
        self.acum_espera_ryd = 0
        self.cont_clientes_atendidos_ep = 0
        self.cont_clientes_atendidos_ryd = 0
        self.acum_uso_ryd = 0
        self.acum_uso_ryd = 0

        # SERVIDORES
        self.servidor_ep1 = [{'estado': 'LIBRE', 'R': 100, 'cliente': None}]
        self.servidor_ep2 = [{'estado': 'LIBRE', 'R': 100, 'cliente': None, 'tmpo_remanente': 0.0} ]
        self.servidor_ryd = [{'estado': 'LIBRE', 'R': 100, 'cliente': None}]

        self.clientes = {}
        #T VIENE POR PARAMETRO
        # T | RND | VALOR DE R (100 0 300)| DEMORA DE AT | HORA FIN  
       # POR CADA UNO DE LOS TRES SERVIDORES !!!!!

        #T VIENE POR PARAMETRO
        #R SE CALCULA CON LIM INF Y SUP // esta un UTTILITIES
        #DEMORA ATENCION es la funcoin RK 
        self.rnd_serv_ep1 = None
        self.rnd_serv_ep2 = None
        self.rnd_serv_ryd = None

        self.hora_fin_serv_ep1 = float('inf')
        self.hora_fin_serv_ep2 = float('inf')
        self.hora_fin_serv_ryd = float('inf')

        # EN UTILIES -- distribucion_exp_neg(mu, rnd)

        #RND ! TIEMPO ENTRE ! PROXIMA LLEGADA {}
    def generar_llegada(self, mu):
      rnd = round(random.uniform(0, 0.99), 2)
      # DEVUELVE EL TIEMPO ENTRE 
      tiempo = distribucion_exp_neg(mu, rnd)
      return {'rnd': rnd, 'dt': tiempo, 'hora': round(self.reloj + tiempo, 2)}
        

    # def iniciar_atencion(self, tipo, cliente):
    #     duracion = None
    #     for i, servidor in enumerate(self.servidores_paquetes if tipo == 'PAQUETE' else self.servidores_reclamos):
    #         if servidor['estado'] == 'LIBRE':
    #             servidor['estado'] = 'OCUPADO'
    #             servidor['cliente'] = cliente
    #             cliente.estado = 'SIENDO ATENDIDO'
    #             cliente.reloj_inicio = self.reloj
    #             C = len(self.cola_paquetes if tipo == 'PAQUETE' else self.cola_reclamos)
    #             duracion = rungeKutta(servidor['R'], self.reloj, C)
    #             fin = round(self.reloj + duracion, 2)
    #             cliente.reloj_fin = fin
    #             self.fin_atencion.append({'tipo': tipo, 'fin': fin, 'id': i, 'cliente': cliente, 'rk': duracion})
    #             break
    #     else:
    #         if tipo == 'PAQUETE':
    #             self.cola_paquetes.append(cliente)
    #         else:
    #             self.cola_reclamos.append(cliente)
    #         cliente.estado = 'EN COLA'


    def registrar_estado(self, evento, info_extra):
        fila = {
            'ITERACION': self.iteracion + 1,
            'RELOJ': round(self.reloj, 2),
            'EVENTO': evento,
            'rnd_lleg_ep': self.llegada_cli_ep['rnd'],
            'tiempo_entre_lleg_ep': self.llegada_cli_ep['dt'],
            'prox_lleg_ep': self.llegada_cli_ep['hora'],
            'rnd_lleg_ryd': self.llegada_cli_ryd['rnd'],
            'tiempo_entre_lleg_ryd': self.llegada_cli_ryd['dt'],
            'prox_lleg_ryd': self.llegada_cli_ryd['hora'],
            'cola_ep': len(self.cola_ep),
            'cola_ryd': len(self.cola_ryd),

            'rnd_serv_ep1': '-',
            'rk_ep1': '-',
            'hora_fin_serv_ep1': '-',

            'rnd_serv_ep2': '-',
            'rk_ep2': '-',
            'hora_fin_serv_ep2': '-',

            'rnd_serv_ryd': '-',
            'rk_ryd': '-',
            'hora_fin_serv_ryd': '-',
            'serv_ep1': self.servidor_ep1[0]['estado'],
            'serv_ep2': self.servidor_ep2[1]['estado'],
            'serv_ryd': self.servidor_ryd[0]['estado'],
        }

        # for e in self.fin_atencion:
        #     col_id = e['id']
        #     if e['tipo'] == 'PAQUETE':
        #         fila[f'RND_FIN_P{col_id+1}'] = round(random.uniform(0, 0.99), 2)
        #         fila[f'RK_FIN_P{col_id+1}'] = e['rk']
        #         fila[f'FIN_P{col_id+1}'] = e['fin']
        #     elif e['tipo'] == 'RECLAMO':
        #         fila['RND_FIN_R1'] = round(random.uniform(0, 0.99), 2)
        #         fila['RK_FIN_R1'] = e['rk']
        #         fila['FIN_R1'] = e['fin']

        # for nombre, cliente in self.clientes.items():
        #     fila[nombre] = cliente.estado
        # fila.update(info_extra)
        # self.vector_estado.append(fila)
        
        


