<template>
  <div class="fixed inset-0 z-[-1] overflow-hidden bg-gradient-to-b from-[#0F172A] via-[#1E293B] to-[#334155]">
    <!-- Central Radial Highlight -->
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(255,255,255,0.03),transparent_70%)]" />

    <!-- Clouds Layer 1 (Back) -->
    <div 
      class="absolute top-[10%] left-[-10%] w-[120%] h-[50%] bg-white/5 blur-[120px] rounded-[100%] animate-cloud-drift-1" 
    />

    <!-- Clouds Layer 2 (Mid) -->
    <div 
      class="absolute top-[30%] right-[-10%] w-[100%] h-[40%] bg-white/10 blur-[90px] rounded-[100%] animate-cloud-drift-2" 
    />

    <!-- Clouds Layer 3 (Front) -->
    <div 
      class="absolute top-[55%] left-[5%] w-[90%] h-[35%] bg-white/15 blur-[60px] rounded-[100%] animate-cloud-drift-3" 
    />
    
    <!-- Atmosphere Filter -->
    <div class="absolute inset-0 backdrop-blur-[2px] pointer-events-none" />
  </div>
</template>

<script setup lang="ts">
// Dream Background Component
</script>

<style scoped>
/* Tailwind v4 animation classes are picked up from main.css */
</style>
