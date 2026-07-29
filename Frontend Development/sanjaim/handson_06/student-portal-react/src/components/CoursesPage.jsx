import { useState, useEffect } from 'react'
import { useDispatch } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import Course from './CourseCard'
import { enroll } from '../store/enrollmentSlice'

const CoursesPage = () => {
  const [course_, setCourse_data] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const dispatch = useDispatch()
  const navigate = useNavigate()

  useEffect(() => {
    fetch('http://127.0.0.1:8000/posts')
      .then((response) => response.json())
      .then((data) => {
        const courses = data.map((post) => ({
          id: post.id,
          name: post.name,
          code: post.code,
          credits: post.credits,
          grade: post.grade,
        }))
        setCourse_data(courses)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  const [search, setSearch] = useState('')
  const filteredCourses = course_.filter((course) => {
    return course.name.toLowerCase().includes(search.toLowerCase())
  })

  const handleEnroll = (selectedCourse) => {
    dispatch(enroll(selectedCourse))
    navigate('/profile')
  }

  if (loading) {
    return <h2>Loading.....</h2>
  }

  if (error) {
    return <h2 style={{ color: 'red' }}>{error}</h2>
  }

  return (
    <div>
      <h2>Courses</h2>
      <input
        style={styles.searchbar}
        type='text'
        placeholder='Search by Name'
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px' }}>
        {filteredCourses.map((course) => (
          <Course
            key={course.id}
            name={course.name}
            code={course.code}
            credits={course.credits}
            grade={course.grade}
            onEnroll={() => handleEnroll(course)}
          />
        ))}
      </div>
    </div>
  )
}

const styles = {
  searchbar: {
    fontSize: "14px",
    fontFamily: "Arial, sans-serif",
    color: "#202124",
    display: "flex",
    zIndex: 3,
    height: "44px",
    background: "#fff",
    borderRadius: "10px",
    marginLeft: "5px",
    marginBottom: "20px",
    width: "400px",
    boxShadow: "none",
    border: "1px solid grey"
  },
}

export default CoursesPage
