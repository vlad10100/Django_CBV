

import { Navigate } from 'react-router-dom'
import { useContext } from 'react'
import AuthContext from '../context/AuthContext'


const PrivateRoute = ({children}) => {
    // console.log('private routes')
    let {user} = useContext(AuthContext)
    return (
        user ? children : <Navigate to='/login'/>   //condition ? exprIfTrue : exprIfFalse
    )
}
export default PrivateRoute