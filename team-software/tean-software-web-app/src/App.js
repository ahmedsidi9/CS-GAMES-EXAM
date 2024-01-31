import logo from './logo.svg';
import './App.css';
import HomePage from './pages/HomePages';
import UploadPage from './pages/UploadPages';
import TreeListPage from './pages/TreeListPages';
import AboutPage from './pages/AboutPages';

function App() {
  return (
  <div>
  
    <div class="hidden sm:block">
      <nav class="flex gap-6" aria-label="Tabs">
        <a
          href="#"
          class="shrink-0 rounded-lg p-2 text-sm font-medium text-gray-500 hover:bg-gray-50 hover:text-gray-700"
        >
          Home
        </a>
  
        <a
          href="#"
          class="shrink-0 rounded-lg p-2 text-sm font-medium text-gray-500 hover:bg-gray-50 hover:text-gray-700"
        >
          Upload
        </a>
  
        <a
          href="#"
          class="shrink-0 rounded-lg p-2 text-sm font-medium text-gray-500 hover:bg-gray-50 hover:text-gray-700"
        >
          TreeList
        </a>
  
        <a
          href="#"
          class="shrink-0 rounded-lg bg-gray-100 p-2 text-sm font-medium text-gray-700"
          aria-current="page"
        >
          About
        </a>
      </nav>
    </div>
  </div>
  );
}

export default App;
