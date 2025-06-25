import "./App.css";

import { useState } from "react";
import Navbar from "./components/Navbar";
import Cuadro from "./components/Cuadro";
import ParametrosForm from "./components/ParametrosForm";

function App() {
  const [filas, setFilas] = useState([]); // ⬅️ Estado global para las filas simuladas

  // Función que se pasa al formulario
  const onSimulacionCompleta = (nuevasFilas) => {
    setFilas(nuevasFilas);
  };

  return (
    <>
      <Navbar />
      <div>
        {/* Le pasamos la función al formulario */}
        <ParametrosForm onSimulacionCompleta={onSimulacionCompleta} />
      </div>

      <h3>Tabla de simulación:</h3>

      {/* Le pasamos las filas al componente Cuadro */}
      <Cuadro filas={filas} />
    </>
  );
}

export default App;
