import './App.css';
import React, {useEffect, useState} from 'react'
import {Container, Row, Col, Card} from 'react-bootstrap'

import axios from 'axios'

import AddToDo from './components/AddToDo'  // AddToDo Component
import ToDo from './components/ToDo'        // ToDo Component
import CompletedToDo from './components/CompletedToDo'



function App() {
  const [todos, setToDos] = useState([])
  const [done, doneTodoList] = useState([])


  const doneList = async () =>{
    try{
      const response = await axios.get('/api/v1/todo/')
      const {data} = response
      doneTodoList(data)
    }catch(err){
      console.log(err)
    }
  }
  useEffect(() => {
    doneList()
  }, [])

  const putBack = async id => {
    try{
      const todo = done.filter(todo => todo.id === id)[0]    // .filter will return a list, need to get the data(dictionary)
      todo.completed = false
      console.log(todo.completed)
      await axios.put(`/api/v1/todo/${id}/`, todo)
      getToDos()
      doneList()
    }catch(err){
      console.log(err)
    }
  }
  const doneDelete = async id => {
    try{
      await axios.delete(`/api/v1/todo/${id}`)
      doneList()
    }catch(err){
      console.log(err)
    }
  }







  // getToDos async function      async (parameter)
  const getToDos = async () => {
    try{
      const response = await axios.get('/api/v1/todo/')
      // console.log(response)
      const {data} = response       // data = dictionary
      setToDos(data)                // {data}  =  response.data
    }catch(err){
      console.log(err)
    }
  }
  useEffect(() => {
    getToDos()
  }, [])

  const createToDo = async (newToDo) => {
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
      const todo = todos.filter(todo => todo.id === id)[0]    // .filter will return a list, need to get the data(dictionary)
      todo.completed = true
      await axios.put(`/api/v1/todo/${id}/`, todo)
      getToDos()
      doneList()
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
    <div className="wrapper">
      <Container>
        <Row className='pt-5'>

          <Col className='col-3'>
            <Card className='p-2'>
              <h3 className='pb-2'>Completed Tasks</h3>
              {done.map((item, index) =>(
                item.completed && <CompletedToDo key={index} id={item.id} title={item.title} putBack={putBack} doneDelete={doneDelete}/>
              ))}              
            </Card>
          </Col>

          <Col className='6'>
            <Card className='p-2'>
            <h3>Django REST framework x ReactJS</h3>
            <AddToDo createToDo={createToDo} />
            {todos.map((todo, index) => (
              !todo.completed && <ToDo key={index} id={todo.id} title={todo.title} 
              description={todo.description} doneToDo={doneToDo} destroyToDo={destroyToDo} updateToDo={updateToDo} />
            ))}
            </Card>
          </Col>

          <Col className='col-3'>
            <Card className='p-2'>
              <p>await React!!!</p>
            </Card>
          </Col>

        </Row>
      </Container>
    </div>
  );
}

export default App;
