import apiClient from './apiClient'

export async function getAllCourses() {
  return apiClient.get('/posts')
}

// the backend only exposes GET /posts (no single-course route), so we fetch
// the full list and find the match client-side
export async function getCourseById(id) {
  const courses = await getAllCourses()
  return courses.find((course) => course.id === Number(id))
}

export async function enrollStudent(studentId, courseId) {
  return apiClient.post('/enrollments', { studentId, courseId })
}
