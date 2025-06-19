import random
from utilities import *


# C = 5
# T = 2
# R = random.uniform(100, 300)
# print(f'Valor de R: {R}')
# trayectoria, t_final = rungeKutta(funcionEDO, C, R)

# print(f"Umbral R = {R:.2f} superado en t = {t_final} min")
#     # Si quieres ver las primeras 5 iter:
# for paso in trayectoria[:5]:
#     print(paso)
#     # Por ejemplo, para enviar al frontend:
# import json
# with open('rk4_trayectoria.json','w') as f:
#         json.dump({
#             'R (Valor uniforme)': R,
#             't_final':     t_final,
#             'trayectoria': trayectoria
#         }, f, indent=2)