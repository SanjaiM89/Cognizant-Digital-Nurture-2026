import React from 'react'

const Header = (props) => {
  <header>
    <h1>{props.title}</h1>
    <div className="hamburger"> =Menu </div>
    <nav>
      <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#course">Courses</a></li>
        <li><a href="#profile">Profile</a></li>
      </ul>
    </nav>
  </header>
}

export default Header;