import { useState } from "react";

function StudentProfile() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [semester, setSemester] = useState("");
  return (
    <div>
      <h2>Student Profile</h2>
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="text"
        placeholder="Semester"
        value={semester}
        onChange={(e) => setSemester(e.target.value)}
      />
    </div>
  );
}

export default StudentProfile;