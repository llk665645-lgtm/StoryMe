<template>
  <footer class="bg-white">
    <div class="mx-auto max-w-7xl overflow-hidden px-6 py-12 lg:px-8">
      <nav class="-mb-6 flex flex-wrap justify-center gap-x-12 gap-y-3 text-sm leading-6 items-center" aria-label="Footer">
        <div v-for="item in navigation" :key="item.name">
          <a :href="item.href" class="text-brand-gray hover:text-brand-dark transition-colors duration-200">{{ item.name }}</a>
        </div>
      </nav>
      <p class="mt-10 text-center text-xs leading-5 text-gray-400">
        &copy; {{ new Date().getFullYear() }} HireFlow AI. {{ $t('footer.rights') }}
      </p>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const navigation = computed(() => [
  { name: t('footer.about'), href: '#' },
  { name: t('footer.features'), href: '#features' },
  { name: t('footer.pricing'), href: '#pricing' },
  { name: t('footer.contact'), href: '#' },
  { name: t('footer.privacy'), href: '#' },
])
</script>
