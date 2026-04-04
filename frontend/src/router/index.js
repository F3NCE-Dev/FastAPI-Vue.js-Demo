import { createRouter, createWebHistory } from "vue-router";
import Home from "../pages/Home.vue";
import TextViewer from "../pages/TextViewer.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/text",
    name: "TextViewer",
    component: TextViewer,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
