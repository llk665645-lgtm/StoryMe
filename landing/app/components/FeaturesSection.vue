<template>
  <section id="features" class="bg-white py-24 sm:py-32">
    <div class="mx-auto max-w-7xl px-6 lg:px-8">
      <div class="mx-auto max-w-2xl lg:text-center">
        <h2 class="text-base font-semibold leading-7 text-brand-primary">Uncompromised Security</h2>
        <p class="mt-2 text-3xl font-bold tracking-tight text-brand-dark sm:text-4xl">
          Protect what matters most
        </p>
        <p class="mt-6 text-lg leading-8 text-brand-gray">
          Maintain full ownership of your data with our advanced protection suite.
        </p>
      </div>
      <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
        <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
          <div v-for="feature in features" :key="feature.name" class="flex flex-col">
            <dt class="flex items-center gap-x-3 text-base font-semibold leading-7 text-brand-dark">
              <div class="h-10 w-10 flex items-center justify-center rounded-lg bg-brand-primary/10">
                 <svg class="h-6 w-6 text-brand-primary" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                    <path stroke-linecap="round" stroke-linejoin="round" :d="feature.iconPath" />
                 </svg>
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
    name: 'Granular Access Control',
    description:
      'Set precise permissions for every file. Decide who can view, download, or edit, and set expiration dates for temporary access.',
    iconPath: 'M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z' // Lock icon
  },
  {
    name: 'Real-Time Tracking',
    description:
      'Know exactly when your documents are opened, viewed, or forwarded. Get instant notifications and detailed audit logs.',
    iconPath: 'M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z M15 12a3 3 0 11-6 0 3 3 0 016 0z' // Eye icon
  },
  {
    name: 'Instant Revocation',
    description:
      'Sent a file to the wrong person? Revoke access immediately with a single click, even after it has been downloaded.',
    iconPath: 'M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z' // X/Circle icon
  },
]
</script>
