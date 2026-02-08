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
  title: 'Secure Document Sharing & Control',
  meta: [
    { name: 'description', content: 'Securely share, track, and manage your sensitive documents. Revoke access instantly and get detailed analytics.' }
  ]
})
</script>