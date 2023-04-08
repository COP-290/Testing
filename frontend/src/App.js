import logo from './logo.svg';
import './App.css';
import Tag1 from './components/tag/tag1';
import Tag from './components/tag/tag';
import Navbar from './components/tag/nav';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Par_ques from './components/tag/particular_question';
import Par_test from './components/tag/particular_test';
import New_ques from './components/tag/new_question';
import Test from './components/tag/test';
import Question from './components/tag/question';
import Profile from './components/tag/profile';
import Login from './components/tag/login';
import Signup from './components/tag/sign_up';
import About from './components/tag/about';
// import WebSocketCall from './components/tag/socket';
// import { io } from "socket.io-client";
import { useEffect, useState } from "react";


function App() {
  const [socketInstance, setSocketInstance] = useState("");
  const [loading, setLoading] = useState(true);
  const [buttonStatus, setButtonStatus] = useState(false);

  const handleClick = () => {
    if (buttonStatus === false) {
      setButtonStatus(true);
    } else {
      setButtonStatus(false);
    }
  };

  // useEffect(() => {
  //   if (buttonStatus === true) {
  //     const socket = io("localhost:5001/", {
  //       transports: ["websocket"],
  //       cors: {
  //         origin: "http://localhost:3000/",
  //       },
  //     });

  //     setSocketInstance(socket);

  //     socket.on("connect", (data) => {
  //       console.log(data);
  //     });

  //     setLoading(false);

  //     socket.on("disconnect", (data) => {
  //       console.log(data);
  //     });

  //     return function cleanup() {
  //       socket.disconnect();
  //     };
  //   }
  // }, [buttonStatus]);

  return (
    <>
        <Navbar/>

        <Router>
          <Routes>
            <Route path="/tag1" element={<Tag1/>} />        
            {/* <Route path="/socket" element={<WebSocketCall/>} />         */}
            <Route path="/about" element={<About/>} />        
            <Route path="/tag" element={<Tag/>} />        
            <Route path="/tag/:id" element={<Question/> } />        
            <Route path="/test" element={<Test/>} />        
            <Route path="/particular_question" element={<Par_ques/>} />        
            <Route path="/particular_test" element={<Par_test/>} />        
            <Route path="/new_question" element={<New_ques/>} />        
            <Route path="/question/:id" element={<Par_ques/>} />        
            <Route path="/question" element={<Question/>} />        
            <Route path="/profile" element={<Profile/>} />        
            <Route path="/login" element={<Login/>} />        
            <Route path="/signup" element={<Signup/>} />        
          </Routes>
        </Router>


</>
  );
}

export default App;
