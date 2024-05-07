import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const results = [];
  const args = [19, 20, 34];
  for (let i = 0; i < 3; i += 1) {
    results.push(new ClassRoom(args[i]));
  }
  return results;
}
