export default function Login() {
    return (
        <>
        <body>

<div class="row">
  <div class="page_title col-12 d-flex justify-content-center">
    -: Login :-
  </div>
</div>

<div class="row">
    <div class="col-12 d-flex justify-content-center mt-5">
        <div class="sign_up_box p-3">
            <form>
                <div class="mb-3 row d-flex flex-column">
                    <label for="staticUsername" class="col-sm-2 col-form-label label_title">Username</label>
                    <div class="col-sm-10">
                      <input type="text" readonly class="form-control-plaintext" id="staticUsername" value="username"></input>
                    </div>
                </div>
                <div class="mb-3 row d-flex flex-column">
                    <label for="staticEmail" class="col-sm-2 col-form-label label_title">Email</label>
                    <div class="col-sm-10">
                      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="email@example.com"></input>
                    </div>
                </div>
                <div class="mb-3 row d-flex flex-column">
                    <label for="inputPassword" class="col-sm-2 col-form-label label_title">Password</label>
                    <div class="col-12">
                      <input type="password" class="form-control" id="inputPassword"></input>
                    </div>
                  </div>
                <div class="mb-3 form-check">
                  <input type="checkbox" class="form-check-input" id="exampleCheck1"></input>
                  <label class="form-check-label" for="exampleCheck1">Check me out</label>
                </div>
                <div class="mb-3 d-flex justify-content-center">
                  Are you new here?
                  <div class="px-1">
                    <a href="signup" class="link-primary">click here</a>
                  </div>
                </div>
                <div class="d-flex justify-content-center">
                    <button type="submit" class="sign_up_btn btn btn-primary">Login</button>
                </div>
            </form>
        </div>
    </div>
    
</div>

</body>
        </>
);
}