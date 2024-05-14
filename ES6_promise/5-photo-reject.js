export default function uploadPhoto(filename) {
  if (typeof filename !== 'string') {
    return {};
  }
  return new Promise((resolve, reject) => {
    reject(new Error(`${filename} cannot be processed`));
  });
}
