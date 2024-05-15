export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  let concatString = '';
  const len = startString.length;
  set.forEach((e) => {
    if (e.startsWith(startString)) {
      if (concatString) {
        concatString = `${concatString}-${e.slice(len, e.length)}`;
      } else {
        concatString += e.slice(len, e.length);
      }
    }
  });
  return concatString;
}
