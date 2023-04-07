import {useState,useEffect} from 'react'

export default function Ans({value:value}){
    
    // const [as,set_as] = useState(value);
    const [score,setScore] = useState(value[4]);
    // set_as(value);
    console.log(value[0])

    
    function inc(){
      fetch(`/${value[0]}/upans`).then((res) =>
      res.json().then((data) => {
        console.log(data);
        setScore(data)
      })
      );
    }

    function dec(){
      fetch(`/${value[0]}/downans`).then((res) =>
      res.json().then((data) => {
        console.log(data);
        setScore(data)
      })
      );
    }    

    // useEffect(() => {
    
    //   fetch(`/80/answers`).then((res) =>
    //   res.json().then((data) => {
    //     // console.log(data);
    //     set_as(data)
    //   })
    //   );
  
  // },[score]);

    return(
      <>
      <div class="col-6 no_answer d-flex justify-content-end">
        {/* {{m}} Answer */}
      </div>
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

      <div class="row px-5 mt-3">
        <div  class="question_box p-2 d-flex flex-row">
            <div class="col-2 px-2">
              <a class="like"  onClick={inc}>
                like
              </a>
              <div class="like">
                 {score}
              </div>
              <a class="like" onClick={dec}>
                disike
              </a>
            </div>
            
            <div class="answer_title col-10 p-1 d-flex justify-content-end flex-column" style ={{"font-size":"x-large", "color":"3A4D3A","cursor": "pointer"}}>
             
              
             {value[5]?<div dangerouslySetInnerHTML={{__html:value[5]}} />:<></>}

             </div>
           
            
        </div>
    </div>
      <div  class="col-xl-2 col-lg-2 col-md-2 col-sm-12 col-12 mt-3 justify-content-sm-center post_data_box mb-3">
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
            <div class="user_pp d-flex float-end " style={{"font-size": "large","color": "rgb(88, 88, 88)"}}>
           {value[2]}
               
            </div>
        </div>
      </div>

    </div>
    </>
    
    );
  }
