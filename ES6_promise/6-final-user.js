import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((responses) => {
    responses.forEach((res) => {
      if (res.status === 'rejected') {
        res.value = `Error: ${res.reason.message}`;
        delete res.reason;
      }
    });
    return responses;
  });
}
