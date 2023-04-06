import logo from './logo.svg';
import './App.css';
import Tag1 from './components/tag/tag1';
import Tag from './components/tag/tag';
import Navbar from './components/tag/nav';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Par_ques from './components/tag/particular_question';
import New_ques from './components/tag/new_question';
import Test from './components/tag/test';
import Question from './components/tag/question';
import Profile from './components/tag/profile';
import Login from './components/tag/login';
import Signup from './components/tag/sign_up';
import Index from './components/tag';

function App() {
  return (
    <>
        <Navbar/>

        <Router>
          <Routes>
            <Route path="/tag1" element={<Tag1/>} />        
          </Routes>
        </Router>

        <Router>
          <Routes>
            <Route path="/index" element={<Index/>} />        
          </Routes>
        </Router>

        <Router>
          <Routes>
            <Route path="/tag" element={<Tag/>} />        
          </Routes>
        </Router>

        <Router>
          <Routes>
            <Route path="/test" element={<Test/>} />        
          </Routes>
        </Router>

        <Router>
          <Routes>
            <Route path="/particular_question" element={<Par_ques/>} />        
          </Routes>
        </Router>

        <Router>
          <Routes>
            <Route path="/new_question" element={<New_ques/>} />        
          </Routes>
        </Router>

        <Router>
          <Routes>
            <Route path="/question" element={<Question/>} />        
          </Routes>
        </Router>

        <Router>
          <Routes>
            <Route path="/profile" element={<Profile/>} />        
          </Routes>
        </Router>

        <Router>
          <Routes>
            <Route path="/login" element={<Login/>} />        
          </Routes>
        </Router>

        <Router>
          <Routes>
            <Route path="/signup" element={<Signup/>} />        
          </Routes>
        </Router>

</>
  );
}

export default App;
