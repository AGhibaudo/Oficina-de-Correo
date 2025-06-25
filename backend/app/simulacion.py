import random
from copy import copy
from typing import List, Dict, Any
from models import Cliente, Servidor
from utilities import rungeKutta, funcionEDO, media_entre_llegadas, distribucion_exp_neg, generar_rnd, distribucion_uniforme, nom_servidor
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
        # ALan -> Crafteo de estadísticos.
        self.fin_atencion = [] # Acá agrega una lista que tiene {Tipo sv, hora_fin_atencion, id servidor, cliente, tiempo_atencion -> runge}
        self.contador_paquetes = 0
        self.contador_reclamos = 0


        r_comun = distribucion_uniforme(self.lim_inf_exp, self.lim_sup_exp, generar_rnd())
        # SERVIDORES
        #self.servidor_ep1 = [{'estado': 'LIBRE', 'R': distribucion_uniforme(lim_inf_exp, lim_sup_exp, generar_rnd()), 'cliente': None}]
        #self.servidor_ep2 = [{'estado': 'LIBRE', 'R': distribucion_uniforme(lim_inf_exp, lim_sup_exp, generar_rnd()), 'cliente': None, 't_remanente': 0.0} ]
        self.servidores_ep = [{'estado': 'LIBRE', 'R': r_comun, 'cliente': None} for _ in range(2)] 
        self.servidor_ryd = [{'estado': 'LIBRE', 'R': r_comun, 'cliente': None}]

        self.servidor_ep[2]['t_remanente'] = 0.0 # Manejo ambos servidores dentro de un for, pero al servidor_ep[2] le agrego el t remanente :)


        self.clientes = {}
        #T VIENE POR PARAMETRO
        # T | RND | VALOR DE R (100 0 300)| DEMORA DE AT | HORA FIN  
       # POR CADA UNO DE LOS TRES SERVIDORES !!!!!

        #T VIENE POR PARAMETRO
        #R SE CALCULA CON LIM INF Y SUP // esta un UTTILITIES
        #DEMORA ATENCION es la funcoin RK 
        self.rnd_serv_ep1 = None # Los voy a usar en función del [i] q ocupe en la iteración !!
        self.rnd_serv_ep2 = None # 
        self.rnd_serv_ryd = None

        self.hora_fin_serv_ep1 = float('inf') # Lo mismo para lo de arriba :)
        self.hora_fin_serv_ep2 = float('inf')
        self.hora_fin_serv_ryd = float('inf')

        # EN UTILIES -- distribucion_exp_neg(mu, rnd)
    

        #RND ! TIEMPO ENTRE ! PROXIMA LLEGADA {}
    def generar_llegada(self, mu):
      # DEVUELVE EL TIEMPO ENTRE 
      rnd = generar_rnd()
      tiempo = distribucion_exp_neg(mu, rnd)
      return {'rnd': rnd, 'dt': tiempo, 'hora': round(self.reloj + tiempo, 2)}
        

    def iniciar_atencion(self, tipo, cliente):
        duracion = None
        # Alan -> Esto es lo q interprete, tambien queda como lo de juli, pero lo que cambia es la utilización de nuestras funciones.
        # Aca tipo = 1 va a hacer referencia a Envio de Paquetes ! mientras que 2 hará referencia a Reclamos y Devoluciones.
        # Ahora esta en función a nuestras funciones definidas en utilities, tiene el mismo funcionamiento
        for i, servidor in enumerate(self.servidores_ep if tipo == 1 else self.servidor_ryd):
            if servidor['estado'] == 'LIBRE':
                servidor['estado'] = 'OCUPADO'
                servidor['cliente'] = cliente
                cliente.estado = 'SIENDO ATENDIDO'
                cliente.reloj_inicio = self.reloj
                cola = len(self.cola_ep if tipo == 1 else self.cola_ryd)
                duracion = rungeKutta(funcionEDO, cola, self.r_calc)
                fin = round(self.reloj + duracion, 2)
                cliente.reloj_fin = fin
                self.fin_atencion.append({'tipo': nom_servidor(tipo), 'fin': fin, 'id': i, 'cliente': cliente, 'rk': duracion})
                break
        else: 
            if tipo == 1:
                self.cola_ep.append(cliente)
            else:
                self.cola_ryd.append(cliente)
            cliente.estado = 'EN COLA'


    # Alan -> Esto debería quedar igual que el de juli, no deberia modificar mucho, ta todo check igual revisen
    # info extra seria para las columnas dinamicas
    def registrar_estado(self, evento, info_extra):
        # Esto es para la columna de eventos :)
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
            #'serv_ep1': self.servidor_ep1[0]['estado'],
            #'serv_ep2': self.servidor_ep2[1]['estado'],
            # Con el cambio puesto de los servidores en un for si andaria con indices, antes estaba mal
            'serv_ep1': self.servidores_ep[0]['estado'],
            'serv_ep2': self.servidores_ep[1]['estado'],
            'serv_ryd': self.servidor_ryd[0]['estado'],
        }
        # Alan -> Falta hacer esta parte, que es cambiar los eventos en MAyus por los q usamos nosotros !
        for e in self.fin_atencion:
            # esto seria el sv que lo esta atendiendo
            col_id = e['id']
            # aca hay que arreglar el tema del rk
            if e['tipo'] == 'PAQUETE':
                fila[f'rnd_fin_p{col_id+1}'] = round(random.uniform(0, 0.99), 2)
                fila[f'rk_fin_p{col_id+1}'] = e['rk']
                fila[f'fin_p{col_id+1}'] = e['fin']
            elif e['tipo'] == 'RECLAMO':
                fila['rnd_fin_r1'] = round(random.uniform(0, 0.99), 2)
                fila['rk_fin_r1'] = e['rk']
                fila['fin_r1'] = e['fin']

        for nombre, cliente in self.clientes.items():
            fila[nombre] = cliente.estado
        fila.update(info_extra)
        self.vector_estado.append(fila)
        
    # Una vez revisado esto, hay q hacer la función de ejecutar la simulación         


