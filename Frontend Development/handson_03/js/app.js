import { courses } from "./data.js"

courses.forEach(
  ({ name, credits }) => {
    console.log(`Name:${name}, Credits:${credits}`);
  }
);