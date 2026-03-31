import { useEffect, useState } from 'react';
import { getMyPrescriptions } from '../api/prescriptionApi';
import PrescriptionCard from '../components/PrescriptionCard';

export default function Prescriptions() {
  const [prescriptions, setPrescriptions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const load = async () => {
      try {
        const data = await getMyPrescriptions();
        setPrescriptions(data || []);
      } catch (err) {
        setError(err?.response?.data?.detail || 'Unable to load prescriptions');
      } finally {
        setLoading(false);
      }
    };
    load();
  }, []);

  if (loading) return <p>Loading prescriptions...</p>;
  if (error) return <p className="error">{error}</p>;

  return (
    <div className="page">
      <h2>My Prescriptions</h2>
      {prescriptions.length === 0 ? (
        <p>No prescriptions available.</p>
      ) : (
        prescriptions.map((p) => <PrescriptionCard key={p.id} prescription={p} />)
      )}
    </div>
  );
}
