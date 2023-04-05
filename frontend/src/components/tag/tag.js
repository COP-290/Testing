import React, { useState, useEffect } from "react";


export default function Tag() {


const [data, setdata] = useState(null);
  
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("/3/tag").then((res) =>
            console.log(res)
        );
    }, []);
    // console.log(data)
    return (
        <div className="App">
            <header className="App-header">
                <h1>React and flask</h1>
                {/* Calling a data from setdata for showing */}

  
            </header>
        </div>
    );

}