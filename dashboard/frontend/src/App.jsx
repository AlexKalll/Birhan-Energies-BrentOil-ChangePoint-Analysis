// Filename: src/App.jsx

import React, { useState, useEffect } from 'react';
import Chart from './Chart.jsx';

const App = () => {
  const [data, setData] = useState([]);
  const [events, setEvents] = useState([]);
  const [changePointDate, setChangePointDate] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const pricesResponse = await fetch('http://localhost:3000/api/data');
        if (!pricesResponse.ok) throw new Error('Failed to fetch prices data');
        const pricesResult = await pricesResponse.json();
        
        const eventsResponse = await fetch('http://localhost:3000/api/events');
        if (!eventsResponse.ok) throw new Error('Failed to fetch events data');
        const eventsResult = await eventsResponse.json();

        const processedPrices = pricesResult.prices.map(item => ({
          ...item,
          Date: new Date(item.Date).getFullYear(),
        }));
        
        const processedEvents = eventsResult.map(event => ({
          ...event,
          Date: new Date(event.Date),
        }));

        setData(processedPrices);
        setEvents(processedEvents);
        setChangePointDate(pricesResult.change_point_date);

        // Initialize date range with full data range
        if (processedPrices.length > 0) {
          const years = processedPrices.map(item => item.Date);
          setStartDate(Math.min(...years).toString());
          setEndDate(Math.max(...years).toString());
        }
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div className="flex justify-center items-center h-screen bg-gray-100 text-gray-800">Loading...</div>;
  if (error) return <div className="flex justify-center items-center h-screen bg-red-100 text-red-800">Error: {error}</div>;

  const handleStartDateChange = (e) => {
    setStartDate(e.target.value);
  };

  const handleEndDateChange = (e) => {
    setEndDate(e.target.value);
  };

  const filteredData = data.filter(item => {
    const itemYear = item.Date;
    const startYear = parseInt(startDate);
    const endYear = parseInt(endDate);
    return itemYear >= startYear && itemYear <= endYear;
  });

  const filteredEvents = events.filter(event => {
    const eventYear = event.Date.getFullYear();
    const startYear = parseInt(startDate);
    const endYear = parseInt(endDate);
    return eventYear >= startYear && eventYear <= endYear;
  });

  return (
    <div className="min-h-screen bg-gray-100 p-8 flex flex-col items-center">
      <h1 className="text-4xl font-bold text-gray-800 mb-6 text-center">
        Brent Oil Price Change Point Analysis
      </h1>
      <p className="text-lg text-gray-600 mb-8 text-center max-w-2xl">
        This dashboard visualizes the monthly Brent oil price, highlighting a statistically
        significant change point detected by a Bayesian model and comparing it with
        key historical events.
      </p>
      <div className="flex space-x-4 mb-6">
        <label className="flex flex-col">
          Start Year:
          <input
            type="number"
            value={startDate}
            onChange={handleStartDateChange}
            className="mt-1 p-2 border border-gray-300 rounded-md"
          />
        </label>
        <label className="flex flex-col">
          End Year:
          <input
            type="number"
            value={endDate}
            onChange={handleEndDateChange}
            className="mt-1 p-2 border border-gray-300 rounded-md"
          />
        </label>
      </div>
      <Chart data={filteredData} events={filteredEvents} changePointDate={changePointDate} />
    </div>
  );
};

export default App;
