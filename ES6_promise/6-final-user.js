import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((responses) => responses.map((res) => {
    const key = res.status === 'rejected' ? 'error' : 'value';
    const val = res.status === 'rejected' ? res.reason.message : res.value;
    return { status: res.status, [key]: val };
  }));
}
