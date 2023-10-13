import React, { useState } from 'react';
import translations from './locates/translation'; // Импорт переводов

const UserForm = ({ translation }) => {

  const [UserData, setUserData] = useState({
    id: '',
    username: '',
    email: '',
    age: '',
    weight: '',
    height:'',
  });

  const handleChange = (u) => {
    const { name, value } = u.target;
    setUserData({ ...UserData, [name]: value });
  };

  const handleSubmit = (u) => {
    u.preventDefault();
    const dataToSend = {
      id: parseInt(UserData.id),
      username: UserData.username,
      email: UserData.email,
      age: parseInt(UserData.age),
      weight: parseInt(UserData.weight),
      height: parseInt(UserData.height),
    };

    console.log('dataToSend:', dataToSend);

    fetch('http://localhost:5000/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dataToSend),
    })
      .then((response) => response.json())
      .then((data) => console.log('Успешно:', data))
      .catch((error) => console.error('Ошибка:', error));
  };

  return (
    <div>
      <label>
        {translation.id}: {/* Используйте переводы */}
        <input
          type="text"
          name="id"
          value={UserData.id}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        {translation.username}:
        <input
          type="text"
          name="username"
          value={UserData.username}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        {translation.date}:
        <input
          type="text"
          name="date"
          value={UserData.date}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        {translation.email}:
        <input
          type="text"
          name="email"
          value={UserData.email}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        {translation.age}:
        <input
          type="text"
          name="age"
          value={UserData.age}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        {translation.weight}:
        <input
          type="text"
          name="weight"
          value={UserData.weight}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        {translation.height}:
        <input
          type="text"
          name="height"
          value={UserData.height}
          onChange={handleChange}
        />
      </label>
      <br />
      <button type="Submit" onClick={handleSubmit}>{translation.submit}</button>
    </div>
  );
};

export default UserForm;
