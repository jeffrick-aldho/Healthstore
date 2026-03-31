import { useEffect, useState } from 'react';
import { getMyAppointments, updateAppointmentStatus } from '../api/appointmentApi';
import AppointmentCard from '../components/AppointmentCard';

export default function MyAppointments() {
  const [appointments, setAppointments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const load = async () => {
    try {
      const data = await getMyAppointments();
      setAppointments(data || []);
    } catch (err) {
      setError(err?.response?.data?.detail || 'Unable to load appointments');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    load();
  }, []);

  const onStatusChange = async (id, status) => {
    try {
      await updateAppointmentStatus(id, status);
      await load();
    } catch (err) {
      alert('Unable to update status.');
    }
  };

  if (loading) return <p>Loading appointments...</p>;
  if (error) return <p className="error">{error}</p>;

  return (
    <div className="page">
      <h2>My Appointments</h2>
      {appointments.length === 0 ? (
        <p>No appointments found.</p>
      ) : (
        appointments.map((appointment) => (
          <AppointmentCard key={appointment.id} appointment={appointment} onStatusChange={(status) => onStatusChange(appointment.id, status)} />
        ))
      )}
    </div>
  );
}
