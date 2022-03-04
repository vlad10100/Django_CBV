


import React, {useState, useEffect, useContext} from 'react'
import AuthContext from '../context/AuthContext'




const HomePage = () => {
    const {authTokens, logoutUser} = useContext(AuthContext)
    const [note, setNote] = useState([])

    

    useEffect(() => {
        getNotes()
    },[])

    const getNotes = async () =>{
        const response = await fetch("http://127.0.0.1:8000/notes/", {
            method:"GET",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + String(authTokens.access)
            }
        })
        let data = await response.json()
        if (response.status === 200){
            setNote(data)
        }
        else if(response.statusText === 'Unauthorized'){
            logoutUser()
        }
    }

    return (
        <div>
            <h1>HomePage</h1>



            <ul>
                {note.map(note => (
                    <li key={note.id}>{note.body}</li>
                ))}
            </ul>
        </div>
    )
}

export default HomePage