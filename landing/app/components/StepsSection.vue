<template>
  <section id="how-it-works" class="bg-brand-light py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:text-center">
        <h2 class="text-base font-semibold leading-7 text-brand-primary">Workflow</h2>
        <p class="mt-2 text-3xl font-bold tracking-tight text-brand-dark sm:text-4xl">
          Secure sharing in three steps
        </p>
      </div>
      <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
        <div class="grid grid-cols-1 gap-8 md:grid-cols-3">
          <div v-for="(step, index) in steps" :key="step.title" class="flex flex-col items-center text-center p-6 bg-white rounded-2xl shadow-sm border border-brand-light">
            <div class="flex h-12 w-12 items-center justify-center rounded-full bg-brand-primary text-white text-xl font-bold mb-6">
              {{ index + 1 }}
            </div>
            <h3 class="text-lg font-semibold leading-8 text-brand-dark">{{ step.title }}</h3>
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
    title: 'Upload Document',
    description: 'Securely upload your contracts, proposals, or financial reports to our encrypted vault.'
  },
  {
    title: 'Set Controls',
    description: 'Add watermarks, disable downloading, and set expiration times or password protection.'
  },
  {
    title: 'Send & Track',
    description: 'Share a secure link and watch in real-time as recipients interact with your document.'
  }
]
</script>
