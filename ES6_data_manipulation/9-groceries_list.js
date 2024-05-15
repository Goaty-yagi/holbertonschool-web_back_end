export default function groceriesList() {
  const map = new Map();
  const groceriesL = [
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5],
  ];
  groceriesL.forEach((e) => {
    map.set(e[0], e[1]);
  });
  return map;
}
