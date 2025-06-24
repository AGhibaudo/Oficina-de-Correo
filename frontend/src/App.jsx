import "./App.css";

import Navbar from "./components/Navbar";
import CuadroCabecera from "./components/CuadroCabecera";
import CuadroFilas from "./components/CuadroFilas";
import Cuadro from "./components/Cuadro";
import ParametrosForm from "./components/ParametrosForm";

function App() {
  return (
    <>
    <div>
        <h1>Simulación de Inscripción — Parámetros</h1>
        <ParametrosForm />
      </div>
    {/* <section className="intro"> */}
      <Navbar />
      <Cuadro/>
      {/* <div className="h-100"> */}
        
      {/* </div> */}
    {/* </section> */}
    </>
  );
}

export default App;
