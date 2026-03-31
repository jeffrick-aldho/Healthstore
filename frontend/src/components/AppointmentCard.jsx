export default function AppointmentCard({ appointment, onStatusChange }) {
  return (
    <div className="card">
      <p>ID: {appointment.id}</p>
      <p>Doctor: {appointment.doctor_id}</p>
      <p>Date: {new Date(appointment.appointment_time).toLocaleString()}</p>
      <p>Status: {appointment.status}</p>
      {onStatusChange && (
        <div>
          <button onClick={() => onStatusChange('confirmed')}>Confirm</button>
          <button onClick={() => onStatusChange('completed')}>Complete</button>
          <button onClick={() => onStatusChange('cancelled')}>Cancel</button>
        </div>
      )}
    </div>
  );
}
