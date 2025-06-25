# import random
# from copy import copy
# from typing import List, Dict, Any
# from backend.app.models import Cliente, Servidor
# from utilities import rungeKutta, funcionEDO


# def run_simulation(params):
#     filas = []
#     base = {"iter": 0, "reloj": 0.0, "cola": 0, "en_servicio": 0}
#     filas.append(base)
#     active_clients: dict[int, Cliente] = {}
#     # Creas también tu pool de servidores (por ejemplo 2 EDP y 1 RYD):
#     servidores: dict[str, Servidor] = {
#       "edp_e1": Servidor(id_servidor="edp_e1", rnd=0, variable_t=0, demora_de_atencion=0, hora_fin_de_atencion=0, estado="LIBRE"),
#       "edp_e2": Servidor(id_servidor="edp_e2", rnd=0, variable_t=0, demora_de_atencion=0, hora_fin_de_atencion=0, estado="LIBRE"),
#       "ryd_e1": Servidor(id_servidor="ryd_e1", rnd=0, variable_t=0, demora_de_atencion=0, hora_fin_de_atencion=0, estado="LIBRE"),
#     }

#     for i in range(1, params.lineas + 1):
#         prev = filas[-1]
#         fila = copy(prev)
#         fila["iter"] = i
#         # 1) Avanzo el reloj (placeholder)
#         fila["reloj"] = round(prev["reloj"] + random.random(), 2)

#         # 2) Lógica de llegadas y active_clients…
#         #    (creas Cliente(...), lo guardas en active_clients,
#         #     luego `fila.update(cliente.to_row())`).

#         # 3) Lógica de servicio:
#         #    Para cada servidor libre u ocupado:
#         sid = "edp_e1"
#         srv = servidores[sid]
#         srv.rnd = random.random()
#         srv.variable_t = params.parametroT
#         srv.demora_de_atencion = rungeKutta(funcionEDO(), 0, )       # cálculo Runge–Kutta, expo, etc.
#         srv.hora_fin_de_atencion = srv.demora_de_atencion + fila["reloj"]
#         srv.estado = "OCUPADO" or "LIBRE"
#         fila.update(srv.to_row())

#         # 4) Estadísticas acumuladas si quieres (tiempo_espera_acumulado_s1…)
#         fila["tiempo_espera_acumulado_s1"] = 0
#         fila["tiempo_atencion_acumulado_s1"] = 0
#         fila["cantidad_clientes_atendidos_s1"] = 0

#         # 5) Finalmente, si algún cliente sale:
#         #    cliente.fin_atencion_cliente = fila["reloj"]
#         #    fila.update(cliente.to_row())
#         #    del active_clients[cliente.id_cliente]

#         # 6) Actualizo colas y servidores ocupados
#         fila["cola"] = len(active_clients)
#         fila["en_servicio"] = sum(1 for c in active_clients.values() if c.inicio_atencion_cliente is not None)

#         filas.append(fila)

#     return filas

 
 
import random
from copy import copy
from typing import List, Dict, Any
from backend.app.models import Cliente, Servidor
from utilities import rungeKutta, funcionEDO, media_entre_llegadas, distribucion_exp_neg
import random
import math
import pandas as pd
from collections import deque
from datetime import timedelta


# def run_simulation(params):
#     filas = []
#     base = {"iter": 0, "reloj": 0.0, "cola": 0, "en_servicio": 0}
#     filas.append(base)
#     active_clients: dict[int, Cliente] = {}
#     # Creas también tu pool de servidores (por ejemplo 2 EDP y 1 RYD):
#     servidores: dict[str, Servidor] = {
#       "edp_e1": Servidor(id_servidor="edp_e1", rnd=0, variable_t=0, demora_de_atencion=0, hora_fin_de_atencion=0, estado="LIBRE"),
#       "edp_e2": Servidor(id_servidor="edp_e2", rnd=0, variable_t=0, demora_de_atencion=0, hora_fin_de_atencion=0, estado="LIBRE"),
#       "ryd_e1": Servidor(id_servidor="ryd_e1", rnd=0, variable_t=0, demora_de_atencion=0, hora_fin_de_atencion=0, estado="LIBRE"),
#     }

#     for i in range(1, params.lineas + 1):
#         prev = filas[-1]
#         fila = copy(prev)
#         fila["iter"] = i
#         # 1) Avanzo el reloj (placeholder)
#         fila["reloj"] = round(prev["reloj"] + random.random(), 2)

#         # 2) Lógica de llegadas y active_clients…
#         #    (creas Cliente(...), lo guardas en active_clients,
#         #     luego `fila.update(cliente.to_row())`).

#         # 3) Lógica de servicio:
#         #    Para cada servidor libre u ocupado:
#         sid = "edp_e1"
#         srv = servidores[sid]
#         srv.rnd = random.random()
#         srv.variable_t = params.parametroT
#         srv.demora_de_atencion = rungeKutta(funcionEDO(), 0, )       # cálculo Runge–Kutta, expo, etc.
#         srv.hora_fin_de_atencion = srv.demora_de_atencion + fila["reloj"]
#         srv.estado = "OCUPADO" or "LIBRE"
#         fila.update(srv.to_row())

#         # 4) Estadísticas acumuladas si quieres (tiempo_espera_acumulado_s1…)
#         fila["tiempo_espera_acumulado_s1"] = 0
#         fila["tiempo_atencion_acumulado_s1"] = 0
#         fila["cantidad_clientes_atendidos_s1"] = 0

