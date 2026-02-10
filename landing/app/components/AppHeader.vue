<template>
  <header 
    class="fixed top-0 left-0 right-0 z-[50] transition-all duration-300 border-b border-transparent bg-brand-light/80 backdrop-blur-md"
    :class="{ 'border-border/50 bg-white/90': scrolled }"
  >
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="flex h-20 items-center justify-between">
        <!-- Logo -->
        <div class="flex items-center gap-2">
          <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#ba445b] text-white shadow-lg">
            <Icon name="lucide:shield-check" class="size-6" />
          </div>
          <span class="text-xl font-bold tracking-tight text-brand-dark">
            Do<span class="text-[#ba445b]">Cafe</span>
          </span>
        </div>

        <!-- Desktop Navigation -->
        <nav class="hidden md:flex items-center gap-8">
          <a v-for="link in navLinks" :key="link.href" :href="link.href" class="text-sm font-medium text-brand-gray hover:text-[#ba445b] transition-colors">
            {{ link.label }}
          </a>
        </nav>

        <!-- CTA Action -->
        <div class="flex items-center gap-4">
          <button 
            class="hidden sm:block text-sm font-semibold text-brand-dark hover:text-[#ba445b] transition-colors"
            @click="openAuth('register')"
          >
            Log in
          </button>
          <button 
            class="rounded-full bg-[#ba445b] px-6 py-2.5 text-sm font-semibold text-white shadow-md transition-all hover:scale-105 active:scale-95"
            @click="openAuth('register')"
          >
            Get Started
          </button>
          
          <!-- Mobile Menu Toggle -->
          <button class="md:hidden text-brand-dark p-2" @click="isMenuOpen = !isMenuOpen">
            <Icon :name="isMenuOpen ? 'lucide:x' : 'lucide:menu'" class="size-6" />
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Navigation -->
    <div v-if="isMenuOpen" class="md:hidden border-t border-border/50 bg-white px-4 py-6 shadow-xl animate-in fade-in slide-in-from-top-4 duration-300">
      <nav class="flex flex-col gap-4">
        <a 
          v-for="link in navLinks" 
          :key="link.href" 
          :href="link.href" 
          class="text-base font-medium text-brand-gray hover:text-[#ba445b]"
          @click="isMenuOpen = false"
        >
          {{ link.label }}
        </a>

        <hr class="border-border/50" />
        <button 
          class="w-full rounded-xl bg-[#ba445b] py-3 text-center font-bold text-white shadow-md"
          @click="openAuth('register')"
        >
          Get Started
        </button>
      </nav>
    </div>

    <!-- Auth Modal -->
    <AuthModal 
      :is-open="isAuthOpen" 
      :initial-mode="authMode" 
      @close="isAuthOpen = false" 
    />
  </header>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

const scrolled = ref(false);
const isMenuOpen = ref(false);
const isAuthOpen = ref(false);
const authMode = ref<'login' | 'register'>('register');

const navLinks = [
  { label: 'Features', href: '#features' },
  { label: 'How it works', href: '#how-it-works' },
  { label: 'Pricing', href: '#pricing' },
];

const openAuth = (mode: 'login' | 'register') => {
  authMode.value = mode;
  isAuthOpen.value = true;
  isMenuOpen.value = false;
};


const handleScroll = () => {
  scrolled.value = window.scrollY > 20;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>
