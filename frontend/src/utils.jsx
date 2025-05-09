function get_image(image) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader()

        reader.readAsDataURL(image)


        reader.onload = () => {
            resolve(reader.result.split(',')[1]);
        };

        reader.onerror = reject;

    })
    
}

const get_prediction = async (image) => {

    if (!image) {
        return;
    }

    try {
        const b64 = await get_image(image);
        const url = "http://localhost:8080/predict";
        const data = {
            "file": b64
        };
        
        const response = await fetch(url, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        const prediction = await response.json();
        
        return prediction.prediction;

    } catch (err) {
        console.error(err)
    }

}


export default get_prediction;