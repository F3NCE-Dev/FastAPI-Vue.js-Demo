<script setup>
import { ref, onMounted } from "vue";
import { appAPI } from "../services/api.js";

const clickCount = ref(0);
const isLoading = ref(false);

const fetchClicks = async () => {
  try {
    const response = await appAPI.getClicks();
    clickCount.value = response.data;
  } catch (error) {
    console.error("Error fetching clicks:", error);
  }
};

const handleIncrement = async () => {
  if (isLoading.value) return;
  isLoading.value = true;
  try {
    await appAPI.incrementClick();
    await fetchClicks();
  } catch (error) {
    console.error("Error incrementing click:", error);
  } finally {
    isLoading.value = false;
  }
};

onMounted(() => {
  fetchClicks();
});
</script>

<template>
  <div class="min-h-screen flex items-center justify-center">
    <div
      class="bg-gray-900 border border-gray-700 rounded-2xl shadow-2xl p-8 w-[600px] max-w-full text-center"
    >
      <h1 class="text-2xl mb-6 text-green-400 tracking-wide">Click Counter</h1>

      <div class="bg-black rounded-lg p-10 border border-gray-800 mb-8">
        <span class="text-6xl font-mono text-gray-200">
          {{ clickCount }}
        </span>
      </div>

      <button
        @click="handleIncrement"
        :disabled="isLoading"
        class="w-full px-6 py-4 bg-gray-800 border border-gray-600 rounded-xl hover:bg-gray-700 active:scale-95 transition-all text-xl text-green-400 font-semibold disabled:opacity-50 cursor-pointer"
      >
        {{ isLoading ? "Processing..." : "CLICK ME" }}
      </button>

      <router-link to="/" class="inline-block mt-6 text-gray-500 hover:text-gray-300 transition">
        ← Back to Home
      </router-link>
    </div>
  </div>
</template>
