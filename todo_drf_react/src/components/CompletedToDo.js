import React from 'react'
import {Form, Button} from 'react-bootstrap'

const CompletedToDo = ({id, title, putBack, doneDelete}) =>{

    return(
        <div className='border border-radius rounded m-1 p-2'>
        <h6>{title}</h6>
        <Form className='text-end'>
            <Button variant='btn btn-outline-success m-1' onClick={() => putBack(id)}/>
            <Button variant='btn btn-outline-danger m-1' onClick={() => doneDelete(id)}/>
        </Form>
        </div>
    )
}

export default CompletedToDo;