import { useState, useEffect } from 'react'
import Course from './CourseCard'
import { useNavigate } from 'react-router-dom'

function HomePage() {
  const [course_, setCourse_data] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
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

  useEffect(() => {
    console.log('Course Updated')
  }, [course_])

  const [search, setSearch] = useState('')
  const filteredCourses = course_.filter((course) => {
    return course.name.toLowerCase().includes(search.toLowerCase())
  })

  const [enrollCourse, setEnrollCourse] = useState([])

  const handleEnroll = (selectedCourse) => {
    const alreadyEnrolled = enrollCourse.some(
      (course) => course.id == selectedCourse.id
    )

    if (!alreadyEnrolled) {
      setEnrollCourse([...enrollCourse, selectedCourse])
      navigate("/profile")
    } else {
      alert('Already Enrolled')
    }
  }

  if (loading) {
    return <h2>Loading.....</h2>
  }

  if (error) {
    return <h2 style={{ color: 'red' }}>{error}</h2>
  }

  return (
    <>
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
    </>
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
    border: "1px solid #dfe1e5",
    borderRadius: "10px",
    marginLeft: "5px",
    width: "400px",
    maxWidth: "224px",
    boxShadow: "none",
    border: "1px solid grey"
  },

  searchbarWrapper: {
    flex: 1,
    display: "flex",
    padding: "5px 8px 0 14px",
  },

  searchbarLeft: {
    fontSize: "14px",
    fontFamily: "Arial, sans-serif",
    color: "#202124",
    display: "flex",
    alignItems: "center",
    paddingRight: "13px",
    marginTop: "-5px",
  },

  searchIconWrapper: {
    margin: "auto",
  },

  searchIcon: {
    marginTop: "3px",
    color: "#9aa0a6",
    height: "20px",
    lineHeight: "20px",
    width: "20px",
  },

  searchbarIcon: {
    display: "inline-block",
    fill: "currentColor",
    height: "24px",
    lineHeight: "24px",
    position: "relative",
    width: "24px",
  },

  searchbarCenter: {
    display: "flex",
    flex: 1,
    flexWrap: "wrap",
  },

  searchbarInputSpacer: {
    color: "transparent",
    flex: "100%",
    whiteSpace: "pre",
    height: "34px",
    fontSize: "16px",
  },

  searchbarInput: {
    backgroundColor: "transparent",
    border: "none",
    margin: 0,
    padding: 0,
    color: "rgba(0, 0, 0, 0.87)",
    wordWrap: "break-word",
    outline: "none",
    display: "flex",
    flex: "100%",
    marginTop: "-37px",
    height: "34px",
    fontSize: "16px",
    maxWidth: "100%",
    width: "100%",
  },
};

export default HomePage