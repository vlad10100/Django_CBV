import React, {useState} from 'react'
import { Form, Row, Col, Button, Modal } from 'react-bootstrap';

const ToDo = ({id, title, description, doneToDo, destroyToDo, updateToDo}) =>{

    
    const [show, setShow] = useState(false);
    const handleClose = () => {
        setShow(false);
        setTitle(title);
        setDescription(description);
    }

    const handleShow = () => setShow(true);
    const [newTitle, setTitle] = useState(title)
    const [newDescription, setDescription] = useState(description)

    const editToDoHandler = (title, description) => {
        handleClose()
        const todo = {id, title, description}
        updateToDo(todo)
        setTitle(title)
        setDescription(description)
    }


    return (
        <>
            <Row className='border border-radius rounded m-2'>
                <Col md={1} className='my-auto'>
                    <Form>
                        <Button variant='btn btn-outline-success' size='sm' onClick={() => doneToDo(id)}>Done</Button>
                    </Form>
                </Col>
                <Col className='text-center my-auto'>
                    <h5>{title}</h5>
                    <p>{description}</p>
                </Col>
                <Col md={3}  className='text-end'>
                    <Form>
                        <Button variant='btn btn-outline-warning' size='sm' className='my-1' onClick={handleShow}>Edit</Button>
                    </Form>
                    <Form>
                        <Button variant='btn btn-outline-danger' size='sm' className='my-1' onClick={() => destroyToDo(id)}>Delete</Button>
                    </Form>
                </Col>
            </Row>

            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                    <Modal.Title>Edit ToDo</Modal.Title>
                </Modal.Header>
                <Modal.Body>


                    <Form>
                    <Form.Group controlId='title'>
                        <Form.Label>Title</Form.Label>
                        <Form.Control type='text' value={newTitle} onChange={e => setTitle(e.target.value)}/>
                    </Form.Group>

                    <Form.Group controlId='description'>
                        <Form.Label>Description</Form.Label>
                        <Form.Control as='textarea' value={newDescription} onChange={e => setDescription(e.target.value)}/>
                    </Form.Group>
                    </Form>

                </Modal.Body>
                <Modal.Footer>
                    <Button variant='btn btn-outline-dark' onClick={handleClose}>Close</Button>
                    <Button variant='btn btn-outline-dark' onClick={() => editToDoHandler (newTitle, newDescription)}>Update</Button>
                </Modal.Footer>
            </Modal>
        </>
    )
}

export default ToDo;