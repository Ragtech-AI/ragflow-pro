import React from 'react';

function App() {
  return (
    <div className="App">
      <header style={{ padding: '20px', textAlign: 'center' }}>
        <h1>RAGFlow Pro</h1>
        <p>RAGTech Solutions - Comprehensive RAG System Platform</p>
        <div style={{ marginTop: '20px' }}>
          <button onClick={() => fetch('/health').then(r => r.json()).then(console.log)}>
            Test Backend Connection
          </button>
        </div>
      </header>
    </div>
  );
}

export default App;