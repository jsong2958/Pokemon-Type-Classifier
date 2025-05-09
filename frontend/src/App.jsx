import { useState } from 'react'
import './App.css'
import Button from './components/Button.jsx'
import Prediction from './components/Prediction.jsx'
import get_prediction from './utils.jsx'

function App() {

  const [showImage, setShowImage] = useState(false)
  const [file, setFile] = useState(null)
  const [types, setTypes] = useState(null)
  const [imageSrc, setImageSrc] = useState(null)

  const handleFileChange = (event) => {
    setShowImage(false)
    const file = event.target.files[0];
    if (file) {
      setFile(file)
      setImageSrc(URL.createObjectURL(file))
    }
  };

  const handleClick = () => {
    if (file) {
      get_prediction(file).then(types => {
        setTypes(types)
        setShowImage(true);
      });
    }
  }

  return (
    <>
      <h1 id="title">Pokemon Type Classifier</h1>
      <div className="container">
        <h2>Upload image here: </h2>
        <input type="file" id="fileInput" onChange={handleFileChange}></input>
        <Prediction src={imageSrc} showImage={showImage} types={types || []}/>
        <Button label={"Predict"} onClick={() => handleClick()}/>
      </div>
    </>
  )
}

export default App
