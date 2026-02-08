<template>
  <section class="bg-white py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-xl text-center">
        <h2 class="text-3xl font-bold tracking-tight text-brand-dark sm:text-4xl">
          Loved by professionals
        </h2>
        <p class="mt-4 text-lg leading-8 text-brand-gray">
          See what our early adopters are saying about their new AI-generated portfolios.
        </p>
      </div>
      <div class="mx-auto mt-16 flow-root max-w-2xl sm:mt-20 lg:mx-0 lg:max-w-none">
        <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
          <div v-for="testimonial in testimonials" :key="testimonial.author" class="rounded-2xl bg-brand-light p-8 text-sm leading-6 border border-gray-100">
            <blockquote class="text-brand-dark">
              <p>“{{ testimonial.body }}”</p>
            </blockquote>
            <div class="mt-6 flex items-center gap-x-4">
              <!-- Avatar Placeholder -->
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
    body: 'I landed my dream job within a week of using this. The portfolio generator is absolute magic.',
    author: 'Sarah Chen',
    role: 'Software Engineer'
  },
  {
    body: 'Finally, a resume builder that actually understands context. Saved me hours of formatting.',
    author: 'Michael Dave',
    role: 'Product Designer'
  },
  {
    body: 'The custom domain feature made my portfolio look so professional. Highly verified!',
    author: 'Emily Smith',
    role: 'Marketing Manager'
  }
]
</script>
