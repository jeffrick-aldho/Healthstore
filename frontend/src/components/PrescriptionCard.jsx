export default function PrescriptionCard({ prescription }) {
  return (
    <div className="card">
      <p>ID: {prescription.id}</p>
      <p>Appointment: {prescription.appointment_id}</p>
      <p>Doctor: {prescription.doctor_id}</p>
      <p>Notes: {prescription.notes}</p>
      <ul>
        {prescription.medicines.map((item, index) => (
          <li key={index}>{item.name} ({item.dosage}) x{item.days} days</li>
        ))}
      </ul>
    </div>
  );
}
