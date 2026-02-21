<template>
  <header 
    class="fixed top-0 left-0 right-0 z-[50] transition-all duration-300 border-b border-transparent bg-brand-light/80 backdrop-blur-md"
    :class="{ 'border-border/50 bg-white/90': scrolled }"
  >
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="grid h-20 grid-cols-2 md:grid-cols-[1fr_auto_1fr] items-center">
        <!-- Logo -->
        <div class="flex items-center gap-2">
          <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-primary text-white shadow-lg">
            <LogoIcon class="w-6 h-6 stroke-white fill-white" />
          </div>
          <span class="text-xl font-bold tracking-tight text-brand-dark">
            Story<span class="text-primary">Me</span>
          </span>
        </div>

        <!-- Desktop Navigation - Perfectly Centered -->
        <nav class="hidden md:flex items-center justify-center gap-8 px-4">
          <NuxtLink to="/" class="text-sm font-medium text-brand-gray hover:text-primary transition-colors whitespace-nowrap">
            {{ $t('header.features') }}
          </NuxtLink>
          <NuxtLink to="/about" class="text-sm font-medium text-brand-gray hover:text-primary transition-colors whitespace-nowrap">
            {{ $t('header.about') }}
          </NuxtLink>
          <NuxtLink to="/blog" class="text-sm font-medium text-brand-gray hover:text-primary transition-colors whitespace-nowrap">
            {{ $t('header.blog') }}
          </NuxtLink>
          <NuxtLink to="/pricing" class="text-sm font-medium text-brand-gray hover:text-primary transition-colors whitespace-nowrap">
            {{ $t('header.pricing') }}
          </NuxtLink>
          <NuxtLink to="/dashboard" class="text-sm font-medium text-brand-gray hover:text-primary transition-colors whitespace-nowrap">
            {{ $t('header.dashboard') }}
          </NuxtLink>
        </nav>

        <!-- CTA Action -->
        <div class="flex items-center justify-end gap-3">
          <!-- Language Switcher -->
          <div class="hidden sm:flex items-center bg-brand-light/50 rounded-lg p-1 border border-border/30">
            <button 
              v-for="locale in ['en', 'ru']" 
              :key="locale"
              @click="setLocale(locale as any)"
              class="px-2 py-1 text-[10px] font-bold uppercase transition-all rounded"
              :class="currentLocale === locale ? 'bg-primary text-white shadow-sm' : 'text-brand-gray/60 hover:text-primary'"
            >
              {{ locale }}
            </button>
          </div>

          <button 
            class="hidden sm:block text-sm font-semibold text-brand-dark hover:text-primary transition-colors"
            @click="openAuth('login')"
          >
            {{ $t('header.login') }}
          </button>
          <button 
            class="rounded-full bg-primary px-5 py-2 text-sm font-semibold text-white shadow-md transition-all hover:scale-105 active:scale-95"
            @click="openAuth('register')"
          >
            {{ $t('header.getStarted') }}
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
        <NuxtLink to="/" class="text-base font-medium text-brand-gray hover:text-primary" @click="isMenuOpen = false">
          {{ $t('header.features') }}
        </NuxtLink>
        <NuxtLink to="/about" class="text-base font-medium text-brand-gray hover:text-primary" @click="isMenuOpen = false">
          {{ $t('header.about') }}
        </NuxtLink>
        <NuxtLink to="/blog" class="text-base font-medium text-brand-gray hover:text-primary" @click="isMenuOpen = false">
          {{ $t('header.blog') }}
        </NuxtLink>
        <NuxtLink to="/pricing" class="text-base font-medium text-brand-gray hover:text-primary" @click="isMenuOpen = false">
          {{ $t('header.pricing') }}
        </NuxtLink>
        <NuxtLink to="/dashboard" class="text-base font-medium text-brand-gray hover:text-primary" @click="isMenuOpen = false">
          {{ $t('header.dashboard') }}
        </NuxtLink>

        <div class="flex items-center gap-2 mt-2">
          <span class="text-xs text-brand-gray font-medium uppercase">Language:</span>
          <div class="flex gap-2">
            <button 
              v-for="locale in ['en', 'ru']" 
              :key="locale"
              @click="setLocale(locale as any)"
              class="px-3 py-1 text-xs font-bold uppercase border border-border rounded-lg"
              :class="currentLocale === locale ? 'bg-primary text-white border-primary' : 'text-brand-gray bg-white'"
            >
              {{ locale }}
            </button>
          </div>
        </div>

        <hr class="border-border/50 my-2" />
        <button 
          class="w-full rounded-xl bg-primary py-3 text-center font-bold text-white shadow-md"
          @click="openAuth('register')"
        >
          {{ $t('header.getStarted') }}
        </button>
      </nav>
    </div>

    <!-- Auth Modal - Teleported to Body for perfect layout -->
    <Teleport to="body">
      <AuthModal 
        :is-open="isAuthOpen" 
        :initial-mode="authMode" 
        @close="isAuthOpen = false" 
      />
    </Teleport>

  </header>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { useI18n } from 'vue-i18n';
import { useAuth } from '~/composables/useAuth';

const { t, locale: currentLocale, setLocale } = useI18n();
const { isAuthOpen, authMode, triggerAuth, closeAuth } = useAuth();

const scrolled = ref(false);
const isMenuOpen = ref(false);

const openAuth = (mode: 'login' | 'register') => {
  triggerAuth(mode);
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
