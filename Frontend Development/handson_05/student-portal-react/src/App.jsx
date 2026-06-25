import { useState } from 'react'
import Header from './components/header'
import Footer from './components/footer'
import Course from './components/CourseCard'
import course_d from './data'

function App(){
    const [course_,setCourse_data] = useState(course_d);
    const [search,setSearch] = useState('')
    const filteredCourses = course_.filter((course)=>{
        return course.name.toLowerCase().includes(search.toLowerCase());
    });
    return (
        <div>
            <Header siteName="Student Portal"/>
            <main>
                <h2>Courses</h2>
                <input
                type="text"
                placeholder='Search by Name'
                value={search}
                onChange={(e)=>
                    setSearch(e.target.value)
                }
                />
                <div style={{display:'flex',flexWrap:'wrap',gap:'20px'}}>
                {filteredCourses.map((course) => (
                    <Course
                    key = {course.id}
                    name = {course.name}
                    code = {course.code}
                    credits = {course.credits}
                    grade = {course.grade}
                    />
                ))}
                </div>
            </main>
            <Footer/>
        </div>
    )
}
export default App
