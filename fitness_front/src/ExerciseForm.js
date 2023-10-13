import React, { useState } from 'react';
import translations from './locates/translation'; // Импорт переводов

const ExerciseForm = ({ translation }) => {

  const [exerciseData, setExerciseData] = useState({
    exercise_id: '',
    user_id: '',
    exercise_type: '',
    duration: '',
    date: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setExerciseData({ ...exerciseData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const dataToSend = {
      exercise_id: parseInt(exerciseData.exercise_id),
      user_id: parseInt(exerciseData.user_id),
      exercise_type: exerciseData.exercise_type,
      duration: parseInt(exerciseData.duration),
      date: exerciseData.date,
    };

    console.log('dataToSend:', dataToSend);

    fetch('http://localhost:5000/exercises', {
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
        {translation.exerciseType}: {/* Используйте переводы */}
        <input
          type="text"
          name="exercise_type"
          value={exerciseData.exercise_type}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        {translation.duration}:
        <input
          type="text"
          name="duration"
          value={exerciseData.duration}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        {translation.date}:
        <input
          type="text"
          name="date"
          value={exerciseData.date}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        {translation.exerciseId}:
        <input
          type="text"
          name="exercise_id"
          value={exerciseData.exercise_id}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        {translation.userId}:
        <input
          type="text"
          name="user_id"
          value={exerciseData.user_id}
          onChange={handleChange}
        />
      </label>
      <br />
      <button type="Submit" onClick={handleSubmit}>{translation.submit}</button>
    </div>
  );
};

export default ExerciseForm;
