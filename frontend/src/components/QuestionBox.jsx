// frontend/src/components/QuestionBox.jsx
import React, { useState } from 'react';
import axios from 'axios';

export default function QuestionBox({ setAnswer }) {
  const [question, setQuestion] = useState('');
  const [loading, setLoading] = useState(false);

  const handleAsk = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;
    setLoading(true);

    const formData = new FormData();
    formData.append('question', question);

    try {
      const res = await axios.post('http://localhost:8000/query', formData);
      setAnswer(res.data.answer);
    } catch (err) {
      console.error(err);
      setAnswer('❌ Failed to get an answer.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form
      onSubmit={handleAsk}
      className="bg-white rounded-lg shadow-md p-6 space-y-4 border"
    >
      <h2 className="text-xl font-semibold">❓ Ask a Question</h2>

      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="e.g. What is the candidate's name?"
        className="w-full border border-gray-300 rounded-md p-2 text-sm focus:outline-none focus:ring focus:border-indigo-400"
      />

      <button
        type="submit"
        disabled={loading}
        className="bg-indigo-600 text-white px-4 py-2 rounded-md shadow hover:bg-indigo-700 transition disabled:opacity-50"
      >
        {loading ? 'Searching...' : 'Get Answer'}
      </button>
    </form>
  );
}
