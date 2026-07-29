import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { getCourseById } from "../api/courseApi";

export default function CourseDetailPage() {
  const { courseId } = useParams();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getCourseById(courseId).then((result) => {
      setCourse(result);
      setLoading(false);
    });
  }, [courseId]);

  if (loading) {
    return <h2>Loading.....</h2>;
  }

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
