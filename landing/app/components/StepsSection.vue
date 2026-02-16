<template>
  <section id="how-it-works" class="bg-brand-light py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:text-center">
        <h2 class="text-base font-semibold leading-7 text-primary uppercase tracking-widest">How it works</h2>
        <div class="flex justify-center mt-2">
            <p class="text-3xl font-bold tracking-tight text-brand-dark sm:text-4xl text-center justify-center">
              Your journey to inspiration
            </p>
        </div>
      </div>
      <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
        <div class="grid grid-cols-1 gap-8 md:grid-cols-3">
          <div v-for="(step, index) in steps" :key="step.title" class="flex flex-col items-center text-center p-8 bg-white rounded-3xl shadow-sm border border-brand-light transition-all hover:shadow-xl hover:-translate-y-1">
            <div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-primary text-white text-2xl font-bold mb-6 rotate-3">
              {{ index + 1 }}
            </div>
            <h3 class="text-xl font-bold leading-8 text-brand-dark">{{ step.title }}</h3>
            <p class="mt-4 text-base leading-7 text-brand-gray">{{ step.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const steps = [
  {
    title: 'Pick your Vibe',
    description: 'Select your current mood or goal—from motivation to peaceful mindfulness.'
  },
  {
    title: 'AI Crafts Magic',
    description: 'Our advanced generative engine creates a unique quote tailored just for you.'
  },
  {
    title: 'Share the Spark',
    description: 'Instantly turn your quote into a beautiful image and share it with the world.'
  }
]
</script>
