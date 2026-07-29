import { useSelector, useDispatch } from 'react-redux'
import StudentProfile from './StudentProfile'
import { unenroll } from '../store/enrollmentSlice'

const ProfilePage = () => {
  const enrolledCourses = useSelector((state) => state.enrollment.enrolledCourses)
  const dispatch = useDispatch()

  return (
    <div>
      <StudentProfile />
      <h2>Enrolled Courses ({enrolledCourses.length})</h2>
      {enrolledCourses.length === 0 ? (
        <p>No courses enrolled yet.</p>
      ) : (
        <ul>
          {enrolledCourses.map((course) => (
            <li key={course.id}>
              {course.name} ({course.code})
              <button onClick={() => dispatch(unenroll(course.id))} style={{ marginLeft: '10px' }}>
                Remove
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

export default ProfilePage
