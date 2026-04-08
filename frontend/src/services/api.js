import axios from "axios";

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
  headers: {
    "Content-Type": "application/json",
  },
});

export const appAPI = {
  getText() {
    return apiClient.get("/text");
  },
  getClicks() {
    return apiClient.get("/click");
  },
  incrementClick() {
    return apiClient.post("/click");
  },
  initUser() {
    return apiClient.post("/user/init");
  },
};
