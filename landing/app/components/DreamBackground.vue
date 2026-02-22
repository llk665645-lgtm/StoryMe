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

    <!-- Dreamy Clouds Layer - Increased density and variety -->
    <div class="absolute inset-0 pointer-events-none opacity-40">
      <div 
        v-for="i in 16" 
        :key="`cloud-${i}`"
        class="absolute blur-[30px] sm:blur-[50px]"
        :class="[
          i % 3 === 0 ? 'animate-drift-slow-1' : '',
          i % 3 === 1 ? 'animate-drift-slow-2' : '',
          i % 3 === 2 ? 'animate-drift-slow-3' : '',
        ]"
        :style="{
          top: `${Math.random() * 95}%`,
          left: `${Math.random() * 120 - 60}%`,
          width: i % 2 === 0 ? `${150 + Math.random() * 200}px` : `${350 + Math.random() * 450}px`,
          aspectRatio: '3/2',
          background: i % 2 === 0 
            ? 'radial-gradient(circle at center, rgba(167, 139, 250, 0.25) 0%, rgba(139, 92, 246, 0) 70%)' 
            : 'radial-gradient(circle at center, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0) 70%)',
          borderRadius: '100%',
          animationDelay: `${-Math.random() * 150}s`,
          animationDuration: `${100 + Math.random() * 100}s`
        }"
      ></div>
    </div>
    
    <!-- Decorative magical nebulae (Violet/Pink) -->
    <div class="absolute top-0 right-0 w-[600px] h-[600px] bg-purple-600/10 blur-[180px] rounded-full -translate-y-1/2 translate-x-1/2"></div>
    <div class="absolute bottom-0 left-0 w-[800px] h-[800px] bg-pink-600/10 blur-[200px] rounded-full translate-y-1/3 -translate-x-1/4"></div>
  </div>
</template>

<script setup lang="ts">
// Enhanced Magical Dream Background
</script>

<style scoped>
/* Animations are defined in main.css */
</style>
