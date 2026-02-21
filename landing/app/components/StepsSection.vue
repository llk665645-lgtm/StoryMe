<template>
  <section id="how-it-works" class="bg-transparent py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:text-center">
        <h2 class="text-base font-semibold leading-7 text-white/50 uppercase tracking-widest">{{ $t('steps.title') }}</h2>
        <div class="flex justify-center mt-2">
            <p class="text-3xl font-bold tracking-tight text-white sm:text-4xl text-center justify-center">
              {{ $t('steps.subtitle') }}
            </p>
        </div>
      </div>
      <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
        <div class="grid grid-cols-1 gap-8 md:grid-cols-3">
          <div v-for="(step, index) in stepList" :key="index" class="flex flex-col items-center text-center p-10 bg-white/5 backdrop-blur-md rounded-[2.5rem] border border-white/10 transition-all hover:bg-white/10 hover:-translate-y-1">
            <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-white text-dream-deep text-2xl font-bold mb-8 shadow-[0_8px_20px_rgba(0,0,0,0.25)]">
              {{ index + 1 }}
            </div>
            <h3 class="text-xl font-bold leading-8 text-white">{{ step.title }}</h3>
            <p class="mt-4 text-base leading-7 text-white/60">{{ step.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
const { tm } = useI18n()

interface Step {
  title: string
  description: string
}

const stepList = computed(() => tm('steps.list') as Step[])
</script>
