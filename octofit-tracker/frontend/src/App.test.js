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
  expect(screen.getByRole('link', { name: /^Activities$/i })).toBeInTheDocument();
  expect(screen.getByRole('link', { name: /^Leaderboard$/i })).toBeInTheDocument();
  expect(screen.getByRole('link', { name: /^Teams$/i })).toBeInTheDocument();
  expect(screen.getByRole('link', { name: /^Users$/i })).toBeInTheDocument();
  expect(screen.getByRole('link', { name: /^Workouts$/i })).toBeInTheDocument();
});
