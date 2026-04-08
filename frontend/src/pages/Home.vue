<template>
  <div class="min-h-screen flex flex-col items-center justify-center gap-6">
    <h1 class="text-3xl text-gray-200">Welcome</h1>

    <router-link
      to="/text"
      class="px-6 py-3 bg-gray-800 border border-gray-600 rounded-lg hover:bg-gray-700 transition text-lg"
    >
      Open Text Viewer
    </router-link>

    <router-link
      to="/clicks"
      class="px-6 py-3 bg-gray-800 border border-gray-600 rounded-lg hover:bg-gray-700 transition text-lg"
    >
      Open Click Counter
    </router-link>
  </div>
</template>
