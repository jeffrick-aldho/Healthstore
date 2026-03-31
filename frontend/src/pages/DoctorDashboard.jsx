import { useState } from 'react';
import { createPrescription } from '../api/prescriptionApi';
import { createDoctorProfile } from '../api/doctorApi';

export default function DoctorDashboard() {
  const [doctorProfile, setDoctorProfile] = useState({ specialization: '', bio: '' });
  const [prescription, setPrescription] = useState({ appointment_id: '', notes: '', medicines: [{ name: '', dosage: '', days: 1 }] });
  const [message, setMessage] = useState(null);

  const handleAddMedicine = () => {
    setPrescription((prev) => ({ ...prev, medicines: [...prev.medicines, { name: '', dosage: '', days: 1 }] }));
  };

  const handleMedicineChange = (idx, key, value) => {
    setPrescription((prev) => {
      const next = [...prev.medicines];
      next[idx] = { ...next[idx], [key]: value };
      return { ...prev, medicines: next };
    });
  };

  const handleProfileSubmit = async (e) => {
    e.preventDefault();
    try {
      await createDoctorProfile(doctorProfile);
      setMessage({ type: 'success', text: 'Doctor profile created.' });
    } catch (err) {
      setMessage({ type: 'error', text: err?.response?.data?.detail || 'Unable to create profile' });
    }
  };

  const handlePrescriptionSubmit = async (e) => {
    e.preventDefault();
    try {
      await createPrescription(prescription);
      setMessage({ type: 'success', text: 'Prescription created.' });
    } catch (err) {
      setMessage({ type: 'error', text: err?.response?.data?.detail || 'Unable to create prescription' });
    }
  };

  return (
    <div className="page">
      <h2>Doctor Dashboard</h2>
      <section className="card">
        <h3>Doctor Profile</h3>
        <form onSubmit={handleProfileSubmit} className="form">
          <input value={doctorProfile.specialization} onChange={(e) => setDoctorProfile((s) => ({ ...s, specialization: e.target.value }))} placeholder="Specialization" required />
          <textarea value={doctorProfile.bio} onChange={(e) => setDoctorProfile((s) => ({ ...s, bio: e.target.value }))} placeholder="Bio" rows={3} />
          <button type="submit">Save Profile</button>
        </form>
      </section>

      <section className="card">
        <h3>Write Prescription</h3>
        <form onSubmit={handlePrescriptionSubmit} className="form">
          <input value={prescription.appointment_id} onChange={(e) => setPrescription((s) => ({ ...s, appointment_id: e.target.value }))} placeholder="Appointment ID" required />
          <textarea value={prescription.notes} onChange={(e) => setPrescription((s) => ({ ...s, notes: e.target.value }))} placeholder="Notes" rows={3} required />
          <h4>Medicines</h4>
          {prescription.medicines.map((m, idx) => (
            <div key={idx} className="grid-sm">
              <input placeholder="Name" value={m.name} onChange={(e) => handleMedicineChange(idx, 'name', e.target.value)} required />
              <input placeholder="Dosage" value={m.dosage} onChange={(e) => handleMedicineChange(idx, 'dosage', e.target.value)} required />
              <input type="number" min="1" value={m.days} onChange={(e) => handleMedicineChange(idx, 'days', Number(e.target.value))} required />
            </div>
          ))}
          <button type="button" onClick={handleAddMedicine}>Add Medicine</button>
          <button type="submit">Create Prescription</button>
        </form>
      </section>
      {message && <p className={message.type === 'error' ? 'error' : 'success'}>{message.text}</p>}
    </div>
  );
}
