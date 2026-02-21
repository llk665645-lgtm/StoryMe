<template>
  <footer class="bg-transparent border-t border-white/5 mt-20">
    <div class="mx-auto max-w-7xl overflow-hidden px-6 py-12 lg:px-8">
      <nav class="-mb-6 flex flex-wrap justify-center gap-x-12 gap-y-3 text-sm leading-6 items-center" aria-label="Footer">
        <NuxtLink to="/about" class="text-white/50 hover:text-white transition-colors duration-200">
          {{ $t('header.about') }}
        </NuxtLink>
        <NuxtLink to="/blog" class="text-white/50 hover:text-white transition-colors duration-200">
          {{ $t('header.blog') }}
        </NuxtLink>
        <NuxtLink to="/pricing" class="text-white/50 hover:text-white transition-colors duration-200">
          {{ $t('header.pricing') }}
        </NuxtLink>
        <a href="#" class="text-white/50 hover:text-white transition-colors duration-200">
          {{ $t('footer.contact') }}
        </a>
        <a href="#" class="text-white/50 hover:text-white transition-colors duration-200">
          {{ $t('footer.privacy') }}
        </a>
      </nav>
      <p class="mt-10 text-center text-[10px] font-bold uppercase tracking-widest text-white/20">
        &copy; {{ new Date().getFullYear() }} StoryMe AI. {{ $t('footer.rights') }}
      </p>
    </div>
  </footer>
</template>

<script setup lang="ts">
// No extra logic needed for simple links
</script>
