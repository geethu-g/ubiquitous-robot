import React from 'react';

const OctofitCard = ({ title, children, className = '' }) => (
  <div className={`card mb-4 ${className}`}>
    <div className="card-body">
      {title && <h2 className="card-title mb-4">{title}</h2>}
      {children}
    </div>
  </div>
);

export default OctofitCard;
