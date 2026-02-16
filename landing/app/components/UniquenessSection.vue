<template>
  <section class="py-24 bg-white relative overflow-hidden">
    <!-- Decorative elements -->
    <div class="absolute top-0 left-1/4 w-64 h-64 bg-primary/5 rounded-full blur-3xl -translate-y-1/2" />
    <div class="absolute bottom-0 right-1/4 w-96 h-96 bg-primary/5 rounded-full blur-3xl translate-y-1/2" />

    <div class="mx-auto max-w-7xl px-6 lg:px-8 relative">
      <div class="mx-auto max-w-2xl text-center mb-16">
        <h2 class="text-3xl font-bold tracking-tight text-brand-dark sm:text-4xl">
          {{ $t('uniqueness.title') }}
        </h2>
        <p class="mt-4 text-lg text-brand-gray">
          {{ $t('uniqueness.subtitle') }}
        </p>
      </div>

      <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
        <div 
          v-for="(item, index) in uniquenessList" 
          :key="index" 
          class="group p-8 rounded-4xl bg-brand-light/30 border border-transparent hover:border-primary/20 hover:bg-white transition-all duration-300 shadow-sm hover:shadow-xl"
        >
          <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-white text-primary shadow-sm group-hover:bg-primary group-hover:text-white transition-all mb-6">
            <Icon :name="icons[index] || 'lucide:sparkles'" class="size-7" />
          </div>
          <h3 class="text-xl font-bold text-brand-dark mb-4">
            {{ item.name }}
          </h3>
          <p class="text-base leading-7 text-brand-gray">
            {{ item.description }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { tm } = useI18n()

interface UniquenessItem {
  name: string
  description: string
}

const uniquenessList = computed(() => tm('uniqueness.list') as UniquenessItem[])
const icons = [
  'lucide:target',
  'lucide:mail',
  'lucide:message-square',
  'lucide:refresh-cw',
  'lucide:maximize'
]
</script>
