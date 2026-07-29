import { Link } from 'react-router-dom'

function HomePage() {
  return (
    <div style={styles.hero}>
      <h1>Welcome to the Student Portal</h1>
      <p>View your enrolled courses, browse the course catalog, and manage your profile.</p>
      <Link to="/courses" style={styles.button}>Explore Courses</Link>
    </div>
  )
}

const styles = {
  hero: {
    textAlign: 'center',
    padding: '60px 20px',
  },
  button: {
    display: 'inline-block',
    marginTop: '20px',
    padding: '10px 24px',
    backgroundColor: '#2c3e50',
    color: '#fff',
    textDecoration: 'none',
    borderRadius: '4px',
  },
}

export default HomePage
