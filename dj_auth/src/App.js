import './App.css';
import React from 'react'
import {BrowserRouter as Router} from 'react-router-dom'  
import {Route, Routes} from 'react-router-dom'


import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomePage';

import Header from './components/Header';

import PrivateRoute from './utils/PrivateRoute';

import { AuthProvider } from './context/AuthContext';

function App() {
  return (

      <Router>
        <AuthProvider>
          <Header />
          <Routes>        
            <Route element={<PrivateRoute><HomePage/></PrivateRoute>} path="/" exact />       // exact
            <Route element={<LoginPage/>} path="/login" />
          </Routes>
        </AuthProvider>
      </Router>

  );
}

export default App;
