import React, { useState, useEffect } from "react";
import { PaginationControl } from 'react-bootstrap-pagination-control';

export default function Tag() {

    const [page, setPage] = useState(1)
    const [data, setdata] = useState(null);

    useEffect(() => {
        fetch(`/tag/6/${page}`).then((res) =>
            res.json().then((data) => {
                console.log(data);
                setdata(data)
            })
        );
    }, [page]);

    return (
        <>
        <body>
        <div class="page_title p-1 d-flex justify-content-center">
         Tags 
    </div>
    <div class="p-2 d-flex justify-content-center" style={{"color":"3A4D3A", "font-size":"xx-large;"}}>
        A tag is a label that categorizes your question with other, similar questions. Using the right tags makes it easier for others to find and answer your question.
    </div>
    <div class="d-flex justify-content-center">
        <div class="col-4 px-3 py-2">
            <form action="/action_page.php" style={{"border":"solid 1.5px", "border-radius":"7px"}}>
                <input style={{"background-color": "#E7E4DF"}}class="form-control" list="tags" name="tag" id="tag" placeholder="Search"></input>
                <datalist id="tags">
                  <option value="Python"/>
                  <option value="JavaScript"/>
                  <option value="MySQL"/>
                  <option value=""/>
                  <option value="Safari"/>
                </datalist>    
            </form>
        </div>
    </div>    
    <div class="container">
    <div class="row px-4">
        {data?
            Object.entries(data).map(([key,value])=>
        <div class="tag_col col-xl-4 col-lg-6 col-md-6 col-sm-12 col-12 p-3">
            <div  onclick="window.location.href = `/{{post[1]}}/question`"  class="tag_box_tag p-3">
                <div class="tag_title" style={{"font-family": "'Roboto Mono', monospace"}}>
                    <div >{value[1]}</div> 
                    <a href="{{ url_for('display_question', tag=post) }}"/>

                </div>
                <div class="tag_body" style={{" color": "rgb(88, 88, 88)"}} > 
                    Python is a multi-paradigm, dynamically typed, multi-purpose programming language.
                </div>
                <div class="tag_questions d-flex justify-content-end " style={{"color": "rgb(88, 88, 88)"}}>
                    {value[0]} questions
                </div>
            </div>
        </div>    
        ):<></>}
    </div> 
    <div class="d-flex justify-content-center" >
        <PaginationControl
            page={page}
            between={4}
            total={250}
            limit={6}
            changePage={(page) => {
            setPage(page); 
            console.log(page)
            }}
            ellipsis={1}
        />
    </div>
   
   </div>
        </body>
        </>
    );
}