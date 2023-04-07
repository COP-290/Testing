import { useEffect,useState } from "react";
import "highlight.js/styles/github.css";
import hljs from "highlight.js";
import Ans from './ans'

export default function Par_test() {

  const [data,setdata] = useState(0);
  const [ans,setans] = useState(0);
  const [score,setScore] = useState(0);

  useEffect(()=>{
    hljs.highlightAll();
  });

  useEffect(() => {
    
    fetch(`/80/answer`).then((res) =>
    res.json().then((data) => {
      console.log(data);
      setdata(data)
    })
    );    

    fetch(`/80/answers`).then((res) =>
    res.json().then((data) => {
      // console.log(data);
      setans(data)
    })
    );

},[score]);

  function inc(){
    fetch(`/80/upscore`).then((res) =>
    res.json().then((data) => {
      console.log(data);
      setScore(data)
    })
    );
  }

  function dec(){
    fetch(`/80/downscore`).then((res) =>
    res.json().then((data) => {
      console.log(data);
      setScore(data)
    })
    );
  }

  function api(id,Answer){
    fetch(`/${id}/new_ans`, {
        method: 'POST',
        body: JSON.stringify({
          Answer:Answer,
        }),
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
        <>
        <body >

  <div class="row">
      <div class="row">
          <div class="col-xl-9 col-lg-9 col-md-9 col-sm-12 px-5 d-flex justify-content-start">
              {data?data[0][4]:""}
          </div>
          <div class ="col-xl-3 col-lg-3 col-md-3 col-sm-12 px-4 py-2 d-flex justify-content-end">
              <button type="button" class=" ask_btn btn btn-success">
                Ask question
              </button>
          </div>
      </div>

      <div class="row px-5">
        <div class="d-flex justify-content-end">
        <div class="question_box col-8 p-2 d-flex flex-row">
              <div class="col-2 px-2">
                <a class="like" onClick={inc}>
                  like
                </a>
                <div class="like">
                 {data?data[0][3]:""}
                </div>
                <a class="like" onClick={dec}>
                  disike
                </a>
              </div>
            
              
              <div class="answer_title col-10 p-1 d-flex justify-content-end flex-column" style ={{"font-size":"x-large", "color":"3A4D3A","cursor": "pointer"}}>
               
                
              {data?<div dangerouslySetInnerHTML={{__html:data[0][5]}} />:<></>}
 
               
              </div>
              
          </div>
        </div>
         
      </div>
      <div class="row py-2 d-flex flex-row ">
        <div class="d-flex flex-row flex-wrap justify-content-start px-3" style={{"row-gap":"15px"}}>
        {data[1]?  Object.entries(data[1]).map(([key,value])=>
          <div class="  justify-content-start px-3">
            <a class="num_button py-2 my-5 px-3" >
              {value[0]}
            </a>
          </div>
        ):<></>}

        </div>
      </div>

          <div  class="col-xl-2 col-lg-2 col-md-2 col-sm-12 col-12 mt-3 justify-content-sm-center post_data_box mb-3">
              <div class="row px-2 d-flex">
                  <div class="">
                      Posted by :- 
                  </div>
                  <div class="user_p" >
                      <div class="d-flex justify-content-start">
                          <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                              <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                              <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                          </svg>
                        </div>
                  </div>
                </div>
              <div class="row px-2 d-flex flex-column">
                  <div class="">
                      Posted on :- 
                  </div>
                  <div class="user_p3 d-flex float-end ">
                      {/* {{l[i][0][2]}} */}
                  </div>
              </div>
          </div>
      </div>
  
      <hr style={{"border": "solid 0.75px !important"}} />
      {/* {% endfor %} */}
      <div class="row">
      
      {ans?  Object.entries(ans).map(([key,value])=>
<>
<Ans value={value}/>
</>
      ):<></>}
    </div>
    <hr style={{"border": "solid 0.75px !important"}} />
    <form class="row d-flex justify-content-center" method="POST" action={data?`/${data[0][0]}/new_ans`:""}>
      <div class="col-xl-8 col-lg-8 col-md-9 col-sm-10 col-12 m-2" style={{"font-size": "larger"}}>
        Submit your answer
      </div>
      <div class=" col-xl-8 col-lg-8 col-md-9 col-sm-10 col-12 ">
        <div class="input-group">
          <span class="input-group-text">Answer</span>
          <textarea name= "Answer" class="form-control ans_body " aria-label="Body" placeholder="Write your answer..."></textarea>
        </div>
      </div>
      <div class="d-flex justify-content-center mt-3">
        <div class="col-3 d-flex justify-content-center column-gap-1">
          <button type="submit" class="btn btn-outline-primary">Submit</button>
          <button type="button" class="btn btn-outline-danger">Cancel</button>
        </div>
      </div>
    </form>
</body>


        </>
    );
}