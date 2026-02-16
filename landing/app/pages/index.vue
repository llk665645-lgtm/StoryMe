<template>
  <div class="bg-brand-light min-h-screen">
    <HeroSection />
    <FeaturesSection />
    <StepsSection />

    <section class="py-24 bg-white">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="bg-background relative h-[500px] w-full overflow-hidden flex items-center justify-center">
          <div class="w-full max-w-3xl px-12">
            <TestimonialSlider :testimonials="testimonials" />
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
import { rand } from "@vueuse/core"
import HeroSection from '~/components/HeroSection.vue'
import FeaturesSection from '~/components/FeaturesSection.vue'
import StepsSection from '~/components/StepsSection.vue'

import CTASection from '~/components/CTASection.vue'
import AppFooter from '~/components/AppFooter.vue'

function getRandomNumber() {
  return rand(1, 99);
}

const testimonials = [
  {
    img: `https://randomuser.me/api/portraits/men/${getRandomNumber()}.jpg`,
    quote:
      "This app literally changed my morning routine. Starting the day with a quote tailored to my mood gives me so much clarity.",
    name: "Alex Rivera",
    role: "Daily User",
  },
  {
    img: `https://randomuser.me/api/portraits/women/${getRandomNumber()}.jpg`,
    quote:
      "The 'Confidence' category helps me prep for big meetings. It's like having a life coach in my pocket.",
    name: "Sarah Jenkins",
    role: "Entrepreneur",
  },
  {
    img: `https://randomuser.me/api/portraits/men/${getRandomNumber()}.jpg`,
    quote:
      "I love generating these for my team. The AI really captures the right sentiment for every situation.",
    name: "Michael Chen",
    role: "Team Lead",
  },
]


useHead({
  title: 'MoodQuotes AI - Your Daily Inspiration',
  meta: [
    { name: 'description', content: 'Generate unique, AI-powered quotes tailored to your mood. Motivation, calm, and wisdom at your fingertips.' }
  ]
})
</script>


