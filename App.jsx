import React, { useState } from 'react';
import './App.css';
import DatabaseConnector from './components/DatabaseConnector';
import DocumentUploader from './components/DocumentUploader';
import QueryPanel from './components/QueryPanel';
import ResultsView from './components/ResultsView';
import MetricsDashboard from './components/MetricsDashboard';

function App() {
  const [connected, setConnected] = useState(false);
  const [schema, setSchema] = useState(null);
  const [queryResults, setQueryResults] = useState(null);
  const [metrics, setMetrics] = useState({
    totalQueries: 0,
    avgResponseTime: 0,
    documentsIndexed: 0
  });

  const handleConnectionSuccess = (schemaData) => {
    setConnected(true);
    setSchema(schemaData);
  };

  const handleQueryResults = (results) => {
    setQueryResults(results);
    // Update metrics
    setMetrics(prev => ({
      ...prev,
      totalQueries: prev.totalQueries + 1
    }));
  };

  const handleDocumentsUploaded = (count) => {
    setMetrics(prev => ({
      ...prev,
      documentsIndexed: prev.documentsIndexed + count
    }));
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1> NLP Query Engine</h1>
        <p>Natural Language Query System for Employee Database</p>
      </header>

      <div className="App-container">
        {/* Database Connection Panel */}
        <section className="panel">
          <DatabaseConnector 
            onConnectionSuccess={handleConnectionSuccess}
            connected={connected}
          />
        </section>

        {connected && (
          <>
            {/* Document Upload Panel */}
            <section className="panel">
              <DocumentUploader onUploadSuccess={handleDocumentsUploaded} />
            </section>

            {/* Query Panel */}
            <section className="panel">
              <QueryPanel 
                schema={schema}
                onQueryResults={handleQueryResults}
              />
            </section>

            {/* Results Display */}
            {queryResults && (
              <section className="panel">
                <ResultsView results={queryResults} />
              </section>
            )}

            {/* Metrics Dashboard */}
            <section className="panel">
              <MetricsDashboard metrics={metrics} />
            </section>
          </>
        )}
      </div>
    </div>
  );
}

export default App;
