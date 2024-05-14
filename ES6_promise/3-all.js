import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const photoPromise = uploadPhoto();
  const userPromose = createUser();
  return Promise.all([photoPromise, userPromose])
    .then((responses) => {
      const photo = responses[0];
      const user = responses[1];
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
