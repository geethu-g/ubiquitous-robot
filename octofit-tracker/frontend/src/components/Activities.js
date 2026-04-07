import React, { useEffect, useState } from 'react';
import OctofitCard from './OctofitCard';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const endpoint = `${process.env.REACT_APP_CODESPACE_NAME ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/` : '/api/activities/'}`;

  useEffect(() => {
    console.log('Fetching Activities from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched Activities:', results);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [endpoint]);

  return (
    <OctofitCard title="Activities">
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead className="table-dark">
            <tr>
              {activities.length > 0 && Object.keys(activities[0]).map((key) => (
                <th key={key}>{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {activities.map((activity, idx) => (
              <tr key={activity.id || idx}>
                {activities.length > 0 && Object.keys(activities[0]).map((key) => (
                  <td key={key}>{String(activity[key])}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </OctofitCard>
  );
};

export default Activities;
