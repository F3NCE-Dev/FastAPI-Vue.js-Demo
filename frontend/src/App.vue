<script setup>
import { onMounted } from 'vue';
import { appAPI } from './services/api';

onMounted(async () => {
  try {
    await appAPI.initUser();
    console.log("User initialized or already exists.");
  } catch (error) {
    console.error("Error initializing user:", error);
  }
});
</script>

<template>
  <router-view />
</template>
