import { useState } from 'react';
import { bookAppointment } from '../api/appointmentApi';

export default function BookAppointment() {
  const [doctorId, setDoctorId] = useState('');
  const [appointmentTime, setAppointmentTime] = useState('');
  const [message, setMessage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await bookAppointment({ doctor_id: doctorId.trim(), appointment_time: new Date(appointmentTime).toISOString() });
      setMessage({ type: 'success', text: 'Appointment booked successfully' });
      setDoctorId('');
      setAppointmentTime('');
    } catch (err) {
      setMessage({ type: 'error', text: err?.response?.data?.detail || 'Failed to book appointment' });
    }
  };

  return (
    <div className="page">
      <h2>Book Appointment</h2>
      <form onSubmit={handleSubmit} className="form">
        <input value={doctorId} onChange={(e) => setDoctorId(e.target.value)} placeholder="Doctor ID" required />
        <input type="datetime-local" value={appointmentTime} onChange={(e) => setAppointmentTime(e.target.value)} required />
        <button type="submit">Book</button>
      </form>
      {message && <p className={message.type === 'error' ? 'error' : 'success'}>{message.text}</p>}
    </div>
  );
}
