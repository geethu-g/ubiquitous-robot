import { render, screen } from '@testing-library/react';
import App from './App';

test('renders Octofit Tracker brand in navbar', () => {
  render(<App />);
  const brandElements = screen.getAllByText(/Octofit Tracker/i);
  expect(brandElements.length).toBeGreaterThan(0);
});

test('renders welcome message on home page', () => {
  render(<App />);
  expect(screen.getByText(/Welcome to/i)).toBeInTheDocument();
});

test('renders navigation links', () => {
  render(<App />);
  expect(screen.getByText(/Activities/i)).toBeInTheDocument();
  expect(screen.getByText(/Leaderboard/i)).toBeInTheDocument();
  expect(screen.getByText(/Teams/i)).toBeInTheDocument();
  expect(screen.getByText(/Users/i)).toBeInTheDocument();
  expect(screen.getByText(/Workouts/i)).toBeInTheDocument();
});
