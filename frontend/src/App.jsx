import "./App.css";
import ParametrosForm from "./components/ParametrosForm";



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

function App() {
  return (
    
    <section className="intro">
      <div>
        <h1>Simulación de Inscripción — Parámetros</h1>
        <ParametrosForm />
      </div>
      <div className="h-100">
        <div className="mask d-flex align-items-center h-100">
          <div className="container">
            <div className="row justify-content-center">
              <div className="col-12">
                <div className="table-responsive bg-white">
                  <table className="table table-bordered border-dark mb-0 mt-5 text-center">
                    <thead>
                      <tr>
                        <th scope="col" colSpan={4}></th>
                        <th scope="col" colSpan={6} className="table-dark">SERVICIOS</th>
                        <th scope="col" colSpan={2}></th>
                        <th scope="col" colSpan={10} className="table-success">SERVIDORES ENVIO DE PAQUETES</th>
                          <th scope="col" colSpan={5} className="table-danger">SERVIDOR RECLAMOS Y DEVOLUCIONES</th>
                      </tr>

                      <tr>
                        <th scope="col" colSpan={2}></th>
                        <th scope="col" colSpan={2} className="table-primary">NECESIDAD DEL TIPO SERVICIO</th>
                        <th scope="col" colSpan={3} className="table-success">LLEGADA DE CLIENTE PARA ENVIO DE PAQUETE</th>
                        <th scope="col" colSpan={3} className="table-danger">LLEGADA DE CLIENTE PARA RECLAMOS Y DEVOLUCIONES</th>
                        <th scope="col" colSpan={2}></th>

                        <th scope="col" colSpan={5} className="table-dark">EMPLEADO 1</th>

                        <th scope="col" colSpan={5} className="table-dark">EMPLEADO 2</th>

                        <th scope="col" colSpan={5} className="table-dark">EMPLEADO 1</th>

                        <th scope="col" colSpan={6} className="table-primary">VARIABLES PARA ESTADISTICAS</th>

                        <th scope="col" colSpan={7} className="table-warning">CLIENTE</th>
                      </tr>

                      <tr>
                        <th scope="col" className="table-warning">RELOJ</th>
                        <th scope="col" className="table-warning">EVENTO</th>
                        <th scope="col" className="table-dark">RND</th>
                        <th scope="col" className="table-secondary" >SERVICIO</th>
                        <th scope="col" className="table-dark">RND</th>
                        <th scope="col" className="table-secondary">TIEMPO ENTRE LLEGADAS</th>
                        <th scope="col" className="table-secondary">HORA DE PROXIMA LLEGADA</th>
                        <th scope="col" className="table-dark">RND</th>
                        <th scope="col" className="table-secondary">TIEMPO ENTRE LLEGADAS</th>
                        <th scope="col" className="table-secondary">HORA DE PROXIMA LLEGADA</th>
                        <th scope="col" className="table-success">COLA EDP</th>
                        <th scope="col" className="table-danger">COLA RYD</th>

                        <th scope="col" className="table-dark">RND</th>
                        <th scope="col" className="table-secondary">VARIABLE T</th>
                        <th scope="col" className="table-secondary">DEMORA DE ATENCION</th>
                        <th scope="col" className="table-secondary">HORA FIN DE ATENCION</th>
                        <th scope="col" className="table-secondary">ESTADO</th>

                        <th scope="col" className="table-dark">RND</th>
                        <th scope="col" className="table-secondary">VARIABLE T</th>
                        <th scope="col" className="table-secondary">DEMORA DE ATENCION</th>
                        <th scope="col" className="table-secondary">HORA FIN DE ATENCION</th>
                        <th scope="col" className="table-secondary">ESTADO</th>

                        <th scope="col" className="table-dark">RND</th>
                        <th scope="col" className="table-secondary">VARIABLE T</th>
                        <th scope="col" className="table-secondary">DEMORA DE ATENCION</th>
                        <th scope="col" className="table-secondary">HORA FIN DE ATENCION</th>
                        <th scope="col" className="table-secondary">ESTADO</th>

                        <th scope="col" className="table-secondary">TIEMPO DE ESPERA ACUMULADO SERVICIO 1</th>
                        <th scope="col" className="table-secondary">TIEMPO DE ESPERA ACUMULADO SERVICIO 2</th>
                        <th scope="col" className="table-secondary">TIEMPO DE ATENCION ACUMULADO SERVICIO 1</th>
                        <th scope="col" className="table-secondary">TIEMPO DE ATENCION ACUMULADO SERVICIO 2</th>
                        <th scope="col" className="table-secondary">CANTIDAD DE CLIENTES ATENDIDOS POR EL SERVICIO 1</th>
                        <th scope="col" className="table-secondary">CANTIDAD DE CLIENTES ATENDIDOS POR EL SERVICIO 2</th>
                        
                        <th scope="col">ID</th>
                        <th scope="col">TIPO</th>
                        <th scope="col">ESTADO</th>
                        <th scope="col">TIEMPO DE LLEGADA</th>
                        <th scope="col">INICIO DE ATENCION</th>
                        <th scope="col">FIN DE ATENCION</th>
                      </tr>
                    </thead>
                    <tbody>
                    {filas.map((fila, index) => (
                      <tr key={index}>
                        {/* RELOJ Y EVENTO */}
                        <td>{fila.reloj}</td>
                        <td>{fila.evento}</td>

                        {/* NECESIDAD DEL TIPO SERVICIO */}
                        <td>{fila.rnd_servicio}</td>
                        <td>{fila.servicio}</td>

                        {/* LLEGADA CLIENTE EDP */}
                        <td>{fila.rnd_llegada_para_edp}</td>
                        <td>{fila.tiempo_entre_llegadas_edp}</td>
                        <td>{fila.hora_de_proxima_llegada_edp}</td>

                        {/* LLEGADA CLIENTE RYD */}
                        <td>{fila.rnd_llegada_para_ryd}</td>
                        <td>{fila.tiempo_entre_llegadas_ryd}</td>
                        <td>{fila.hora_de_proxima_llegada_ryd}</td>

                        {/* COLAS */}
                        <td>{fila.cola_edp}</td>
                        <td>{fila.cola_ryd}</td>

                        {/* EMPLEADO 1 (EDP) */}
                        <td>{fila.rnd_edp_e1}</td>
                        <td>{fila.variable_t_edp_e1}</td>
                        <td>{fila.demora_de_atencion_e1}</td>
                        <td>{fila.hora_fin_de_atencion_e1}</td>
                        <td>{fila.estado_e1}</td>

                        {/* EMPLEADO 2 (EDP) */}
                        <td>{fila.rnd_edp_e2}</td>
                        <td>{fila.variable_t_edp_e2}</td>
                        <td>{fila.demora_de_atencion_e2}</td>
                        <td>{fila.hora_fin_de_atencion_e2}</td>
                        <td>{fila.estado_e2}</td>

                        {/* EMPLEADO 1 (RYD) */}
                        <td>{fila.rnd_ryd_e1}</td>
                        <td>{fila.variable_t_ryd_e1}</td>
                        <td>{fila.demora_de_atencion_e3}</td>
                        <td>{fila.hora_fin_de_atencion_e3}</td>
                        <td>{fila.estado_e3}</td>

                        {/* VARIABLES PARA ESTADÍSTICAS */}
                        <td>{fila.tiempo_espera_acumulado_s1}</td>
                        <td>{fila.tiempo_espera_acumulado_s2}</td>
                        <td>{fila.tiempo_atencion_acumulado_s1}</td>
                        <td>{fila.tiempo_atencion_acumulado_s2}</td>
                        <td>{fila.cantidad_clientes_atendidos_s1}</td>
                        <td>{fila.cantidad_clientes_atendidos_s2}</td>

                        {/* CLIENTE */}
                        <td>{fila.id_cliente}</td>
                        <td>{fila.tipo_cliente}</td>
                        <td>{fila.estado_cliente}</td>
                        <td>{fila.tiempo_llegada_cliente}</td>
                        <td>{fila.inicio_atencion_cliente}</td>
                        <td>{fila.fin_atencion_cliente}</td>
                      </tr>
                    ))}
                  </tbody>

                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default App;
