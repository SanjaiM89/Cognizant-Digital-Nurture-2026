import { courses } from "./data.js"

courses.forEach(
  ({ name, credits }) => {
    console.log(`Name:${name}, Credits:${credits}`);
  }
);

const course = courses.map(
  course => {
    return `${course.code}-,${course.name} (${course.credits} credits)`
  }
)

console.log(course)

const course_filter = courses.filter(
  course =>   course.credits>-4
)

console.log(`No of courses with credits less than or equal to 4 is ${course.length}`)