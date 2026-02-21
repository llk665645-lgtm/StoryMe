<template>
  <div class="bg-brand-light min-h-screen">
    <HeroSection />
    <UniquenessSection />
    <ThemeShowcase />
    <FeaturesSection />
    <StepsSection />

    <section class="py-24 bg-white">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="bg-background relative h-[500px] w-full overflow-hidden flex items-center justify-center">
          <div class="w-full max-w-3xl px-12">
            <TestimonialSlider :testimonials="testimonialList" />
          </div>
        </div>
      </div>
    </section>


    <PricingSection />

    <CTASection />

    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { rand } from "@vueuse/core"
import HeroSection from '~/components/HeroSection.vue'
import UniquenessSection from '~/components/UniquenessSection.vue'
import ThemeShowcase from '~/components/ThemeShowcase.vue'
import FeaturesSection from '~/components/FeaturesSection.vue'
import StepsSection from '~/components/StepsSection.vue'

import CTASection from '~/components/CTASection.vue'
import AppFooter from '~/components/AppFooter.vue'

const { t, tm } = useI18n()

function getRandomNumber() {
  return rand(1, 99);
}

interface Testimonial {
  quote: string
  name: string
  role: string
  img: string
}

const testimonialList = computed(() => {
  const baseList = tm('testimonials.list') as Omit<Testimonial, 'img'>[]
  return baseList.map((item, index) => ({
    ...item,
    img: `https://randomuser.me/api/portraits/${index % 2 === 0 ? 'men' : 'women'}/${30 + index}.jpg`
  }))
})


useSeoMeta({
  title: t('seo.title'),
  description: t('seo.description'),
  ogTitle: t('seo.title'),
  ogDescription: t('seo.description'),
  ogImage: '/og-main.png',
  twitterCard: 'summary_large_image',
})
</script>


