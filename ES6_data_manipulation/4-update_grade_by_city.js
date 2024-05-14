export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const updatedStudent = { ...student };
      const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
      updatedStudent.grade = gradeObj ? gradeObj.grade : 'N/A';
      return updatedStudent;
    });
}
