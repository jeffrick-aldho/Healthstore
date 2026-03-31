import { createContext, useContext, useEffect, useState } from 'react';
import { login as apiLogin, register as apiRegister, getMe } from '../api/authApi';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) {
      setLoading(false);
      return;
    }

    const fetchUser = async () => {
      try {
        const data = await getMe(token);
        setUser(data);
      } catch (error) {
        console.error('Session invalid', error);
        setToken(null);
        localStorage.removeItem('token');
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, [token]);

  const login = async (credentials) => {
    const data = await apiLogin(credentials);
    if (!data?.access_token) throw new Error('Login failed');
    localStorage.setItem('token', data.access_token);
    setToken(data.access_token);
    const profile = await getMe(data.access_token);
    setUser(profile);
    return profile;
  };

  const register = async (payload) => {
    return await apiRegister(payload);
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, token, login, register, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
