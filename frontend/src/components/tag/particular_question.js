export default function Par_ques() {
    return (
        <>
        <body >
  {/* {% for i in range(0,n) %} */}
  <div class="row">
      <div class="row">
          <div class="col-xl-9 col-lg-9 col-md-9 col-sm-12 px-5 d-flex justify-content-start">
            {/* {% autoescape off %}
              {{l[i][0][4]}}
            {% endautoescape %} */}
          </div>
          <div class ="col-xl-3 col-lg-3 col-md-3 col-sm-12 px-4 py-2 d-flex justify-content-end">
              <button type="button" class=" ask_btn btn btn-success">
                Ask question
              </button>
          </div>
      </div>

      <div class="row px-5">
          <div class="question_box p-2 d-flex flex-row">
              <div class="col-2 px-2">
                <div class="like">
                  like
                </div>
                <div class="like">
                 {/* {{l[i][0][3]}} */}
                </div>
                <div class="like">
                  disike
                </div>
              </div>
            
              <div class="answer_title col-10 p-1 d-flex justify-content-end flex-column">
                {/* {% autoescape off %}
              {{l[i][0][5]}}
              {% endautoescape %} */}
              </div>
          </div>
      </div>
      <div class="row py-2 d-flex flex-row ">
        <div class="d-flex flex-row flex-wrap justify-content-start px-3" style={{"row-gap":"15px"}}>
          {/* {% for j in l[i][1] %} */}
          <div class="  justify-content-start px-3">
            <a class="num_button py-2 my-5 px-3" >
              {/* {{j[0]}} */}
            </a>
          </div>
          {/* {% endfor %} */}
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
      
        {/* {% for answer in ans_list %} */}
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
                <div class="like">
                  like
                </div>
                <div class="like">
                  {/* {% autoescape off %}
                   {{answer[4]}}
              {% endautoescape %} */}
                </div>
                <div class="like">
                  disike
                </div>
              </div>
            
              <div class="col-10 p-1 d-flex justify-content-end flex-column" style ={{"font-size":"x-large", "color":"3A4D3A","cursor": "pointer"}}>
               
                {/* {% autoescape off %}
                {{answer[5]}} 
              {% endautoescape %}  */}
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
                  {/* {% autoescape off %}
             {{answer[2]}}
              {% endautoescape %} */}
                 
              </div>
          </div>
        </div>

      </div>
    {/* {% endfor %} */}
    </div>
    <hr style={{"border": "solid 0.75px !important"}} />
    <div class="row d-flex justify-content-center">
      <div class="col-xl-8 col-lg-8 col-md-9 col-sm-10 col-12 m-2" style={{"font-size": "larger"}}>
        Submit your answer
      </div>
      <div class=" col-xl-8 col-lg-8 col-md-9 col-sm-10 col-12 ">
        <div class="input-group">
          <span class="input-group-text">Answer</span>
          <textarea class="form-control ans_body " aria-label="Body" placeholder="Write your answer..."></textarea>
        </div>
      </div>
      <div class="d-flex justify-content-center mt-3">
        <div class="col-3 d-flex justify-content-center column-gap-1">
          <button type="button" class="btn btn-outline-primary">Submit</button>
          <button type="button" class="btn btn-outline-danger">Cancel</button>
        </div>
      </div>
    </div>
</body>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/highlight.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/atom-one-light.min.css" integrity="sha512-o5v54Kh5PH0dgnf9ei0L+vMRsbm5fvIvnR/XkrZZjN4mqdaeH7PW66tumBoQVIaKNVrLCZiBEfHzRY4JJSMK/Q==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<script>hljs.initHighlightingOnLoad();</script>
        </>
    );
}