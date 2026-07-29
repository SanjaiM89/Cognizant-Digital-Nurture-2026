import { courses } from "./data.js"

const searchInput = document.getElementById('search-courses')
const courseGrid = document.querySelector('.course-grid')
const resultsCount = document.getElementById('course-count')
const selectedCourseEl = document.getElementById('selected-course')

function selectCourse(course) {
  selectedCourseEl.textContent = `Selected: ${course.name} (${course.grade})`
}

function renderCourses(list) {
  courseGrid.innerHTML = ''

  list.forEach((course) => {
    const article = document.createElement('article')
    article.className = 'course-card'
    article.tabIndex = 0
    article.innerHTML = `
      <h3>${course.name}</h3>
      <p>${course.code}</p>
      <p class="credits">Credits: ${course.credits}</p>
    `
    article.addEventListener('click', () => selectCourse(course))
    article.addEventListener('keydown', (event) => {
      if (event.key === 'Enter') {
        selectCourse(course)
      }
    })
    courseGrid.appendChild(article)
  })

  resultsCount.textContent = `${list.length} courses found`
}

searchInput.addEventListener('input', () => {
  const term = searchInput.value.toLowerCase()
  const filtered = courses.filter((course) => course.name.toLowerCase().includes(term))
  renderCourses(filtered)
})

renderCourses(courses)

const hamburger = document.querySelector('.hamburger')
const primaryNav = document.getElementById('primary-nav')

hamburger.addEventListener('click', () => {
  const expanded = hamburger.getAttribute('aria-expanded') === 'true'
  hamburger.setAttribute('aria-expanded', String(!expanded))
  primaryNav.classList.toggle('open')
})

const gradesBody = document.getElementById('grades-body')
courses.forEach((course) => {
  const row = document.createElement('tr')
  row.innerHTML = `<td>${course.name}</td><td>${course.code}</td><td>${course.grade}</td>`
  gradesBody.appendChild(row)
})

const profileForm = document.getElementById('profile-form')
profileForm.addEventListener('submit', (event) => {
  event.preventDefault()
})
