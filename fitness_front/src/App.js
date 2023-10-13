import React, { useState } from 'react';
import ExerciseForm from './ExerciseForm';
import LanguageSelector from './LanguageSelector';
import translations from './locates/translation';
import UserForm from "./UserForm";

function App() {
  const [language, setLanguage] = useState('ru');

  return (
    <div>

      <LanguageSelector setLanguage={setLanguage} />
      <ExerciseForm translation={translations[language]} />
      <UserForm translation = {translations[language]} />
    </div>
  );
}

export default App;
