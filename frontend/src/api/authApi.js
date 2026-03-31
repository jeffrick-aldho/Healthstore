import axiosInstance from './axiosInstance';

export const register = async (payload) => {
  const res = await axiosInstance.post('/api/auth/register', payload);
  return res.data;
};

export const login = async (payload) => {
  const res = await axiosInstance.post('/api/auth/login', payload);
  return res.data;
};

export const getMe = async (token) => {
  if (token) {
    return axiosInstance.get('/api/auth/me', { headers: { Authorization: `Bearer ${token}` } }).then((res) => res.data);
  }
  return axiosInstance.get('/api/auth/me').then((res) => res.data);
};
