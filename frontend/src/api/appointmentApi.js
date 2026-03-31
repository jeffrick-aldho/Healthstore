import axiosInstance from './axiosInstance';

export const bookAppointment = async (payload) => {
  const res = await axiosInstance.post('/api/appointments', payload);
  return res.data;
};

export const getMyAppointments = async () => {
  const res = await axiosInstance.get('/api/appointments/my');
  return res.data;
};

export const updateAppointmentStatus = async (appointmentId, status) => {
  const res = await axiosInstance.put(`/api/appointments/${appointmentId}`, { status });
  return res.data;
};
