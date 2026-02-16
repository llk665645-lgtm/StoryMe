<template>
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl overflow-hidden px-6 py-12 lg:px-8">
      <nav class="-mb-6 flex flex-wrap justify-center gap-x-12 gap-y-3 text-sm leading-6 items-center" aria-label="Footer">
        <div v-for="item in navigation" :key="item.name">
          <a :href="item.href" class="text-brand-gray hover:text-brand-dark transition-colors duration-200">{{ item.name }}</a>
        </div>
      </nav>
      <p class="mt-10 text-center text-xs leading-5 text-gray-400">
        &copy; 2026 MoodQuotes AI. All rights reserved.
      </p>
    </div>
  </footer>
</template>

<script setup lang="ts">
const navigation = [
  { name: 'About', href: '#' },
  { name: 'Features', href: '#features' },
  { name: 'Pricing', href: '#' },
  { name: 'Contact', href: '#' },
  { name: 'Privacy', href: '#' },
]
</script>
