export default function Signup() {
    return (
        <>
        <body>



<div class="row">
  <div class="page_title col-12 d-flex justify-content-center">
    -: Sign up :-
  </div>
</div>

<div class="row">
    <div class="col-12 d-flex justify-content-center mt-5">
        <div class="sign_up_box p-3">
            <form>
                <div class="mb-3">
                    <label for="exampleInputusername1" class="form-label label_title">Username</label>
                    <input type="username" class="form-control" id="exampleInputusername1" aria-describedby="usernameHelp"></input>
                  </div>
                <div class="mb-3">
                  <label for="exampleInputEmail1" class="form-label label_title">Email address</label>
                  <input type="email" class="form-control" id="exampleInputEmail1" placeholder="name@example.com" aria-describedby="emailHelp"></input>
                  <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div class="mb-3">
                  <label for="exampleInputPassword1" class="form-label label_title">Password</label>
                  <input type="password" class="form-control" id="exampleInputPassword1"></input>
                </div>
                <div class="mb-3 form-check">
                  <input type="checkbox" class="form-check-input" id="exampleCheck1"></input>
                  <label class="form-check-label" for="exampleCheck1">Check me out</label>
                </div>
                <div class="mb-3 d-flex justify-content-center">
                  Already have an account?
                  <div class="px-1">
                    <a href="login" class="link-primary">click here</a>
                  </div>
                </div>
                <div class="d-flex justify-content-center">
                    <button type="submit" class="sign_up_btn btn btn-primary">Sign up</button>
                </div>
            </form>
        </div>
    </div>
    
</div>

</body>
        </>
);
}