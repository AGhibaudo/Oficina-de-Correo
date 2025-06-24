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
    <div className="container my-4">
      <h2 className="text-center mb-4">Parámetros de Simulación</h2>
      <form
        onSubmit={handleSubmit}
        className="mx-auto row row-cols-1 row-cols-md-2 g-3"
        style={{ maxWidth: "600px" }}
      >
        <div className="col-12">
          <label className="form-label">Líneas a simular:</label>
          <select
            className="form-select"
            value={lineas}
            onChange={(e) => setLineas(e.target.value)}
          >
            {opcionesLineas.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </select>
        </div>

        <div className="col-12">
          <label className="form-label">Límite Inferior Expertiz:</label>
          <input
            type="number"
            className="form-control"
            value={limInf}
            onChange={(e) => setLimInf(e.target.value)}
            placeholder="p.ej. 1"
            required
          />
        </div>

        <div className="col-12">
          <label className="form-label">Límite Superior Expertiz:</label>
          <input
            type="number"
            className="form-control"
            value={limSup}
            onChange={(e) => setLimSup(e.target.value)}
            placeholder="p.ej. 10"
            required
          />
        </div>

        <div className="col-12">
          <label className="form-label">Parámetro T (Runge-Kutta):</label>
          <input
            type="number"
            step="0.01"
            className="form-control"
            value={paramT}
            onChange={(e) => setParamT(e.target.value)}
            placeholder="p.ej. 0.5"
            required
          />
        </div>

        <div className="col-12 text-center">
          <button type="submit" className="btn btn-primary mt-3 px-5">
            Enviar Parámetros
          </button>
        </div>

        {error && (
          <div className="col-12 alert alert-danger mt-2 text-center">
            <strong>Error:</strong> {error}
          </div>
        )}

        {respuesta && (
          <div className="col-12 alert alert-success mt-2 text-center">
            <strong>Respuesta del backend:</strong>
            <div>{respuesta.mensaje}</div>
          </div>
        )}
      </form>
    </div>
  );
}
