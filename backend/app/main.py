import random
from utilities import *
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS: permitir conexiones desde el frontend (localhost:5173 en desarrollo)

# Para poder runnear el back:
# uvicorn main:app --reload

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend en React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos esperado
class FormData(BaseModel):
    nombre: str
    edad: int

@app.get("/")
def read_root():
    return {"mensaje": "API funcionando correctamente"}


@app.post("/submit")
def recibir_form(data: FormData):
    return {"mensaje": f"Hola {data.nombre}, tenés {data.edad} años."}


C = 0
T = 2
R = random.uniform(100, 300)
print(f'Valor de R: {R}')
trayectoria, t_final = rungeKutta(funcionEDO, C, R)

print(f"Umbral R = {R:.2f} superado en t = {t_final} min")
    # Si quieres ver las primeras 5 iter:
for paso in trayectoria[:20]:
    print(paso)
    # Por ejemplo, para enviar al frontend:
import json
with open('rk4_trayectoria.json','w') as f:
        json.dump({
            'R (Valor uniforme)': R,
            't_final':     t_final,
            'trayectoria': trayectoria
        }, f, indent=2)