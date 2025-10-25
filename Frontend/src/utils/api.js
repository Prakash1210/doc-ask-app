import axios from "axios";

const api = axios.create({
  baseURL: "/api",
});

export const uploadFile = (data) =>
  api.post("/upload", data, {
    headers: { "Content-Type": "multipart/form-data" },
  });

export const sendQuery = (query) => api.post("/chat", { query });

export default api;
