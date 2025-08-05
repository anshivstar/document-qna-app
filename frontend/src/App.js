import './App.css';
import ErrorBoundary from './ErrorBoundary';
import HomePage from './pages/Homepage';

function App() {
  return (
    <ErrorBoundary>
      <HomePage />
    </ErrorBoundary>
  );
}

export default App;
