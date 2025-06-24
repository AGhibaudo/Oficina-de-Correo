import random
from copy import copy
from typing import List, Dict, Any
from backend.app.models import Cliente, Servidor
from utilities import rungeKutta, funcionEDO


def run_simulation(params):
    filas = []
    base = {"iter": 0, "reloj": 0.0, "cola": 0, "en_servicio": 0}
    filas.append(base)
    active_clients: dict[int, Cliente] = {}
    # Creas también tu pool de servidores (por ejemplo 2 EDP y 1 RYD):
    servidores: dict[str, Servidor] = {
      "edp_e1": Servidor(id_servidor="edp_e1", rnd=0, variable_t=0, demora_de_atencion=0, hora_fin_de_atencion=0, estado="LIBRE"),
      "edp_e2": Servidor(id_servidor="edp_e2", rnd=0, variable_t=0, demora_de_atencion=0, hora_fin_de_atencion=0, estado="LIBRE"),
      "ryd_e1": Servidor(id_servidor="ryd_e1", rnd=0, variable_t=0, demora_de_atencion=0, hora_fin_de_atencion=0, estado="LIBRE"),
    }

    for i in range(1, params.lineas + 1):
        prev = filas[-1]
        fila = copy(prev)
        fila["iter"] = i
        # 1) Avanzo el reloj (placeholder)
        fila["reloj"] = round(prev["reloj"] + random.random(), 2)

        # 2) Lógica de llegadas y active_clients…
        #    (creas Cliente(...), lo guardas en active_clients,
        #     luego `fila.update(cliente.to_row())`).

        # 3) Lógica de servicio:
        #    Para cada servidor libre u ocupado:
        sid = "edp_e1"
        srv = servidores[sid]
        srv.rnd = random.random()
        srv.variable_t = params.parametroT
        srv.demora_de_atencion = rungeKutta(funcionEDO(), 0, )       # cálculo Runge–Kutta, expo, etc.
        srv.hora_fin_de_atencion = srv.demora_de_atencion + fila["reloj"]
        srv.estado = "OCUPADO" or "LIBRE"
        fila.update(srv.to_row())

        # 4) Estadísticas acumuladas si quieres (tiempo_espera_acumulado_s1…)
        fila["tiempo_espera_acumulado_s1"] = 0
        fila["tiempo_atencion_acumulado_s1"] = 0
        fila["cantidad_clientes_atendidos_s1"] = 0

        # 5) Finalmente, si algún cliente sale:
        #    cliente.fin_atencion_cliente = fila["reloj"]
        #    fila.update(cliente.to_row())
        #    del active_clients[cliente.id_cliente]

        # 6) Actualizo colas y servidores ocupados
        fila["cola"] = len(active_clients)
        fila["en_servicio"] = sum(1 for c in active_clients.values() if c.inicio_atencion_cliente is not None)

        filas.append(fila)

    return filas