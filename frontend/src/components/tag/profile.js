import { useState,useEffect } from "react"

export default function Profile() {

  const [text,setText] = useState(true)
  const [btn,setBtn] = useState(true)

  useEffect(() => {
    // document.title = `You clicked ${} times`;
  },[Text]);

    return (
        <>
        <body>
        <div class="d-flex flex-column justify-content-center mt-3">

<div class="row user_pp d-flex justify-content-center ">
  <div class="d-flex justify-content-center" >
    <svg xmlns="http://www.w3.org/2000/svg" width="150" height="150" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
        <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
    </svg>
  </div>
</div>

<div class="row d-flex justify-content-center mt-3">

  <div class="username d-flex justify-content-center col-8" style={{"font-size": "35px"}}>
    <div class="input-group mb-3" >
        <span class="input-group-text" id="basic-addon1">Username</span>
        <input type="text" disabled={text} class="form-control"  placeholder="Username" aria-label="Username" aria-describedby="basic-addon1"></input>
    </div>
  </div>

  <div class="user ID d-flex justify-content-center col-8" style={{"font-size": "35px"}}>
    <div class="input-group mb-3">
        <span class="input-group-text" id="basic-addon1">User ID</span>
        <input type="text" disabled={text} class="form-control" placeholder="User ID" aria-label="User ID" aria-describedby="basic-addon1"></input>
    </div>
  </div>

  <div class="joindate d-flex justify-content-center col-8" style={{"font-size": "35px"}}>
    <input class="form-control" type="text" placeholder="Join Date : DD/MM/YYYY" aria-label="Disabled input example" disabled></input>
  </div>
</div>

<hr/>

<div class="aboutme_row row d-flex justify-content-center">
  <div class="col-8">
    <div class="input-group">
      <span class="input-group-text">About me</span>
      <textarea disabled={text} name="content" class="form-control q_body" aria-label="Body" placeholder="Write something about yorself.."></textarea>
    </div>
  </div>
  <div class="d-flex justify-content-center mt-3">
        <button type="button" class="btn btn-success" onClick={()=>{setText(Text => !Text)}}>
            {`${Text?"Edit":"Save"}`}
        </button>
</div>
    

</div>

<hr/>

<div class="activity_row row">
  <div class="username d-flex justify-content-center" style={{"font-size": "26px;"}}>
    Reputation : 
  </div>
  <div class="userid d-flex justify-content-center" style={{"font-size": "26px;"}}>
    Up vote :
  </div>
  <div class="joindate d-flex justify-content-center" style={{"font-size": "26px;"}}>
    Down vote :
  </div>
</div>

<hr/>

<div class="settings_row row">
  <div class="d-flex flex-column justify-content-center"> 
  <a href="/pythonlogin/logout"> <div class="d-flex justify-content-center mb-3">
      <button type="button" class="btn btn-outline-danger">Logout</button>
    </div>
  </a> 
    <div class="d-flex justify-content-center mb-3">
      <button type="button" class="btn btn-outline-danger">Delele Profile</button>
    </div>
    
  </div>
</div>
</div>

</body>
        </>
    )
}