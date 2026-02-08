<template>
  <div class="bg-brand-light min-h-screen">
    <HeroSection />
    <FeaturesSection />
    <StepsSection />
    <TestimonialsSection />
    <CTASection />
    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import HeroSection from '~/components/HeroSection.vue'
import FeaturesSection from '~/components/FeaturesSection.vue'
import StepsSection from '~/components/StepsSection.vue'
import TestimonialsSection from '~/components/TestimonialsSection.vue'
import CTASection from '~/components/CTASection.vue'
import AppFooter from '~/components/AppFooter.vue'

useHead({
  title: 'AI Resume & Portfolio Builder',
  meta: [
    { name: 'description', content: 'Create your professional identity in minutes with AI-generated resumes and portfolios.' }
  ]
})
</script>