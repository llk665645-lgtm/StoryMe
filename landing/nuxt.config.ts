import tailwindcss from "@tailwindcss/vite";

export default defineNuxtConfig({
  compatibilityDate: "2025-07-15",
  ssr: true,
  srcDir: 'app',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  vite: {
    plugins: [
      (tailwindcss as any)(),
    ],
  },
  modules: [
    '@nuxt/a11y',
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/image',
    '@nuxt/icon',
    '@nuxtjs/i18n',
    '@nuxtjs/seo',
    'shadcn-nuxt'
  ],
  shadcn: {
    prefix: '',
    componentDir: './app/components/ui',
  },
  site: {
    url: 'https://storyme.ai', // Placeholder, update to actual if known
    name: 'StoryMe - AI Magical Stories for Kids',
    description: 'Create personalized bedtime stories with AI illustrations for your child in 30 seconds.',
    defaultLocale: 'en',
  },
  i18n: {
    locales: [
      { code: 'en', name: 'English', file: 'en.json' },
      { code: 'ru', name: 'Русский', file: 'ru.json' }
    ],
    lazy: true,
    langDir: 'locales',
    defaultLocale: 'en',
    strategy: 'no_prefix'
  },
  ogImage: {
    enabled: true,
  },
  sitemap: {
    enabled: true,
  },
  robots: {
    enabled: true,
  }
});