<template>
  <section id="features" class="bg-transparent py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:text-center px-4">
      </div>
      <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
        <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
          <div v-for="(feature, index) in featureList" :key="index" class="flex flex-col">
            <dt class="flex items-center gap-x-3 text-base font-semibold leading-7 text-white">
              <div class="h-12 w-12 flex items-center justify-center rounded-2xl bg-white/10 backdrop-blur-sm border border-white/5">
                 <Icon :name="featureIcons[index] || 'lucide:sparkles'" class="h-6 w-6 text-white" />
              </div>
              {{ feature.name }}
            </dt>
            <dd class="mt-4 flex flex-auto flex-col text-base leading-7 text-white/60">
              <p class="flex-auto">{{ feature.description }}</p>
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
const { tm } = useI18n()

interface Feature {
  name: string
  description: string
}

const featureList = computed(() => tm('features.list') as Feature[])
const featureIcons = [
  'lucide:zap', 
  'lucide:users', 
  'lucide:cpu', 
  'lucide:smartphone', 
  'lucide:copy-check'
]
</script>
