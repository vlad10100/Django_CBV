import React, {useState} from 'react'
import {Form, Button} from 'react-bootstrap'


// AddToDo Component
const AddToDo = ({createToDo}) => {
    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')

    const addToDoHandler = e => {
        e.preventDefault()              // will not refresh after clicking the submit button.
        createToDo({
            title, description, complete:false
        })
    }

    return ( // JSX
        <Form>
            <Form.Group controlId='title'>
                <Form.Label>Title</Form.Label>
                <Form.Control type='text' placeholder='Title' onChange={e => setTitle(e.target.value)}/>
            </Form.Group>

            <Form.Group controlId='description'>
                <Form.Label>Description</Form.Label>
                <Form.Control as='textarea' placeholder='' onChange={e => setDescription(e.target.value)}/>
            </Form.Group>
            <Button className='my-3' variant='btn btn-outline-dark' type='submit' onClick={addToDoHandler}>Add</Button>
        </Form>
        
    )
}


export default AddToDo;