<script setup lang="ts">
import DataTable from "@/components/DataTable.vue"
import SectionCards from "@/components/SectionCards.vue"

definePageMeta({
  layout: "dashboard",
  middleware: "auth"
})

const data = [
  {
    id: 1,
    header: "The Brave Little Dino",
    type: "Fairytale",
    status: "Completed",
    target: "Alex (4)",
    limit: "Watercolor",
    reviewer: "Forest",
  },
  {
    id: 2,
    header: "Starry Night Adventure",
    type: "Educational",
    status: "Completed",
    target: "Sophia (6)",
    limit: "Ink & Wash",
    reviewer: "Space",
  },
  {
    id: 3,
    header: "The Lost Key of Magic",
    type: "Fantasy",
    status: "In Progress",
    target: "Leo (3)",
    limit: "3D Render",
    reviewer: "Fairytale",
  },
  {
    id: 4,
    header: "Superhero for a Day",
    type: "Action",
    status: "Completed",
    target: "Alex (4)",
    limit: "Comic Style",
    reviewer: "Superheroes",
  },
]
</script>

<template>
  <div class="flex flex-1 flex-col">
    <div class="@container/main flex flex-1 flex-col gap-2">
      <div class="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
        <SectionCards />
        <DataTable :data="data" />
      </div>
    </div>
  </div>
</template>
