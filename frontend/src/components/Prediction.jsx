import Type from "./Type";

function Prediction( {src, showImage, types} ) {
    
    if (!showImage) {
        return null;
    }

    return (
        <div>
          <img src={src} width="100px"></img>
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