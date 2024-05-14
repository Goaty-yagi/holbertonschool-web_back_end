export default function getStudentIdsSum(students) {
  return students.reduce((pre, curr) => pre + curr.id, 0);
}
