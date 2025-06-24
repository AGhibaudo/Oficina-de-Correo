import React from "react";

function CuadroFilas({ filas }) {
    return (
        <tbody>
            {/* {filas.map((fila, index) => (
        <tr key={index}>
          <td>{fila.reloj}</td>
          <td>{fila.evento}</td>
          <td>{fila.rnd_servicio}</td>
          <td>{fila.servicio}</td>
          <td>{fila.rnd_llegada_para_edp}</td>
          <td>{fila.tiempo_entre_llegadas_edp}</td>
          <td>{fila.hora_de_proxima_llegada_edp}</td>
          <td>{fila.rnd_llegada_para_ryd}</td>
          <td>{fila.tiempo_entre_llegadas_ryd}</td>
          <td>{fila.hora_de_proxima_llegada_ryd}</td>
          <td>{fila.cola_edp}</td>
          <td>{fila.cola_ryd}</td>
          <td>{fila.rnd_edp_e1}</td>
          <td>{fila.variable_t_edp_e1}</td>
          <td>{fila.demora_de_atencion_e1}</td>
          <td>{fila.hora_fin_de_atencion_e1}</td>
          <td>{fila.estado_e1}</td>
          <td>{fila.rnd_edp_e2}</td>
          <td>{fila.variable_t_edp_e2}</td>
          <td>{fila.demora_de_atencion_e2}</td>
          <td>{fila.hora_fin_de_atencion_e2}</td>
          <td>{fila.estado_e2}</td>
          <td>{fila.rnd_ryd_e1}</td>
          <td>{fila.variable_t_ryd_e1}</td>
          <td>{fila.demora_de_atencion_e3}</td>
          <td>{fila.hora_fin_de_atencion_e3}</td>
          <td>{fila.estado_e3}</td>
          <td>{fila.tiempo_espera_acumulado_s1}</td>
          <td>{fila.tiempo_espera_acumulado_s2}</td>
          <td>{fila.tiempo_atencion_acumulado_s1}</td>
          <td>{fila.tiempo_atencion_acumulado_s2}</td>
          <td>{fila.cantidad_clientes_atendidos_s1}</td>
          <td>{fila.cantidad_clientes_atendidos_s2}</td>
          <td>{fila.id_cliente}</td>
          <td>{fila.tipo_cliente}</td>
          <td>{fila.estado_cliente}</td>
          <td>{fila.tiempo_llegada_cliente}</td>
          <td>{fila.inicio_atencion_cliente}</td>
          <td>{fila.fin_atencion_cliente}</td>
        </tr> 
 ))} */}

            {filas.map((fila, index) => (
                // <tr key={index}>
                //     {Object.values(fila).map((valor, j) => (
                //         <td key={j}>{valor}</td>
                //     ))}
                // </tr>
                <tr key={index}>
                    {Object.entries(fila).map(([key, valor], j) => {
                        let stickyClass = "";
                        if (j === 0) stickyClass = "sticky-col";
                        if (j === 1) stickyClass = "sticky-col-2";
                        if (j === 2) stickyClass = "sticky-col-3";

                        return (
                            <td key={j} className={stickyClass}>
                                {valor}
                            </td>
                        );
                    })}
                </tr>
            ))}




        </tbody>
    );
}

export default CuadroFilas;
