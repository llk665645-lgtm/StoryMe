<template>
  <section class="py-24 bg-transparent relative overflow-hidden">
    <div class="mx-auto max-w-7xl px-6 lg:px-8 relative">
      <div class="mx-auto max-w-2xl text-center mb-16">
        <h2 class="text-3xl font-bold tracking-tight text-white sm:text-5xl font-serif italic">
          {{ $t('uniqueness.title') }}
        </h2>
      </div>

      <div class="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
        <div 
          v-for="(item, index) in uniquenessList" 
          :key="index" 
          class="group p-10 rounded-[2.5rem] bg-white/5 backdrop-blur-md border border-white/10 hover:border-white/30 hover:bg-white/10 transition-all duration-500 shadow-sm hover:shadow-2xl"
        >
          <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-white text-dream-deep shadow-[0_8px_20px_rgba(0,0,0,0.25)] group-hover:scale-110 transition-all mb-8">
            <Icon :name="icons[index] || 'lucide:sparkles'" class="size-8" />
          </div>
          <h3 class="text-xl font-bold text-white mb-4">
            {{ item.name }}
          </h3>
          <p class="text-base leading-7 text-white/50">
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
