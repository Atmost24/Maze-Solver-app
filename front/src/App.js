import "./App.css";
import { useState } from "react";
import axios from "axios";
import Canvas from "./Components/Canvas";
import BasicTable from "./Components/BasicTable";
var statistics=[];

function App() {
	const route = "http://127.0.0.1:8000/classic";
	var url;
	const [selectedFile, setState] = useState(null);
	const [option, setOption] = useState("deep");
	const [response, setResponse] = useState(null);
	const [imagevalue, setImageValue] = useState(null);
	const [limitValue, setlimitValue] = useState(2);
	

	const addOption = (val) => {
		setOption(val.target.value);
		console.log(val.target.value);
	};
	const onFileChange = (e) => {
		setState(e.target.files[0]);
	};

	const addLimit = (e) => {
		setlimitValue(e.target.value);
	};

	const cipher = () => {
		const formData = new FormData();
		formData.append("file", selectedFile);
		var par={}
		if (option === "deep") {
			url = route + "/profundidad";
		} else if (option === "breadth") {
			url = route + "/anchura";
		} else if (option === "iterative") {
			url = route + "/profundidad_iterativa";
			par={limit:limitValue}
		} else if (option === "uniform") {
			url = route + "/busqueda_uniforme";
		} else if (option === "greedy") {
			url = route + "/greedy";
		} else {
			url = route + "/a";
		}

		axios.post(url, formData,{ params: par}).then((response) => {
			console.log(response.data);
			statistics.push({"alg":response.data.alg,"shape":response.data.shape,
							"time":response.data.time,"memory":response.data.memory
				});
			if (response.data.flag){
				setImageValue(response.data.filedata)
			}else {
				setImageValue(null)
			}
			console.log(statistics);
			setResponse(response.data);
			
		});
	};

	return (
		<div className="App">
			<header className="App-header">
				<h1>Maze Solver</h1>
				
				<div className="fila">
					<div className="element">
						<h5>Selecciona el archivo</h5>
						<input type="file" onChange={onFileChange}  />
					</div>
					<div className="element"> 
					<h5 className="fw-bold mb-0" >Algoritmo</h5>
					<select onChange={addOption} className="form-select" name="option_encrypt">
						<option value="deep" selected="">
							Deep
						</option>
						<option value="breadth">Breadth</option>
						<option value="iterative" selected="">
							Iterative
						</option>
						<option value="uniform">Uniform</option>
						<option value="greedy" selected="">
							Greedy
						</option>
						<option value="A*">A*</option>
					</select>
					
					</div>
					<div className="element">
						{option==="iterative"  && <h5 >Limite de iteración</h5> }
						{option==="iterative"&& <input onchange={addLimit} value="2" type="number" min="1"></input>}
					</div>
					
					
				</div>
				<div className="Boton" onClick={cipher}>Iniciar Busqueda!</div>
			
				{response != null && <BasicTable rows={statistics}></BasicTable>}
				<h4>Solucion</h4>
				{response != null && <Canvas style={{maxWidth:"800px",maxHeight:"800px"}} props={response}></Canvas>}
				{imagevalue != null && <h4>Grafo</h4>}
				{imagevalue != null && <h6>d: ir abajo; u: ir arriba ; l: ir a izquierda; r: ir a derecha </h6>}
				{imagevalue != null && <img style={{maxWidth:"800px",maxHeight:"1200px"}} src={imagevalue}></img>} 
				

				
			</header>
		</div>
	);
}

export default App;
