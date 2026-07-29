import Header from './components/header'
import Footer from './components/footer'
import { Routes, Route } from 'react-router-dom'
import HomePage from './components/HomePage'
import CoursesPage from './components/CoursesPage'
import ProfilePage from './components/ProfilePage'
import CourseDetailsPage from './components/CourseDetailsPage'

function App() {
  return (
    <div>
      <Header title="Student Portal" />
      <main>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/courses" element={<CoursesPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/courses/:courseId" element={<CourseDetailsPage />} />
        </Routes>
      </main>
      <Footer />
    </div>
  )
}

export default App
