import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ImageUpload from './components/ImageUpload';
import './App.css';
  
class App extends Component {
    render() {
      return (
        <Router>
            <Routes>
              <Route exact path="/upload-image" element={<ImageUpload/>}/>
            </Routes>
        </Router>
      );
    }
}
export default App;