import React from "react";

function CuadroCabecera() {
  return (
    <thead>
      <tr>
        <th colSpan={3} className="sticky-col"></th>
        <th colSpan={6} className="table-dark">SERVICIOS</th>
        <th colSpan={2}></th>
        <th colSpan={6} className="table-success">SERVIDORES ENVIO DE PAQUETES</th>
        <th colSpan={3} className="table-danger">SERVIDOR RECLAMOS Y DEVOLUCIONES</th>
        <th colSpan={6} className="table-primary">VARIABLES PARA ESTADISTICAS</th>

      </tr>

      <tr>
        <th colSpan={3} className="sticky-col"></th>

        <th colSpan={3} className="table-success">LLEGADA DE CLIENTE A ENVIO DE PAQUETE</th>
        <th colSpan={3} className="table-danger">LLEGADA DE CLIENTE A RECLAMOS Y DEVOLUCIONES</th>
        <th colSpan={2}></th>
        <th colSpan={3} className="table-dark">EMPLEADO 1</th>
        <th colSpan={3} className="table-dark">EMPLEADO 2</th>
        <th colSpan={3} className="table-dark">EMPLEADO 1</th>
        <th colSpan={3} className="table-primary">SERVIDOR 1</th>
        <th colSpan={3} className="table-primary">SERVIDOR 2</th>

        <th colSpan={7} className="table-warning">CLIENTE</th>
      </tr>

      <tr>
      <th className="table-warning sticky-col">IT</th>
        <th className="table-warning sticky-col">RELOJ</th>
        <th className="table-warning sticky-col-2">EVENTO</th>

        <th className="table-dark sticky-col-3">RND</th>
        <th className="table-secondary sticky-col-4">TMPO ENTRE LLEG</th>
        <th className="table-secondary">PROX LLEG</th>

        <th className="table-dark">RND</th>
        <th className="table-secondary">TMPO ENTRE LLEG</th>
        <th className="table-secondary">PROX LLEG</th>

        <th className="table-success">COLA PAQ</th>
        <th className="table-danger">COLA REC</th>

        <th className="table-dark">RND</th>
        <th className="table-secondary">RK</th>
        <th className="table-secondary">FIN AT</th>

        <th className="table-dark">RND</th>
        <th className="table-secondary">RK</th>
        <th className="table-secondary">FIN AT</th>

        <th className="table-dark">RND</th>
        <th className="table-secondary">RK</th>
        <th className="table-secondary">FIN AT</th>

        <th className="table-secondary">ESTADO</th>
        <th className="table-secondary">ESTADO</th>
        <th className="table-secondary">ESTADO</th>
        <th className="table-dark">RND</th>
        <th className="table-secondary">VARIABLE T</th>
        <th className="table-secondary">DEMORA DE ATENCION</th>
        <th className="table-secondary">HORA FIN DE ATENCION</th>
        <th className="table-secondary">ESTADO</th>
        <th className="table-secondary">TMPO ESPERA ACUM </th>
        <th className="table-secondary">TMPO ATENCION ACUM</th>
        <th className="table-secondary">CANT CLIENTES ATENDIDOS</th>
        <th className="table-secondary">TMPO ESPERA ACUM</th>
        <th className="table-secondary">TMPO ATENCION ACUM</th>
        <th className="table-secondary">CANT CLIENTES ATENDIDOS</th>
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
