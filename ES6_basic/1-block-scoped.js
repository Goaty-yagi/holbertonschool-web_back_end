export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true; // assigned a value but never used
    const task2 = false; // assigned a value but never used
  }

  return [task, task2];
}
