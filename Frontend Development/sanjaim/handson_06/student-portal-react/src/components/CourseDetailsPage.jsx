import { useParams } from "react-router-dom";
import data from "../data";

export default function CourseDetailPage() {
  const { courseId } = useParams();
  const course = data.find((course) => course.id === parseInt(courseId));

  if (!course) {
    return <h2>Course not found</h2>;
  }

  return (
    <div>
      <h1>{course.name}</h1>
      <p>Code: {course.code}</p>
      <p>Credits: {course.credits}</p>
      <p>Grade: {course.grade}</p>
    </div>
  );
}