import React from 'react';

const LanguageSelector = ({ setLanguage }) => {
  const changeLanguage = (lang) => {
    setLanguage(lang);
  };

  return (
    <div>
      <button onClick={() => changeLanguage('en')}>English</button>
      <button onClick={() => changeLanguage('ru')}>Русский</button>
    </div>
  );
};

export default LanguageSelector;
