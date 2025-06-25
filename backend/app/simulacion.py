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
        self.vector_estado = []

        # INICIALIZACION COLAS
        self.cola_ep = deque()
        self.cola_ryd = deque()
       
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

        self.r_comun, self.rnd = distribucion_uniforme(self.lim_inf_exp, self.lim_sup_exp, generar_rnd())
        # SERVIDORES
        
        # self.servidores_ep = [{'estado': 'LIBRE', 'rnd': self.rnd, 'R': self.r_comun, 'cliente': None} for _ in range(2)] 
        # self.servidor_ryd = [{'estado': 'LIBRE', 'rnd': self.rnd,'R': self.r_comun, 'cliente': None}]
        self.servidores_ep = [{'estado': 'LIBRE', 'R': self.r_comun, 'cliente': None} for _ in range(2)] 
        self.servidor_ryd = [{'estado': 'LIBRE', 'R': self.r_comun, 'cliente': None}]
        self.servidores_ep[1]['t_remanente'] = 0.0 # Manejo ambos servidores dentro de un for, pero al servidor_ep[2] le agrego el t remanente :)


 # VER VER 
        self.llegada_cli_ep = self.generar_llegada(25)
        self.llegada_cli_ryd = self.generar_llegada(15)
        # self.llegada_cli_ep = None
        # self.llegada_cli_ryd = None
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

        self.registrar_estado('INICIO', {})

        # EN UTILIES -- distribucion_exp_neg(mu, rnd)
    

        #RND ! TIEMPO ENTRE ! PROXIMA LLEGADA {}
    def generar_llegada(self, mu):
      # DEVUELVE EL TIEMPO ENTRE 
      rnd = generar_rnd()
      print(rnd)
      tiempo = distribucion_exp_neg(mu, rnd)
      return {'rnd': rnd, 'dt': tiempo, 'hora': round(self.reloj + tiempo, 2)}
        

    def iniciar_atencion(self, tipo, cliente):
        duracion = None
        vector_kutta = None
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
                vector_kutta, duracion = rungeKutta(funcionEDO, cola, self.r_comun)
                fin = round(self.reloj + duracion, 2)
                cliente.reloj_fin = fin
                # self.fin_atencion.append({'tipo': nom_servidor(tipo), 'fin': fin, 'id': i, 'cliente': cliente, 'rnd': servidor['rnd'],'rk': duracion})
                rnd = generar_rnd()

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
           
            'serv_ep1': self.servidores_ep[0]['estado'],
            'serv_ep2': self.servidores_ep[1]['estado'],
            'serv_ryd': self.servidor_ryd[0]['estado'],
        }
        # Alan -> Falta hacer esta parte, que es cambiar los eventos en MAyus por los q usamos nosotros !
        for e in self.fin_atencion:
            # esto seria el sv que lo esta atendiendo
            col_id = e['id']
            # aca hay que arreglar el tema del rk
            if e['tipo'] == 'ENVIO_PAQUETES':
                # Alan -> creo q lo solucione i guess.
                fila[f'rnd_fin_ep{col_id+1}'] = e['rnd']
                fila[f'rk_fin_ep{col_id+1}'] = e['rk']
                fila[f'fin_ep{col_id+1}'] = e['fin']
            elif e['tipo'] == 'RECLAMOS_Y_DEVOLUCIONES':
                fila['rnd_fin_ryd'] = e['rnd']
                fila['rk_fin_ryd'] = e['rk']
                fila['fin_ryd'] = e['fin']

        for nombre, cliente in self.clientes.items():
            fila[nombre] = cliente.estado
        fila.update(info_extra)
        self.vector_estado.append(fila)
        
    def ejecutar(self):
        while self.iteracion < self.lineas:
            eventos = [
                ('Llegada_EnvPaq', self.llegada_cli_ep['hora']),
                ('Llegada_RecYDev', self.llegada_cli_ryd['hora'])
            ] + [(f'FIN_{e["tipo"]}_{e["cliente"].nombre()}', e['fin']) for e in self.fin_atencion]
            # print(eventos)

            evento, instante = min(eventos, key=lambda x: x[1])
            # print("holaholaholaholaholahoalhoalhoalhoahlaohlo")
            # print(evento, instante)
            self.reloj = instante 
            info_extra = {}
            
            if evento == 'Llegada_EnvPaq' and self.reloj == self.llegada_cli_ep['hora']:
                self.contador_paquetes += 1
                cliente = Cliente('PAQ_', self.contador_paquetes)
                cliente.reloj_llegada = self.reloj
                nombre = cliente.nombre()
                self.clientes[nombre] = cliente
                self.llegada_cli_ep = self.generar_llegada(25)
                self.iniciar_atencion(1, cliente)
            
            elif evento == 'Llegada_RecYDev' and self.reloj == self.llegada_cli_ryd['hora']:
                self.contador_reclamos += 1
                cliente = Cliente('REC_', self.contador_reclamos)
                cliente.reloj_llegada = self.reloj
                nombre = cliente.nombre()
                self.clientes[nombre] = cliente
                self.llegada_cli_ryd = self.generar_llegada(15)
                self.iniciar_atencion(2, cliente)

            elif evento.startswith('FIN_ENVIO_PAQUETES'):
                id = int(evento.split('_')[4])
                cliente_nombre = '_'.join(evento.split('_')[3:])
                servidor = self.servidores_ep[id]
                servidor['estado'] = 'LIBRE'
                cliente = servidor['cliente']
                if cliente:
                    cliente.estado = 'FINALIZADO'
                servidor['cliente'] = None
                self.fin_atencion = [f for f in self.fin_atencion if not (f['tipo'] == 'ENVIO_PAQUETES' and f['id'] == id)] 
                # self.fin_atencion = [f for f in self.fin_atencion
                #                      if not (f['tipo'] == "ENVIO_PAQUETES" and f['cliente'].nombre() == cliente_nombre)]
                if self.cola_ep:
                    nuevo = self.cola_ep.popleft()
                    self.iniciar_atencion(1, nuevo)           

            elif evento.startswith('FIN_RECLAMOS_Y_DEVOLUCIONES'):
                servidor = self.servidor_ryd[0]
                cliente = servidor['cliente']
                servidor['estado'] = 'LIBRE'
                if cliente:
                    cliente.estado = "FINALIZADO"
                    servidor['cliente'] = None
                
                # print('antes', self.fin_atencion[0].nombre())
                
                self.fin_atencion = [f for f in self.fin_atencion if f['tipo'] != "RECLAMOS_Y_DEVOLUCIONES"]
                # self.fin_atencion = [f for f in self.fin_atencion
                #                      if not (f['tipo'] == "RECLAMOS_Y_DEVOLUCIONES" and f['cliente'].nombre() == cliente_nombre)]
                # print('despues', self.fin_atencion[0].nombre())


                if self.cola_ryd:
                    nuevo = self.cola_ryd.popleft()
                    self.iniciar_atencion(2, nuevo)
                    
            # print(f'Iter {self.iteracion} | Evento: {evento} | Reloj: {self.reloj}')
            self.registrar_estado(evento, info_extra)
            print(f'Iter {self.iteracion} | Evento: {evento} | Reloj: {self.reloj}')
            # print(f'Fin_atencion: {[e["cliente"].nombre() for e in self.fin_atencion]}')


            self.iteracion += 1
        df = pd.DataFrame(self.vector_estado)
        return df


    # Una vez revisado esto, hay q hacer la función de ejecutar la simulación         

