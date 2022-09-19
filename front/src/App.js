import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import axios from 'axios';


function App() {
  const route="http://127.0.0.1:8000/classic"
  var url;
  const [selectedFile,setState]=useState(null);
  const [option,setOption]=useState('deep');

  const addOption=val=>{
    setOption(val.target.value)
    console.log(val.target.value)
  };

  const onFileChange= (e)=>{
    setState(e.target.files[0])
  }
  
  const cipher =()=>{
    const formData= new FormData();
    formData.append("file", selectedFile);
    
    if (option==="deep"){
      url=route+"/profundidad"
    }
    else if (option==="breadth"){
      url=route+"/anchura"
    }
    else if (option==="iterative"){
      url=route+"/profundidad_iterativa"
    }
    else if (option==="uniform"){
      url=route+"/busqueda_uniforme"
    }
    else if (option==="greedy"){
      url=route+"/greedy"
    }
    else {
      url=route+"/a"
    }
    
    
    axios
        .post(url, formData)
        .then((response) => {
            console.log(response.data);
        });

    
}

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <input  type="file" onChange={onFileChange} style={{marginBottom : "20px"}} />
        <div onClick={cipher}  >Try!</div>
        <h6 className="fw-bold mb-0">Option:</h6>
        <select  onChange={addOption} className="form-select" name="option_encrypt">
            <option value="deep" selected="">Deep</option>
            <option value="breadth">Breadth</option>
            <option value="iterative" selected="">Iterative</option>
            <option value="uniform">Uniform</option>
            <option value="greedy" selected="">Greedy</option>
            <option value="A*">A*</option>
        </select>
      </header>
    </div>
  );
}

export default App;
