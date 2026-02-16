<template>
  <section id="features" class="bg-white py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:text-center">
        <h2 class="text-base font-semibold leading-7 text-primary uppercase tracking-widest">Why MoodQuotes?</h2>
        <div class="flex justify-center mt-2">
            <p class="text-3xl font-bold tracking-tight text-brand-dark sm:text-4xl text-center justify-center">
              Elevate your daily mindset
            </p>
        </div>
        <p class="mt-6 text-lg leading-8 text-brand-gray">
          Harness the power of generative AI to find the perfect words for any moment.
        </p>
      </div>
      <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
        <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
          <div v-for="feature in features" :key="feature.name" class="flex flex-col">
            <dt class="flex items-center gap-x-3 text-base font-semibold leading-7 text-brand-dark">
              <div class="h-12 w-12 flex items-center justify-center rounded-2xl bg-primary/10">
                 <Icon :name="feature.icon" class="h-6 w-6 text-primary" />
              </div>
              {{ feature.name }}
            </dt>
            <dd class="mt-4 flex flex-auto flex-col text-base leading-7 text-brand-gray">
              <p class="flex-auto">{{ feature.description }}</p>
            </dd>
          </div>
        </dl>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const features = [
  {
    name: 'Personalized AI Wisdom',
    description:
      'Our AI understands context. Whether you need a push to start your day or a gentle word to end it, the quotes are unique to you.',
    icon: 'lucide:brain-circuit'
  },
  {
    name: 'Mood-Sync Technology',
    description:
      'Select your current emotion and get content that resonates. From deep motivation to peaceful mindfulness.',
    icon: 'lucide:palette'
  },
  {
    name: 'Visual Creator',
    description:
      'Transform any generated quote into a stunning, shareable social media post with our built-in designer.',
    icon: 'lucide:image'
  },
]
</script>
