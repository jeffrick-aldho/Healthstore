import axiosInstance from './axiosInstance';

export const createDoctorProfile = async (payload) => {
  const res = await axiosInstance.post('/api/doctor/profile', payload);
  return res.data;
};

export const getAllDoctorProfiles = async () => {
  // Backend does not expose list endpoint in existing API; placeholder for future.
  return [];
};
