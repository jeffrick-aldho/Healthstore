import { useEffect, useState } from 'react';
import axiosInstance from '../api/axiosInstance';

export default function AdminDashboard() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const loadUsers = async () => {
    try {
      const res = await axiosInstance.get('/api/admin/users');
      setUsers(res.data || []);
    } catch (err) {
      setError(err?.response?.data?.detail || "Can't load users");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadUsers();
  }, []);

  const approveDoctor = async (id) => {
    try {
      await axiosInstance.put(`/api/admin/doctors/${id}/approve`);
      loadUsers();
    } catch {
      alert('Approve doctor failed');
    }
  };

  const deleteUser = async (id) => {
    if (!window.confirm('Delete this user?')) return;
    try {
      await axiosInstance.delete(`/api/admin/users/${id}`);
      loadUsers();
    } catch {
      alert('Delete user failed');
    }
  };

  if (loading) return <p>Loading users...</p>;
  if (error) return <p className="error">{error}</p>;

  return (
    <div className="page">
      <h2>Admin Dashboard</h2>
      <table>
        <thead>
          <tr><th>Name</th><th>Email</th><th>Role</th><th>Approved</th><th>Actions</th></tr>
        </thead>
        <tbody>
          {users.map((u) => (
            <tr key={u.id}>
              <td>{u.name}</td>
              <td>{u.email}</td>
              <td>{u.role}</td>
              <td>{String(u.is_approved)}</td>
              <td>
                {u.role === 'doctor' && !u.is_approved && <button onClick={() => approveDoctor(u.id)}>Approve</button>}
                <button onClick={() => deleteUser(u.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
