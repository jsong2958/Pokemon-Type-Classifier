import { useState } from 'react'
import './App.css'
import Button from './components/Button.jsx'
import Image from './components/Prediction.jsx'

function App() {

  const [img, setImg] = useState("")

  return (
    <>
      <h1 id="title">Pokemon Type Classifier</h1>
      <div className="container">
        <h2>Upload image here: </h2>
        <input type="file" id="fileInput"></input>
        <Button label={"Predict"} />

      </div>
    </>
  )
}

export default App
