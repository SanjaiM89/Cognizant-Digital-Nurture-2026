import React from 'react'


const Header = (props) =>{
return(
  <header style={styles.header}>
    <h1 style={styles.title}>{props.title}</h1>
    <div style={styles.hamburger}> =Menu </div>
    <nav style={styles.nav}>
      <ul style={styles.navList}>
        <li><a href="#home" style={styles.link}>Home</a></li>
        <li><a href="#course" style={styles.link}>Courses</a></li>
        <li><a href="#profile" style={styles.link}>Profile</a></li>
        <li style={styles.enrolled}>Enrolled Course: {props.enrollCount}</li>
      </ul>
    </nav>
  </header>
)
}

const styles = {
    header: {
        padding: "20px 40px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        backgroundColor: "#2c3e50",
        color: "#fff",
    },
    title: {
        fontSize: '2rem',
        marginBottom: '10px'
    },
    nav: {
        display: 'block'
    },
    navList: {
        listStyle: 'none',
        display: 'flex',
        gap: '30px',
        alignItems: 'center',
        flexDirection: 'row',
        padding: 0,
        margin: 0
    },
    link: {
        textDecoration: 'none',
        color: '#fff',
        paddingBottom: "5px",
        borderBottom: "2px solid transparent",
        transition: "border-color 0.3s ease",
    },
    hamburger: {
        display: 'none',
        fontSize: '1.2rem',
        cursor: 'pointer'
    },
    enrolled: {
        color: '#90cdf4',
        fontWeight: 'bold'
    }
};

export default Header;