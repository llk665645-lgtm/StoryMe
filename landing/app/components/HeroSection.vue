<template>
  <section class="bg-brand-light py-20 lg:py-32 overflow-hidden">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 relative">
      <div class="mx-auto max-w-2xl text-center">
        <div class="flex justify-center">
          <h1 
            ref="titleRef"
            class="text-4xl font-bold tracking-tight text-brand-dark sm:text-6xl text-center justify-center mb-6 opacity-0 translate-y-0"
          >
            Complete Control Over <br class="hidden sm:block" /> Your Sensitive Documents
          </h1>
        </div>
        <p ref="descriptionRef" class="mt-6 text-lg leading-8 text-brand-gray opacity-0 translate-y-0">
          Securely share, track, and revoke access to your files instantly. 
          Enterprise-grade security meets consumer simplicity.
        </p>
        <div ref="buttonsRef" class="mt-10 flex items-center justify-center gap-x-6 opacity-0 translate-y-0">
          <button class="rounded-md bg-brand-primary px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-brand-primary-hover focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-brand-primary transition-colors duration-200">
             Start Securing Now
          </button>
          <a href="#features" class="text-sm font-semibold leading-6 text-brand-dark">
            How it works <span aria-hidden="true">→</span>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import gsap from 'gsap';

const titleRef = ref<HTMLElement | null>(null);
const descriptionRef = ref<HTMLElement | null>(null);
const buttonsRef = ref<HTMLElement | null>(null);

onMounted(() => {
  const tl = gsap.timeline({ delay: 0.2 });
  
  if (titleRef.value) {
    tl.to(titleRef.value, {
      opacity: 1,
      duration: 0.8,
      ease: 'power2.out'
    });
  }
  
  if (descriptionRef.value) {
    tl.to(descriptionRef.value, {
      opacity: 1,
      duration: 0.8,
      ease: 'power2.out'
    }, "-=0.4");
  }

  if (buttonsRef.value) {
    tl.to(buttonsRef.value, {
      opacity: 1,
      duration: 0.8,
      ease: 'power2.out'
    }, "-=0.4");
  }
});
</script>
