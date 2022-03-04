



import React, { createContext, useEffect, useState } from "react";
import jwt_decode from "jwt-decode";

import {useNavigate} from 'react-router-dom'


const AuthContext = createContext()
export default AuthContext;


export const AuthProvider = ({children}) => {
    
    
    let [authTokens, setAuthTokens] = useState(() =>localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null);
    let [user, setUser] = useState(() => localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null);
    let [loading, setLoading] = useState(true)

    const navigate = useNavigate()

    const loginUser = async (e ) => {
        e.preventDefault()
        console.log('Form Submitted')

        let response = await fetch("http://127.0.0.1:8000/api/token/", 
        {method: "POST",
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'username':e.target.username.value, 'password':e.target.password.value})
        });
        let data = await response.json()
        if (response.status === 200){
            setAuthTokens(data)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
            navigate('/')
        }else{
            alert('something went wrong')
        }
    }

    const logoutUser = () => {
        setAuthTokens(null)
        setUser(null)
        localStorage.removeItem('authTokens')
        navigate('/login')
    }


    const updateToken = async () => {
        
        console.log('refresh')
        const response = await fetch("http://127.0.0.1:8000/api/token/refresh/", {
            method: "POST",
            headers: {
                'Content-Type':'application/json'
            },
            body:JSON.stringify({'refresh':authTokens?.refresh})
        })
        const data = await response.json()

        if (response.status === 200){
            setAuthTokens(data)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
        }
        else{
            logoutUser()
        }
        if(loading){
            setLoading(false)
        }
    }
        

    const contextData = {
        user:user,
        loginUser:loginUser,  
        logoutUser:logoutUser,
        name: 'NAME',
    }

    useEffect(() => {
        if (loading){
            updateToken()
        }

        const interval = setInterval(()=> {
            if (authTokens){
                updateToken()
            }
        }, 3000)


        return ()=> clearInterval(interval)
        
    }, [authTokens, loading])












    return(
        
        <AuthContext.Provider value={contextData}>
            {loading ? null : children}
        </AuthContext.Provider>

    )
}
