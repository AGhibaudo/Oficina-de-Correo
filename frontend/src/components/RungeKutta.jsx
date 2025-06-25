import React from "react";

export default function RungeKutta({ data }) {
  if (!data || data.length === 0) {
    return <p className="text-center mt-3">No hay datos de Runge–Kutta disponibles.</p>;
  }

  return (
    <div className="container my-4">
      <h4 className="mb-3">Evolución Runge–Kutta</h4>
      <div className="table-responsive">
        <table className="table table-bordered text-center">
          <thead className="table-light">
            <tr>
              <th>t</th>
              <th>R(t)</th>
            </tr>
          </thead>
          <tbody>
            {data.map((row, idx) => (
              <tr key={idx}>
                <td>{row.t}</td>
                <td>{row.R}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
