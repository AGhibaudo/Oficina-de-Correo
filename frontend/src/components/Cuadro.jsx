import React from "react";
import CuadroCabecera from "./CuadroCabecera";
import CuadroFilas from "./CuadroFilas";
const filas = [
    {
      reloj: "0:00",
      evento: "nombre de evento",
  
      rnd_servicio: "0",
      servicio: "nombre de servicio",
  
      rnd_llegada_para_edp: "0",
      tiempo_entre_llegadas_edp: "0:00",
      hora_de_proxima_llegada_edp: "0:00",
  
      rnd_llegada_para_ryd: "0",
      tiempo_entre_llegadas_ryd: "0:00",
      hora_de_proxima_llegada_ryd: "0:00",
  
      cola_edp: "0",
      cola_ryd: "0",
  
      rnd_edp_e1: "0",
      variable_t_edp_e1: "0:00",
      demora_de_atencion_e1: "0:00",
      hora_fin_de_atencion_e1: "0:00",
      estado_e1: "estado", 
  
      rnd_edp_e2: "0",
      variable_t_edp_e2: "0:00",
      demora_de_atencion_e2: "0:00",
      hora_fin_de_atencion_e2: "0:00",
      estado_e2: "estado", 
  
      rnd_ryd_e1: "0",
      variable_t_ryd_e1: "0:00",
      demora_de_atencion_e3: "0:00",
      hora_fin_de_atencion_e3: "0:00",
      estado_e3: "estado",
      
      tiempo_espera_acumulado_s1: "0:00",
      tiempo_espera_acumulado_s2: "0:00",
      tiempo_atencion_acumulado_s1: "0:00",
      tiempo_atencion_acumulado_s2: "0:00",
      cantidad_clientes_atendidos_s1: "0", 
      cantidad_clientes_atendidos_s2: "0",
      
      id_cliente: "0", 
      tipo_cliente: "tipo cliente",
      estado_cliente: "estado cliente",
      tiempo_llegada_cliente: "0:00", 
      inicio_atencion_cliente: "0:00", 
      fin_atencion_cliente: "0:00",
    },
  ];

  function Cuadro() {
    // para que queren fijas 3 primeras filas de datos al scrollear
    const filasFijas = filas.slice(0, 3);       // primeras 3 filas
    const filasRestantes = filas.slice(3);      // el resto
    return (
    
        <div className="container-fluid px-0">
        <div className="table-responsive table-container">
          <table className="table table-bordered border-dark text-center mb-0">
            <CuadroCabecera />
  
            <thead className="filas-fijas">
              {filasFijas.map((fila, i) => (
                <tr key={`fija-${i}`}>
                  {Object.values(fila).map((valor, j) => (
                    <td key={j}>{valor}</td>
                  ))}
                </tr>
              ))}
            </thead>
  
            <CuadroFilas filas={filasRestantes} />
          </table>
        </div>
      </div>
    );
  }
export default Cuadro