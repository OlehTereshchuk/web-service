import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [serverData, setServerData] = useState({});
  const [error, setError] = useState('')
  const [correlation, setCorrelation] = useState(0);

  useEffect(() => {
    console.log(serverData);
  }, [serverData, correlation])

  const handleSelectMethod = e => {
    e.preventDefault();
    const fileData = new FormData()
    fileData.append('file', file)
    axios.post(`http://127.0.0.1:8000/api/${e.target.value}-trend/`, fileData)
    .then(response => {
      if (response.data.error) return setError(response.data.error);
      return response.data
    })
    .then(data => setServerData(data))
    .catch(error => console.log(error.message))
  }
  
  return (
    <div className="App">
      <form encType="multipart/form-data">
        <input type="file" onChange={e => setFile(e.target.files[0])}/>
        {file && (
          <>
            <button onClick={e => handleSelectMethod(e) } value='linear'>Linear</button>
            <button onClick={e => handleSelectMethod(e) } value='logarithmic'>Logarithmic</button>
            <button onClick={e => handleSelectMethod(e) } value='hyperbolic'>Hyperbolic</button>
            <button onClick={e => handleSelectMethod(e) } value='smoothing'>Smoothing</button>
            <p>{serverData?.correlation}</p>
            {error && !serverData?.data && <p>{error}</p>}
          </>
        )}
      </form>
    </div>
  );
}

export default App;
