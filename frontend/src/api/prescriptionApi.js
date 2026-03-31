import axiosInstance from './axiosInstance';

export const getMyPrescriptions = async () => {
  const res = await axiosInstance.get('/api/prescriptions/my');
  return res.data;
};

export const createPrescription = async (payload) => {
  const res = await axiosInstance.post('/api/prescriptions', payload);
  return res.data;
};
