<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { appAPI } from "../services/api.js";

const text = ref("");
let intervalId = null;

const fetchText = async () => {
  try {
    const response = await appAPI.getText();
    text.value = response.data.text;
  } catch (error) {
    console.error("Error fetching text:", error);
  }
};

onMounted(() => {
  fetchText();

  intervalId = setInterval(() => {
    fetchText();
  }, 3000);
});

onUnmounted(() => {
  clearInterval(intervalId);
});
</script>

<template>
  <div class="min-h-screen flex items-center justify-center">
    <div
      class="bg-gray-900 border border-gray-700 rounded-2xl shadow-2xl p-8 w-[600px] max-w-full"
    >
      <h1 class="text-2xl mb-6 text-green-400 tracking-wide">API Text</h1>

      <div class="bg-black rounded-lg p-6 border border-gray-800">
        <p class="text-lg leading-relaxed text-gray-200">
          {{ text }}
        </p>
      </div>
    </div>
  </div>
</template>
