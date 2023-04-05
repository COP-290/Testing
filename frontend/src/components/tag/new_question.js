export default function New_ques() {
    return (
        <>
        <body>
    <div class="row">
      <div class="page_title p-1 d-flex justify-content-center">
          -: Ask any Questions :-
      </div>
    </div>

    <form class="row mx-5 my-4" method="POST" action="/ask/question">

      <div class="input-group mb-3">
        <span class="input-group-text" id="title">Title</span>
        <input id="title" name="title" type="text" class="form-control q_title" placeholder="Enter the title.." aria-label="Title" aria-describedby="basic-addon1" required></input>
      </div>

      <div class="input-group">
        <span class="input-group-text">Body</span>
        <textarea name="content" class="form-control q_body" aria-label="Body" placeholder="Write the question body.."></textarea>
      </div>

      <div class="input-group mt-3">
        <span class="input-group-text" id="basic-addon1">Tag</span>
        <input name="tag" type="text" class="form-control q_tag" placeholder="Enter tags.." aria-label="Tags" aria-describedby="basic-addon1"></input>
      </div>

      <div class="d-flex justify-content-center">
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