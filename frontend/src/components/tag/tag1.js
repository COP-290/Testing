import React, { useState, useEffect } from "react";
import { PaginationControl } from 'react-bootstrap-pagination-control';

export default function Tag() {
    
    const [page, setPage] = useState(1)
    const [data, setdata] = useState(null);

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

    useEffect(() => {

        fetch(`/tag/6/${page}`).then((res) =>
            res.json().then((data) => {
                console.log(data);
                setdata(data)
            })
        );

        fetch('/tag/number').then((res) =>
            res.json().then((data) => {
                console.log(data);
                setdata(data)
            })
        );        
        
    }, [page]);

  
    console.log(data? Object.entries(data):"false")
    return (
        <div className="App">
            <header className="App-header">
                <h1>React and flask</h1>
<button onClick={api}>API</button>

            </header>

            {data?
            Object.entries(data).map(([key,value])=>value)
            
            :<></>}

            <PaginationControl
                page={page}
                between={4}
                total={250}
                limit={20}
                changePage={(page) => {
                setPage(page); 
                console.log(page)
                }}
                ellipsis={1}
            />
        </div>
    );

}