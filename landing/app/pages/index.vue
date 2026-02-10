<template>
  <div class="bg-brand-light min-h-screen">
    <HeroSection />
    <FeaturesSection />
    <StepsSection />

    <section class="py-24 bg-white">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="bg-background relative h-[500px] w-full overflow-hidden">
          <div class="mt-[64px] flex justify-center px-12">
            <TestimonialSlider :testimonials="testimonials" />
          </div>
        </div>
      </div>
    </section>


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
      "The level of control we now have over our legal documents is unprecedented. Revoking access instantly has saved us from several potential data leaks.",
    name: "James Morrison",
    role: "Corporate Attorney, Morrison & Associates",
  },
  {
    img: `https://randomuser.me/api/portraits/women/${getRandomNumber()}.jpg`,
    quote:
      "Knowing exactly when and where our pitch decks are being viewed gives us a huge advantage during fundraising. It's an essential tool for any startup.",
    name: "Elena Rodriguez",
    role: "Founder, FinTech Global",
  },
  {
    img: `https://randomuser.me/api/portraits/men/${getRandomNumber()}.jpg`,
    quote:
      "Security is non-negotiable in healthcare. This platform provides the encryption and tracking we need to stay compliant while remaining incredibly easy to use.",
    name: "Dr. Sarah Chen",
    role: "Chief of Medicine, Metro Health",
  },
  {
    img: `https://randomuser.me/api/portraits/men/${getRandomNumber()}.jpg`,
    quote:
      "We share sensitive financial reports daily. The ability to set expiration dates and disable downloads ensures our data stays exactly where it belongs.",
    name: "Marcus Thorne",
    role: "CFO, Peak Capital",
  },
]


useHead({
  title: 'Secure Document Sharing & Control',
  meta: [
    { name: 'description', content: 'Securely share, track, and manage your sensitive documents. Revoke access instantly and get detailed analytics.' }
  ]
})
</script>


