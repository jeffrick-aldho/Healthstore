import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Dashboard() {
  const { user } = useAuth();

  return (
    <div className="page">
      <h2>Welcome, {user?.name || 'Guest'}</h2>
      <p>Role: {user?.role}</p>
      <div className="grid">
        <Link to="/appointments" className="card">My Appointments</Link>
        <Link to="/prescriptions" className="card">My Prescriptions</Link>
        <Link to="/book" className="card">Book Appointment</Link>
        {user?.role === 'doctor' && <Link to="/doctor" className="card">Doctor Dashboard</Link>}
        {user?.role === 'admin' && <Link to="/admin" className="card">Admin Dashboard</Link>}
      </div>
    </div>
  );
}
