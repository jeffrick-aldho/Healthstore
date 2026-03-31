import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Navbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav className="navbar">
      <div className="brand">HealthCare App</div>
      <div>
        <Link to="/">Dashboard</Link>
        <Link to="/appointments">Appointments</Link>
        <Link to="/prescriptions">Prescriptions</Link>
        {user?.role === 'doctor' && <Link to="/doctor">Doctor</Link>}
        {user?.role === 'admin' && <Link to="/admin">Admin</Link>}
        {user ? <button onClick={handleLogout}>Logout</button> : <Link to="/login">Login</Link>}
      </div>
    </nav>
  );
}