#         # 5) Finalmente, si algún cliente sale:
#         #    cliente.fin_atencion_cliente = fila["reloj"]
#         #    fila.update(cliente.to_row())
#         #    del active_clients[cliente.id_cliente]

#         # 6) Actualizo colas y servidores ocupados
#         fila["cola"] = len(active_clients)
#         fila["en_servicio"] = sum(1 for c in active_clients.values() if c.inicio_atencion_cliente is not None)

#         filas.append(fila)

#     return filas

def minutos_a_hora_minuto(mins):
    return str(timedelta(minutes=round(mins)))

class SimuladorCorreo:
    def __init__(self, lineas, lim_inf_exp, lim_sup_exp, param_t):
        self.lineas = lineas 
        self.lim_inf_exp = lim_inf_exp
        self.lim_sup_exp = lim_sup_exp
        self.reloj = 0.0
        self.iteracion = 0
        self.clientes = []
        self.id_cliente = 1

        self.estado_servicio = {
            1: [{'estado': 'LIBRE', 'R': 100, 'tiempo_espera': 0, 'tiempo_atencion': 0, 'atendidos': 0} for _ in range(2)],
            2: [{'estado': 'LIBRE', 'R': 300, 'tiempo_espera': 0, 'tiempo_atencion': 0, 'atendidos': 0}]
        }

        self.colas = {1: deque(), 2: deque()}

        self.prox_llegada = 0.0
        self.rnd_llegada = None
        self.dt_llegada = None
        for tipo in [1, 2]:
            self._generar_proxima_llegada(tipo)

        self.prox_fin = {(1, 0): float('inf'), (1, 1): float('inf'), (2, 0): float('inf')}
        self.vector_estado = []

    def _generar_proxima_llegada(self, tipo_servicio):
        tasa = 25 if tipo_servicio == 1 else 15
        media = media_entre_llegadas(tasa)
        rnd = round(random.uniform(0, 0.99), 2)
        dt = distribucion_exp_neg(media, rnd) #este seria tiempo prox llegada
        self.rnd_llegada[tipo_servicio] = rnd
        self.dt_llegada[tipo_servicio] = dt
        self.prox_llegada[tipo_servicio] = round(self.reloj + dt, 2) #aca te hace la hora de prox llegada

    def ejecutar(self):
        while self.iteracion < self.lineas:
            eventos = {('LLEGADA', tipo): tiempo for tipo, tiempo in self.prox_llegada.items()}
            eventos.update({('FIN', (tipo, idx)): tiempo for (tipo, idx), tiempo in self.prox_fin.items()})
            (evento, detalle), t_evento = min(eventos.items(), key=lambda x: x[1])
            self.reloj = round(t_evento, 2)

            fila = {
                "reloj": minutos_a_hora_minuto(self.reloj),
                "evento": f"{evento}_{detalle}",
                "rnd_servicio": "-",
                "servicio": "-",
                "rnd_llegada_para_edp": self.rnd_llegada.get(1, "-"),
                "tiempo_entre_llegadas_edp": minutos_a_hora_minuto(self.dt_llegada.get(1, 0)),
                "hora_de_proxima_llegada_edp": minutos_a_hora_minuto(self.prox_llegada.get(1, 0)),
                "rnd_llegada_para_ryd": self.rnd_llegada.get(2, "-"),
                "tiempo_entre_llegadas_ryd": minutos_a_hora_minuto(self.dt_llegada.get(2, 0)),
                "hora_de_proxima_llegada_ryd": minutos_a_hora_minuto(self.prox_llegada.get(2, 0)),
                "cola_edp": len(self.colas[1]),
                "cola_ryd": len(self.colas[2]),
                "rnd_edp_e1": "-",
                "variable_t_edp_e1": "-",
                "demora_de_atencion_e1": "-",
                "hora_fin_de_atencion_e1": "-",
                "estado_e1": self.estado_servicio[1][0]['estado'],
                "rnd_edp_e2": "-",
                "variable_t_edp_e2": "-",
                "demora_de_atencion_e2": "-",
                "hora_fin_de_atencion_e2": "-",
                "estado_e2": self.estado_servicio[1][1]['estado'],
                "rnd_ryd_e1": "-",
                "variable_t_ryd_e1": "-",
                "demora_de_atencion_e3": "-",
                "hora_fin_de_atencion_e3": "-",
                "estado_e3": self.estado_servicio[2][0]['estado'],
                "tiempo_espera_acumulado_s1": minutos_a_hora_minuto(sum(s['tiempo_espera'] for s in self.estado_servicio[1])),
                "tiempo_atencion_acumulado_s1": minutos_a_hora_minuto(sum(s['tiempo_atencion'] for s in self.estado_servicio[1])),
                "cantidad_clientes_atendidos_s1": sum(s['atendidos'] for s in self.estado_servicio[1]),
                "tiempo_espera_acumulado_s2": minutos_a_hora_minuto(self.estado_servicio[2][0]['tiempo_espera']),
                "tiempo_atencion_acumulado_s2": minutos_a_hora_minuto(self.estado_servicio[2][0]['tiempo_atencion']),
                "cantidad_clientes_atendidos_s2": self.estado_servicio[2][0]['atendidos'],
                "id_cliente": "-", "tipo_cliente": "-", "estado_cliente": "-",
                "tiempo_llegada_cliente": "-", "inicio_atencion_cliente": "-", "fin_atencion_cliente": "-"
            }

            self.vector_estado.append(fila)
            self.iteracion += 1

        return pd.DataFrame(self.vector_estado)


sim = SimuladorCorreo(tiempo_limite=30, max_iteraciones=5)
df_resultado = sim.ejecutar()
df_resultado.head()
