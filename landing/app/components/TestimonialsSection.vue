<template>
  <section class="bg-white py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-xl text-center">
        <h2 class="text-3xl font-bold tracking-tight text-brand-dark sm:text-4xl">
          Trusted by sensitive industries
        </h2>
        <p class="mt-4 text-lg leading-8 text-brand-gray">
          Ensuring confidentiality for legal, financial, and healthcare professionals.
        </p>
      </div>
      <div class="mx-auto mt-16 flow-root max-w-2xl sm:mt-20 lg:mx-0 lg:max-w-none">
        <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
          <div v-for="testimonial in testimonials" :key="testimonial.author" class="rounded-2xl bg-brand-light p-8 text-sm leading-6 border border-gray-100">
            <blockquote class="text-brand-dark">
              <p>“{{ testimonial.body }}”</p>
            </blockquote>
            <div class="mt-6 flex items-center gap-x-4">
              <div class="h-10 w-10 rounded-full bg-brand-primary/20 flex items-center justify-center text-brand-primary font-bold">
                  {{ testimonial.author[0] }}
              </div>
              <div>
                <div class="font-semibold text-brand-dark">{{ testimonial.author }}</div>
                <div class="text-brand-gray">{{ testimonial.role }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
const testimonials = [
  {
    body: 'Being able to revoke access to a contract after negotiations stalled saved us from a major leak.',
    author: 'James Morrison',
    role: 'Corporate Attorney'
  },
  {
    body: 'The analytics are game-changing. I know exactly when investors review our pitch deck.',
    author: 'Elena Rodriguez',
    role: 'Startup Founder'
  },
  {
    body: 'Simple enough for our clients to use, but secure enough for our compliance team. Perfect balance.',
    author: 'David Chen',
    role: 'Wealth Manager'
  }
]
</script>
