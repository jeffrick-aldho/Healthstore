import { Routes, Route } from 'react-router-dom';
import Navbar from '../components/Navbar';
import Login from '../pages/Login';
import Register from '../pages/Register';
import Dashboard from '../pages/Dashboard';
import BookAppointment from '../pages/BookAppointment';
import MyAppointments from '../pages/MyAppointments';
import Prescriptions from '../pages/Prescriptions';
import DoctorDashboard from '../pages/DoctorDashboard';
import AdminDashboard from '../pages/AdminDashboard';
import ProtectedRoute from '../components/ProtectedRoute';

export default function AppRoutes() {
  return (
    <div>
      <Navbar />
      <main>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route element={<ProtectedRoute />}>
            <Route path="/" element={<Dashboard />} />
            <Route path="/book" element={<BookAppointment />} />
            <Route path="/appointments" element={<MyAppointments />} />
            <Route path="/prescriptions" element={<Prescriptions />} />
          </Route>
          <Route element={<ProtectedRoute roles={['doctor']} />}>
            <Route path="/doctor" element={<DoctorDashboard />} />
          </Route>
          <Route element={<ProtectedRoute roles={['admin']} />}>
            <Route path="/admin" element={<AdminDashboard />} />
          </Route>
          <Route path="*" element={<Login />} />
        </Routes>
      </main>
    </div>
  );
}
