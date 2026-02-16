<template>
  <section class="bg-brand-light pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 relative">
      <div class="mx-auto max-w-4xl text-center">
        <div class="flex justify-center">
          <h1 
            ref="titleRef"
            class="text-5xl font-bold tracking-tight text-brand-dark sm:text-7xl text-center justify-center mb-6 opacity-0"
          >
            Your Daily Dose of <br class="hidden sm:block" /> <span class="text-primary italic">Inspiration</span>
          </h1>
        </div>
        <p ref="descriptionRef" class="mt-6 text-xl leading-8 text-brand-gray opacity-0 max-w-2xl mx-auto">
          AI-powered quotes, uniquely crafted for your current state of mind. 
          Transform your mood into actionable wisdom.
        </p>
        
        <div ref="generatorRef" class="opacity-0">
          <QuoteGenerator />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import gsap from 'gsap';
import QuoteGenerator from './QuoteGenerator.vue';

const titleRef = ref<HTMLElement | null>(null);
const descriptionRef = ref<HTMLElement | null>(null);
const generatorRef = ref<HTMLElement | null>(null);

onMounted(() => {
  const tl = gsap.timeline({ delay: 0.2 });
  
  if (titleRef.value) {
    tl.fromTo(titleRef.value, 
      { opacity: 0, y: 30 },
      { opacity: 1, y: 0, duration: 1, ease: 'power3.out' }
    );
  }
  
  if (descriptionRef.value) {
    tl.fromTo(descriptionRef.value, 
      { opacity: 0, y: 20 },
      { opacity: 1, y: 0, duration: 1, ease: 'power3.out' }, 
      "-=0.7"
    );
  }

  if (generatorRef.value) {
    tl.fromTo(generatorRef.value, 
      { opacity: 0, scale: 0.95, y: 40 },
      { opacity: 1, scale: 1, y: 0, duration: 1.2, ease: 'elastic.out(1, 0.8)' }, 
      "-=0.5"
    );
  }
});
</script>
