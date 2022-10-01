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
	
	

	const addOption = (val) => {
		setOption(val.target.value);
		console.log(val.target.value);
	};
	const onFileChange = (e) => {
		setState(e.target.files[0]);
	};

	const cipher = () => {
		const formData = new FormData();
		formData.append("file", selectedFile);

		if (option === "deep") {
			url = route + "/profundidad";
		} else if (option === "breadth") {
			url = route + "/anchura";
		} else if (option === "iterative") {
			url = route + "/profundidad_iterativa";
		} else if (option === "uniform") {
			url = route + "/busqueda_uniforme";
		} else if (option === "greedy") {
			url = route + "/greedy";
		} else {
			url = route + "/a";
		}

		axios.post(url, formData).then((response) => {
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
				<input type="file" onChange={onFileChange} style={{ marginBottom: "20px" }} />
				<div onClick={cipher}>Try!</div>
				<h6 className="fw-bold mb-0">Option:</h6>
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
				<BasicTable rows={statistics}></BasicTable>
				{imagevalue != null && <img style={{maxWidth:"1200px",maxHeight:"1200px"}} src={imagevalue}></img>} 
				{response != null && <Canvas props={response}></Canvas>}
			</header>
		</div>
	);
}

export default App;
