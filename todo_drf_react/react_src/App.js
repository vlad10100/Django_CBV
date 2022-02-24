import './App.css';
import React, {useEffect, useState} from 'react'
import {Container, Row, Col, Card} from 'react-bootstrap'

import axios from 'axios'

import AddToDo from './components/AddToDo'
import ToDo from './components/ToDo'



function App() {
  const [todos, setToDos] = useState([])

  const getToDos = async () => {
    try{
      const response = await axios.get('/api/v1/todo/')
      const {data} = response
      setToDos(data)
    }catch(err){
      console.log(err)
    }
  }
  useEffect(() => {
    getToDos()
  }, [])

  const createToDo = async newToDo => {
    try{
      console.log(newToDo)
      await axios.post('/api/v1/todo/', newToDo)
      getToDos()
    }catch(err){
      console.log(err)
    }
  }

  const doneToDo = async id => {
    try{
      const todo = todos.filter(todo => todo.id === id)[0]
      todo.completed = true
      await axios.put(`/api/v1/todo/${id}/`, todo)
      getToDos()
    }catch(err){
      console.log(err)
    }
  }

  const destroyToDo = async id => {
    try{
      await axios.delete(`/api/v1/todo/${id}/`)
      getToDos()
    }catch(err){
      console.log(err)
    }
  }
  
  const updateToDo = async todo => {
    try{
      await axios.put(`/api/v1/todo/${todo.id}/`, todo)
      getToDos()
    }catch(err){
      console.log(err)
    }
  }

  return (
    <div className="wrapper p-5">
      <Container>
        <Row className='justify-content-center p-5'>
          <Col>
            <Card className='p-5'>
            <h3>React Django</h3>
            <AddToDo createToDo={createToDo} />
            {todos.map((todo, index) => (
              !todo.completed && <ToDo key={index} id={todo.id} title={todo.title} 
              description={todo.description} doneToDo={doneToDo} destroyToDo={destroyToDo} updateToDo={updateToDo} />
            ))}
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;



