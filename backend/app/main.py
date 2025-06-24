import random
from utilities import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import HTTPException


app = FastAPI()

# CORS: permitir conexiones desde el frontend (localhost:5173 en desarrollo)

# Para poder runnear el back:
# tienen q tener la dependencia -> pip install uvicorn !!!!!!!!!!!
# uvicorn main:app --reload -> Parense en app !!!

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend en React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos esperado
class FormParametros(BaseModel):
    lineas: int
    limInfExpertizEmpleado: int
    limSupExpertizEmpleado: int
    parametroT: float
    """
    Acá puse más o menos los parámetros que se supone que debería poder modificar el usuario
    Lineas a simular: Faltaría hacer la validación en el Forms que sea de: 100, 1000, 50000, 10000000 corte desplegable.
    Limite inferior expertiz del empleado: Indica q tan malo es definiendo un limite para la Distr. Uniforme.
    Lim Superior expertiz del empleado: Indica q tan bueno es definiendo el máximo de capacidad que este puede tener para la Distr. Uniforme.
    parametro T: Esté parámetro es una cte para poder realizar Runge Kutta de 4to orden.
    """

app.state.form_params: FormParametros | None = None

"""
Enpoints Definidos
"""
@app.get("/")
def read_root():
    return {"mensaje": "API funcionando correctamente, ntu al netimanid"}

@app.post("/parametros")
async def recibir_form(data: FormParametros):
    app.state.form_params = data
    return {"ok": True, "message": "Parámetros recibidos con exito!"} 

@app.get("/parametros")
async def obtener_forms_params():
    if app.state.form_params is None:
        raise HTTPException(404, detail="Aún no se enviaron parámetros")
    return app.state.form_params

# C = 0
# T = 2
# R = random.uniform(100, 300)
# print(f'Valor de R: {R}')
# trayectoria, t_final = rungeKutta(funcionEDO, C, R)

# print(f"Umbral R = {R:.2f} superado en t = {t_final} min")
#     # Si quieres ver las primeras 5 iter:
# for paso in trayectoria[:20]:
#     print(paso)
#     # Por ejemplo, para enviar al frontend:
# import json
# with open('rk4_trayectoria.json','w') as f:
#         json.dump({
#             'R (Valor uniforme)': R,
#             't_final':     t_final,
#             'trayectoria': trayectoria
#         }, f, indent=2)