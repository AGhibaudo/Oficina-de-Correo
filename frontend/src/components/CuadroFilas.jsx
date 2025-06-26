import React, { useState } from "react";

function CuadroFilas({ filas }) {
  const [filaSeleccionada, setFilaSeleccionada] = useState(null);

  const handleClick = (index) => {
    setFilaSeleccionada(prev => prev === index ? null : index)
  };

  return (
    <tbody>
      {filas.map((fila, index) => (
        <tr
          key={index}
          onClick={() => handleClick(index)}
          className={index === filaSeleccionada ? "fila-seleccionada table-danger" : ""}
          style={{ cursor: "pointer" }}
        >
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
// import React, { useState } from "react";
// import ModalRK from "./ModalRK";

// function CuadroFilas({ filas }) {
//   const [mostrarModal, setMostrarModal] = useState(false);
//   const [datosRK, setDatosRK] = useState(null);

//   const handleRKClick = (valorRK, fila) => {
//     // Esta función puede consultar al backend o usar datos dummy
//     // Suponiendo que ya tenés un campo fila._detalleRK_P1 o similar
//     const detalle = fila._detalleRK || []; // o adaptá al campo que uses
//     setDatosRK(detalle);
//     setMostrarModal(true);
//   };

//   return (
//     <>
//       <tbody>
//         {filas.map((fila, index) => (
//           <tr key={index}>
//             {Object.entries(fila).map(([key, valor], j) => {
//               let stickyClass = "";
//               if (j === 0) stickyClass = "sticky-col";
//               if (j === 1) stickyClass = "sticky-col-2";
//               if (j === 2) stickyClass = "sticky-col-3";

//               const esRK = key.includes("RK_");

//               return (
//                 <td
//                   key={j}
//                   className={stickyClass}
//                   style={{ cursor: esRK ? "pointer" : "default", color: esRK ? "blue" : "black" }}
//                   onClick={() => esRK && handleRKClick(valor, fila)}
//                 >
//                   {valor}
//                 </td>
//               );
//             })}
//           </tr>
//         ))}
//       </tbody>

//       <ModalRK show={mostrarModal} onClose={() => setMostrarModal(false)} datosRK={datosRK} />
//     </>
//   );
// }

// export default CuadroFilas;
