import React, { useState, useEffect } from "react";


export default function Test(){
    const [data, setdata] = useState({
        name: "",
        age: 0,
        date: "",
        programming: "",
    });
  
    // Using useEffect for single rendering
    function api(){
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch('/tag', {
            method: 'POST',
            body: JSON.stringify({
              title:"name",
              body:"body",
          
            }),
            headers: {
              'Content-type': 'application/json; charset=UTF-8',
            }
            })
            .then(function(response){ 
            return response.json()})
            .then(function(data)
            {console.log(data)
            // title=document.getElementById("title")
            // body=document.getElementById("bd")
            // title.innerHTML = data.title
            // body.innerHTML = data.body  
          }).catch(error => console.error('Error:', error)); 

    }

    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("/data").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    name: data.Name,
                    age: data.Age,
                    date: data.Date,
                    programming: data.programming,
                });
            })
        );
    }, []);

    function api(){
        fetch('/tag/6/2', {
            method: 'GET',
            // body: JSON.stringify({
            //   title:"name",
            //   body:"body",
            // }),
            headers: {
              'Content-type': 'application/json; charset=UTF-8',
            }
            })
            .then(function(response){ 
            return response.json()})
            .then(function(data)
            {console.log(data)
          }).catch(error => console.error('Error:', error)); 

    }
  
    return (
        <div className="App">
            <header className="App-header">
                <button onClick={api}>API</button>
  
            </header>
        </div>
    );
}