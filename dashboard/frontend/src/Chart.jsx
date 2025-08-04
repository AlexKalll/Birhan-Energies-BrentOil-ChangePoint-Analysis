// Filename: src/Chart.jsx

import React from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
  ReferenceLine,
  ReferenceDot,
} from 'recharts';

const Chart = ({ data, events, changePointDate }) => {
  const changePointIndex = data.findIndex(item => item.Date === new Date(changePointDate).getFullYear());

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 w-full max-w-6xl">
      <h2 className="text-2xl font-semibold text-gray-700 mb-4">
        Monthly Oil Prices with Inferred Change Point
      </h2>
      <ResponsiveContainer width="100%" height={500}>
        <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#e0e0e0" />
          <XAxis dataKey="Date" tickFormatter={(value) => value} />
          <YAxis label={{ value: 'Price (USD)', angle: -90, position: 'insideLeft' }} />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="Price" stroke="#3b82f6" activeDot={{ r: 8 }} />
          
          {changePointIndex !== -1 && (
            <ReferenceLine x={data[changePointIndex].Date} stroke="red" strokeDasharray="5 5" label="Change Point" />
          )}

          {events.map((event, index) => {
            const eventDataPoint = data.find(d => d.Date === event.Date.getFullYear());
            return eventDataPoint ? (
              <ReferenceDot 
                key={index} 
                x={eventDataPoint.Date} 
                y={eventDataPoint.Price} 
                r={6} 
                fill="#10b981" 
                stroke="#10b981" 
                className="cursor-pointer"
              >
                <Tooltip />
                <div style={{ pointerEvents: 'none' }}>{event.Event}</div>
              </ReferenceDot>
            ) : null;
          })}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default Chart;
