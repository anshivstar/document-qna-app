import  { useState } from 'react';
import UploadForm from '../components/UploadForm';
import QuestionBox from '../components/QuestionBox';


const HomePage = () => {
  const [answer, setAnswer] = useState('');

  return (
    <div className="min-h-screen bg-gray-50 p-4 text-gray-800">
      <div className="max-w-3xl mx-auto space-y-8">
        <h1 className="text-3xl font-bold text-center">📄 Document Q&A App</h1>
        <UploadForm />
        <QuestionBox setAnswer={setAnswer} />
        {answer && (
          <div className="bg-white shadow p-4 rounded-md border">
            <h2 className="font-semibold mb-2">Answer:</h2>
            <p className="whitespace-pre-line text-gray-700">{answer}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default HomePage;