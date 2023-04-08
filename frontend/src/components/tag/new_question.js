import JoditEditor from "jodit-react";
import { useRef, useState, useEffect } from "react";
import Select from 'react-select';

export default function New_ques() {

    const [tags,setTags] = useState([])

  useEffect(() => {
    fetch('/tag/list').then((res) =>
        res.json().then((data) => {
            // console.log(data);
            const p = Object.values(data)
            const q = JSON.stringify(p)
            const s = JSON.parse(q)
            console.log(s)
            // console.log(s)
            // console.log(colourOptions)
            setTags(s)
          })
          );
        }, []); 
        
        const colourOptions = [
          { value: 'chocolate', label: 'Chocolate' },
          { value: 'strawberry', label: 'Strawberry' },
          { value: 'vanilla', label: 'Vanilla' }
        ]
        
      console.log(colourOptions)
    const editor = useRef(null);
    const [content,setContent] = useState('');
    return (
        <>
        <body>
    <div class="row">
      <div class="page_title p-1 d-flex justify-content-center">
          -: Ask any Questions :-
      </div>
    </div>

    <form class="row mx-5 my-4" method="POST" action="/ask/question">
    <div class="title d-flex justify-content-center col-12" style={{"font-size": "35px"}}>
    <div class="input-group mb-3" >
        <span class="d-flex justify-content-center input-group-text new_question_span" id="basic-addon1">Title</span>
        <input type="text" class="form-control"  placeholder="Enter title.." aria-label="Title" aria-describedby="basic-addon1"></input>
    </div>
  </div>

    <div class="tag  col-12 d-flex flex-row mb-3" style={{"zIndex":"99"}}>
    {/* <div class="input-group my-3" > */}
        <span class="d-flex justify-content-center input-group-text new_question_span" id="basic-addon1">Tag</span>
        {/* <input type="text" class="form-control"  placeholder="Enter tags.." aria-label="Tag" aria-describedby="basic-addon1"></input> */}


    <div class="filter_box">
    {tags?<Select
    // defaultValue={[colourOptions[2], colourOptions[3]]}
    isMulti
    // name="colors"
    options={tags}
    className="basic-multi-select"
    classNamePrefix="select"
  />:<></>}
    </div>

{/* </div> */}
  </div>


  <div class="col-12 mb-3">
  <div class="d-flex justify-content-start ">
        <span class="d-flex justify-content-center input-group-text new_question_span">Body</span>

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




    </form>

    
      

</body>

        </>
    );
}