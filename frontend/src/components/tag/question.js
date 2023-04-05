export default function Question() {
    return (
        <>
        <body>

<div class="row">

<div class="page_title p-1 d-flex justify-content-center">
    -: Questions :-
</div>

<div class ="col-12 px-4 d-flex justify-content-end">
  <button type="button" class="ask_btn btn btn-success">
    <a href="/ask/question">Ask question</a>
  </button>
</div>

<div class="row col-12 px-3 d-flex justify-content-start">
  <div class="dropdown col-12 px-4 ">
    <button  class="sorting_box btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
      Sorting
    </button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="/time/question">Newest</a></li>
      <li><a class="dropdown-item" href="#">Active</a></li>
      <li><a class="dropdown-item" href="/score/question">Score</a></li>
    </ul>
  </div>
</div>

<div class="row d-flex justify-content-start">
  <div class="col-12 d-flex justify-content-start" style={{"font-size": "larger"}}>
    <div class="px-3 py-2">
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <label class="filter_box input-group-text" for="inputGroupSelect01">Filters</label>
        </div>
        <select class="custom-select" style={{"border-radius": "2.75px","color": "3A4D3A"}} id="inputGroupSelect01">
          <option selected>choose the filter...</option>
          <option value="1">fitler-1</option>
          <option value="2">fitler-2</option>
          <option value="3">fitler-3</option>
        </select>
      </div> 
    </div> 
  </div>  
</div>

{/* {% for i in range(0,n) %} */}
  <div class="col-12 d-flex justify-content-end py-2 px-4">
    <div class="question_box p-3">
        <div class="container">
          <div class="row mx-lg-n5">
            <div class="vav col-xl-2 col-lg-2 col-md-2 col-sm-3 col-3 d-flex justify-content-center" >0 votes</div>
            <div class="vav col-xl-2 col-lg-2 col-md-2 col-sm-3 col-3 d-flex justify-content-center" >0 answer</div>
            <div class="vav col-xl-2 col-lg-2 col-md-2 col-sm-3 col-3 d-flex justify-content-center" >0 views</div>
          </div>
        </div>
        <div class="question" style={{"font-style": "italic","font-size": "larger", "font-weight": "bold"}}>
            {/* <a href="/{{l[i][0][0]}}/answer ">
            {% autoescape off %}
          {{l[i][0][4]}}
          {% endautoescape %}
        </a> */}
        </div>
        <div class="answer" style={{" font-size": "larger","color": "rgb(88, 88, 88);" }}> 
          
          {/* {% autoescape off %}
            {{l[i][0][5]}}
            {% endautoescape %} */}


        </div>
      
        <div class="row py-2 d-flex flex-row ">
          <div class="d-flex flex-row flex-wrap justify-content-start px-3" style={{"row-gap": "15px"}}>
            {/* {% for j in l[i][1] %} */}
            <div class="  justify-content-start px-3">
              {/* <a class="num_button py-2 my-5 px-3" href="/{{j}}/question">
                {{j}}
              </a> */}
            </div>
            {/* {% endfor %} */}
          </div>
        </div>

        <div class="col-12 user_ppp d-flex justify-content-end ">
            <div class="d-flex justify-content-center">
              <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                  <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                  <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
              </svg>
            </div>
        </div>

    </div>  
  </div>  
{/* {% endfor %} */}
</div>

<div class="d-flex justify-content-center" >
{/* {{pagination.links}} */}
</div>



</body>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/highlight.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/atom-one-light.min.css" integrity="sha512-o5v54Kh5PH0dgnf9ei0L+vMRsbm5fvIvnR/XkrZZjN4mqdaeH7PW66tumBoQVIaKNVrLCZiBEfHzRY4JJSMK/Q==" crossorigin="anonymous" referrerpolicy="no-referrer" />
<script>hljs.initHighlightingOnLoad();</script>
        </>
    );
}