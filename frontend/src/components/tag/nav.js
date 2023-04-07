export default function Navbar() {
    return (
        <>

<nav class="navbar navbar-expand-lg navbar-light ">
        <div class="container-fluid" >
          <a class="navbar-brand site_icon px-5"  href="/" style={{"fontSize":"50px"}}>askQ</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav_active nav-link active px-5" aria-current="page" href="about">About</a>
              </li>
              <li class="nav-item">
                <a class="nav-link px-5" href="tag">Tag</a>
              </li>
              <li class="nav-item">
                <a class="nav-link px-5" href="question">Question</a>
              </li>
            </ul> 
            
            <form class="d-flex pt-3">
              <input class="form-control me-2" type="search" placeholder="Search..." aria-label="Search"></input>
              <button type="button" class="nav_search_btn btn btn-success">Search</button>
            </form>
            <div class="col-1 user_ppp d-flex justify-content-end " >
                <div class="d-flex justify-content-center" >
                  <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                      <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                      <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                  </svg>
                </div>
            </div>
          </div>
        </div>
    </nav>
        </>
    );
}