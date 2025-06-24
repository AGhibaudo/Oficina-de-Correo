// src/components/ParametrosForm.jsx
import React, { useState } from "react";

export default function ParametrosForm() {
  const [lineas, setLineas] = useState(100);
  const [limInf, setLimInf] = useState("");
  const [limSup, setLimSup] = useState("");
  const [paramT, setParamT] = useState("");
  const [respuesta, setRespuesta] = useState(null);
  const [error, setError] = useState(null);

  const opcionesLineas = [
    { value: 100, label: "100" },
    { value: 1000, label: "1 000" },
    { value: 50000, label: "50 000" },
    { value: 10000000, label: "10 000 000" },
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setRespuesta(null);

    // Validaciones básicas en front
    if (!limInf || !limSup || !paramT) {
      setError("Todos los campos son obligatorios.");
      return;
    }
    if (Number(limInf) >= Number(limSup)) {
      setError("El límite inferior debe ser menor que el superior.");
      return;
    }

    try {
      const res = await fetch("http://localhost:8000/parametros", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          lineas: Number(lineas),
          limInfExpertizEmpleado: Number(limInf),
          limSupExpertizEmpleado: Number(limSup),
          parametroT: parseFloat(paramT),
        }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Error en servidor");
      setRespuesta(data);
    } catch (err) {
      console.error(err);
      setError(err.message);
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: "auto", padding: 20 }}>
      <h2>Parámetros de Simulación</h2>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: 12 }}>
          <label>Líneas a simular:</label>
          <select
            value={lineas}
            onChange={(e) => setLineas(e.target.value)}
            style={{ marginLeft: 8 }}
          >
            {opcionesLineas.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </select>
        </div>

        <div style={{ marginBottom: 12 }}>
          <label>Límite Inferior Expertiz:</label>
          <input
            type="number"
            value={limInf}
            onChange={(e) => setLimInf(e.target.value)}
            placeholder="p.ej. 1"
            style={{ marginLeft: 8, width: "100%" }}
            required
          />
        </div>

        <div style={{ marginBottom: 12 }}>
          <label>Límite Superior Expertiz:</label>
          <input
            type="number"
            value={limSup}
            onChange={(e) => setLimSup(e.target.value)}
            placeholder="p.ej. 10"
            style={{ marginLeft: 8, width: "100%" }}
            required
          />
        </div>

        <div style={{ marginBottom: 12 }}>
          <label>Parámetro T (Runge-Kutta):</label>
          <input
            type="number"
            step="0.01"
            value={paramT}
            onChange={(e) => setParamT(e.target.value)}
            placeholder="p.ej. 0.5"
            style={{ marginLeft: 8, width: "100%" }}
            required
          />
        </div>

        <button type="submit">Enviar Parámetros</button>
      </form>

      {error && (
        <div style={{ marginTop: 16, color: "crimson" }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {respuesta && (
        <div style={{ marginTop: 16, whiteSpace: "pre-wrap" }}>
          <strong>Respuesta del backend:</strong>
          <div>{respuesta.mensaje}</div>
        </div>
      )}
    </div>
  );
}
