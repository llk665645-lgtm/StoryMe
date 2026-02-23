<template>
    <div class="fixed inset-0 z-[-1] overflow-hidden bg-[#0A0514]">
    <!-- Deep Dream Violet Gradient -->
    <div class="absolute inset-0 bg-gradient-to-b from-[#0F0A1E] via-[#0A0514] to-[#050209]" />

    <!-- Stars Layer -->
    <div class="absolute inset-0 pointer-events-none">
      <div v-for="i in 150" :key="`star-${i}`" 
        class="absolute rounded-full bg-white shadow-sm"
        :class="i % 3 === 0 ? 'animate-twinkle' : ''"
        :style="{
          top: `${Math.random() * 100}%`,
          left: `${Math.random() * 100}%`,
          width: i % 15 === 0 ? '2px' : '1px',
          height: i % 15 === 0 ? '2px' : '1px',
          opacity: 0.4 + Math.random() * 0.6,
          animationDelay: `${Math.random() * 5}s`,
          animationDuration: `${2 + Math.random() * 3}s`
        }"
      />
    </div>

    <!-- Mini Comet -->
    <div class="absolute top-[-50px] left-[10%] w-[2px] h-[2px] bg-white rounded-full animate-comet pointer-events-none">
      <div class="absolute top-1/2 right-0 w-[40px] h-[1px] bg-gradient-to-l from-white to-transparent -translate-y-1/2" />
    </div>
  </div>
</template>

<script setup lang="ts">
// Enhanced Magical Dream Background
</script>

<style scoped>
/* Animations are defined in main.css */
</style>
