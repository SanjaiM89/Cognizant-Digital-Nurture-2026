import { useState } from 'react'
import Header from './components/header'
import Footer from './components/footer'
import Course from './components/CourseCard'
function App(){
    return (
        <div>
            <Header siteName="Student Portal"/>
            <main>
                <h2>Courses</h2>
                <Course name="test" code="123" credits={3} grade="A"/>
            </main>
            <Footer/>
        </div>
    )
}
export default App
