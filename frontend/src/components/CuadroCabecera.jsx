import React from "react";

function CuadroCabecera() {
  return (
    <thead>
      <tr>
        <th colSpan={4}></th>
        <th colSpan={6} className="table-dark">SERVICIOS</th>
        <th colSpan={2}></th>
        <th colSpan={10} className="table-success">SERVIDORES ENVIO DE PAQUETES</th>
        <th colSpan={5} className="table-danger">SERVIDOR RECLAMOS Y DEVOLUCIONES</th>
      </tr>

      <tr>
        <th colSpan={2}></th>
        <th colSpan={2} className="table-primary">NECESIDAD DEL TIPO SERVICIO</th>
        <th colSpan={3} className="table-success">LLEGADA DE CLIENTE PARA ENVIO DE PAQUETE</th>
        <th colSpan={3} className="table-danger">LLEGADA DE CLIENTE PARA RECLAMOS Y DEVOLUCIONES</th>
        <th colSpan={2}></th>
        <th colSpan={5} className="table-dark">EMPLEADO 1</th>
        <th colSpan={5} className="table-dark">EMPLEADO 2</th>
        <th colSpan={5} className="table-dark">EMPLEADO 1</th>
        <th colSpan={6} className="table-primary">VARIABLES PARA ESTADISTICAS</th>
        <th colSpan={7} className="table-warning">CLIENTE</th>
      </tr>

      <tr>
        <th className="table-warning">RELOJ</th>
        <th className="table-warning">EVENTO</th>
        <th className="table-dark">RND</th>
        <th className="table-secondary">SERVICIO</th>
        <th className="table-dark">RND</th>
        <th className="table-secondary">TIEMPO ENTRE LLEGADAS</th>
        <th className="table-secondary">HORA DE PROXIMA LLEGADA</th>
        <th className="table-dark">RND</th>
        <th className="table-secondary">TIEMPO ENTRE LLEGADAS</th>
        <th className="table-secondary">HORA DE PROXIMA LLEGADA</th>
        <th className="table-success">COLA EDP</th>
        <th className="table-danger">COLA RYD</th>
        <th className="table-dark">RND</th>
        <th className="table-secondary">VARIABLE T</th>
        <th className="table-secondary">DEMORA DE ATENCION</th>
        <th className="table-secondary">HORA FIN DE ATENCION</th>
        <th className="table-secondary">ESTADO</th>
        <th className="table-dark">RND</th>
        <th className="table-secondary">VARIABLE T</th>
        <th className="table-secondary">DEMORA DE ATENCION</th>
        <th className="table-secondary">HORA FIN DE ATENCION</th>
        <th className="table-secondary">ESTADO</th>
        <th className="table-dark">RND</th>
        <th className="table-secondary">VARIABLE T</th>
        <th className="table-secondary">DEMORA DE ATENCION</th>
        <th className="table-secondary">HORA FIN DE ATENCION</th>
        <th className="table-secondary">ESTADO</th>
        <th className="table-secondary">TIEMPO DE ESPERA ACUMULADO SERVICIO 1</th>
        <th className="table-secondary">TIEMPO DE ESPERA ACUMULADO SERVICIO 2</th>
        <th className="table-secondary">TIEMPO DE ATENCION ACUMULADO SERVICIO 1</th>
        <th className="table-secondary">TIEMPO DE ATENCION ACUMULADO SERVICIO 2</th>
        <th className="table-secondary">CANTIDAD DE CLIENTES ATENDIDOS POR EL SERVICIO 1</th>
        <th className="table-secondary">CANTIDAD DE CLIENTES ATENDIDOS POR EL SERVICIO 2</th>
        <th>ID</th>
        <th>TIPO</th>
        <th>ESTADO</th>
        <th>TIEMPO DE LLEGADA</th>
        <th>INICIO DE ATENCION</th>
        <th>FIN DE ATENCION</th>
      </tr>
    </thead>
  );
}

export default CuadroCabecera;
