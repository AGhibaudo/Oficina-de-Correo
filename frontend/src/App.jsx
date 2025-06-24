import "./App.css";

import Navbar from "./components/Navbar";
import CuadroCabecera from "./components/CuadroCabecera";
import CuadroFilas from "./components/CuadroFilas";
import Cuadro from "./components/Cuadro";
import ParametrosForm from "./components/ParametrosForm";

function App() {
  return (
    <>
  
      <Navbar />
      <div>
        <ParametrosForm />
      </div>
      <h3>Tabla de simulación: </h3>
      <Cuadro/>
     
    </>
  );
}

export default App;
