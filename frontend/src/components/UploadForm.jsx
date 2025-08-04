// frontend/src/components/UploadForm.jsx
import  { useState } from 'react';
import axios from 'axios';

export default function UploadForm() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('');

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      setStatus('Please select a file first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      setStatus('Uploading...');
      const res = await axios.post('http://localhost:8000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setStatus(`✅ ${res.data.message} (${res.data.chunks} chunks)`);
    } catch (error) {
      console.error(error);
      setStatus('❌ Upload failed.');
    }
  };

  return (
    <form
      onSubmit={handleUpload}
      className="bg-white rounded-lg shadow-md p-6 space-y-4 border"
    >
      <h2 className="text-xl font-semibold">📤 Upload PDF</h2>

      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="block w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100 cursor-pointer"
      />

      <button
        type="submit"
        className="bg-indigo-600 text-white px-4 py-2 rounded-md shadow hover:bg-indigo-700 transition"
      >
        Upload
      </button>

      {status && <p className="text-sm text-gray-700">{status}</p>}
    </form>
  );
}
