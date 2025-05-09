import Type from "./Type";
import './Prediction.css'

function Prediction( {src, showImage, types} ) {
    
    if (!showImage) {
        return null;
    }

    return (
      <div className="pred-container">
        <img src={src} width="300px"></img>
        <h3>Predicted types: </h3>
        <ul>
        {types.map((type, index) => (
          <Type type={type} key={index}/>
        ))}
        </ul>
      </div>
    );

}

export default Prediction