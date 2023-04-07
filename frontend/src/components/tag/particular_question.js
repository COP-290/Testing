import { useEffect,useState,useRef } from "react";
import "highlight.js/styles/github.css";
import hljs from "highlight.js";
import JoditEditor from "jodit-react";

export default function Par_ques() {

  const editor = useRef(null);
  const [content,setContent] = useState('');
  const [data,setdata] = useState(0);
  const [ans,setans] = useState(0);

  useEffect(()=>{
    hljs.highlightAll();
  });

  useEffect(() => {
    
    fetch(`/80/answer`).then((res) =>
    res.json().then((data) => {
      // console.log(data);
      setdata(data)
    })
    );
    
    fetch(`/80/answers`).then((res) =>
    res.json().then((data) => {
      // console.log(data);
      setans(data)
    })
    );

},[]);

    return (
        <>
        <body >

  <div class="row d-flex flex-row">
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

      <div class="row px-5 mt-3">
        <div class="d-flex justify-content-center">
          <div class="question_box col-xl-8 col-lg-8 col-md-11 col-sm-12 col-12 p-2 d-flex flex-column">

            <div class="row like_box+answer">
              <div class="like_box col-2 px-3 ms-3 mt-1">
                <div class="like">
                  like
                </div>
                <div class="like">
                 {data?data[0][3]:""}
                </div>
                <div class="like">
                  disike
                </div>
              </div>
              <div class="col-10 px-2 d-flex justify-content-center">
                <div class="answer_title_par col-11 p-1 d-flex justify-content-center flex-column" style ={{"font-size":"x-large", "color":"3A4D3A","cursor": "pointer"}}>
                  {data?<div dangerouslySetInnerHTML={{__html:data[0][5]}} />:<></>}
                </div>
              </div> 
            </div>  
            
            <div class="row tag+post_data_box d-flex justify-content-end flex-row">
              <div class="col-xl-10 col-lg-10 col-md-10 col-sm-12 col-12 mt-3">
                <div class="d-flex tag_box_par flex-row flex-wrap justify-content-start px-3">
                    {data[1]?  Object.entries(data[1]).map(([key,value])=>
                    <>
                        <div class=" justify-content-center px-3">
                        <a class="num_button py-2 px-3" >
                          {value[0]}
                        </a>
                      </div>
                      <div class=" justify-content-center px-3">
                        <a class="num_button py-2 px-3" >
                          {value[0]}
                        </a>
                      </div>
                    </>
                      
                    ):<></>}
                    </div>
                </div>
                <div  class="col-xl-2 col-lg-2 col-md-2 col-sm-12 col-12 mt-3 me-3 post_data_box mb-1">
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
                            {data?data[0][2]:""}
                        </div>
                    </div>
                </div>
            <div/>

          </div>
        </div>  
      </div>
  </div>
      {/* tags  */}
      <div class="row py-2 d-flex flex-row ">
        

      </div>

          
      </div>
  
      <hr style={{"border": "solid 0.75px !important"}} />
      {/* {% endfor %} */}
      <div class="row">
      
        <div class="col-6 no_answer d-flex justify-content-end">
          {/* {{m}} Answer */}100 answers
        </div>

        {/* sorting box */}
        <div class="col-6 px-3 d-flex justify-content-start">
          <div class="dropdown col-4 px-4 ">
            <button  class="sorting_box btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
              Sorting
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Newest</a></li>
              <li><a class="dropdown-item" href="#">Active</a></li>
              <li><a class="dropdown-item" href="#">Score</a></li>
            </ul>
          </div>
        </div>

      {ans?  Object.entries(ans).map(([key,value])=>
<>
        {/* Answers */}
        <div class="row px-5 mt-3 d-flex flex-row">
          <div class="d-flex justify-content-center">
            <div  class="question_box col-xl-8 col-lg-8 col-md-11 col-sm-12 col-12 p-2 d-flex flex-column">
              <div class="row px-3 mt-1">
                <div class="like_box col-xl-2 col-lg-2 col-md-2 col-sm-2 col-2 px-2">
                  <div class="like">
                    like
                  </div>
                  <div class="like">
                    {value[4]}
                  </div>
                  <div class="like">
                    disike
                  </div>
                </div>
                <div class="col-xl-10 col-lg-10 col-md-10 col-sm-10 col-10 px-2 d-flex justify-content-center">
                  <div class="answer_title_par col-11 p-1 d-flex justify-content-center flex-column" style ={{"font-size":"x-large", "color":"3A4D3A","cursor": "pointer"}}>
                    {data?<div dangerouslySetInnerHTML={{__html:value[5]}} />:<></>}
                  </div>
                </div>
              </div>
              <div class="row d-flex justify-content-end px-3 mb-1">
                <div  class="col-xl-2 col-lg-2 col-md-2 col-sm-12 col-12 mt-3 justify-content-center post_data_box">
                  <div class="row px-2 d-flex">
                    <div class="">
                        Posted by :- 
                    </div>
                    <div class="user_p4" >
                        <div class="d-flex justify-content-start">
                            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                            </svg>
                        </div>
                    </div>
                    <div class="row px-2 d-flex flex-column">
                        <div class="">
                            Posted on :- 
                        </div>
                        <div class="user_pp d-flex float-end " style={{"font-size": "large","color": "E7E4DF"}}>
                          {value[2]}
                        </div>
                  </div>
                </div>
              </div>
            </div>
          </div> 
        </div>

      {/* question date and posted user */}
      
      </div>
      </>
      ):<></>}
    </div>
    <hr style={{"border": "solid 0.75px !important"}} />
    <div class="row d-flex justify-content-center mt-2">
      <div class="col-xl-8 col-lg-8 col-md-9 col-sm-10 col-12  d-flex justify-content-center" style={{"font-size": "x-large","color":"3A4D3A !important"}}>
        Submit your answer
      </div>
      <div class="col-10 my-3">
      <div class="d-flex flex-row">
        <span class="input-group-text d-flex justify-content-center par_question_span_body">Answer</span>

        <div class="q_title">
        <JoditEditor
        
			ref={editor}
			value={content}
			onBlur={newContent => setContent(newContent)} // preferred to use only this option to update the content for performance reasons
      onChange={newcontent=>{}}
      
    />
        </div>
      </div>
      </div>
      <div class="d-flex justify-content-center ">
        <div class="col-4 d-flex justify-content-center column-gap-1">
          <div class="px-1">
            <button type="submit" class="p-1 btn btn-outline-primary">Submit</button>
          </div>
          <div class="px-1">
            <button type="button" class="p-1 btn btn-outline-danger">Cancel</button>
          </div>
        </div>
      </div>
    </div>
</body>

        </>
    );
}