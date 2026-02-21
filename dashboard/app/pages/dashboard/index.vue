<script lang="ts">
export const iframeHeight = "800px"
export const description = "A dashboard with sidebar, data table, and analytics cards."
</script>

<script setup lang="ts">
import AppSidebar from "@/components/AppSidebar.vue"
import ChartAreaInteractive from "@/components/ChartAreaInteractive.vue"
import DataTable from "@/components/DataTable.vue"
import SectionCards from "@/components/SectionCards.vue"
import SiteHeader from "@/components/SiteHeader.vue"
import {
  SidebarInset,
  SidebarProvider,
} from "@/components/ui/sidebar"

const data = [
  {
    id: 1,
    header: "The Brave Little Fox",
    type: "Forest",
    status: "Ready",
    target: "Oliver",
    limit: "12 Oct",
    reviewer: "Alex Parent",
  },
  {
    id: 2,
    header: "Space Adventure with Robo",
    type: "Space",
    status: "Ready",
    target: "Sophia",
    limit: "10 Oct",
    reviewer: "Alex Parent",
  },
  {
    id: 3,
    header: "Dino's Big Secret",
    type: "Dino",
    status: "Ready",
    target: "Oliver",
    limit: "05 Oct",
    reviewer: "Alex Parent",
  },
  {
    id: 4,
    header: "The Mermaid's Song",
    type: "Ocean",
    status: "Draft",
    target: "Sophia",
    limit: "Today",
    reviewer: "Alex Parent",
  },
  {
    id: 5,
    header: "Super Leo Saves the Day",
    type: "Super",
    status: "Ready",
    target: "Leo",
    limit: "01 Oct",
    reviewer: "Alex Parent",
  },
]

</script>

<template>
  <SidebarProvider
    :style=" {
      '--sidebar-width': 'calc(var(--spacing) * 72)',
      '--header-height': 'calc(var(--spacing) * 12)',
    }"
  >
    <AppSidebar variant="inset" />
    <SidebarInset>
      <SiteHeader />
      <div class="flex flex-1 flex-col">
        <div class="@container/main flex flex-1 flex-col gap-2">
          <div class="flex flex-col gap-4 py-4 md:gap-6 md:py-6">
            <SectionCards />
            <div class="px-4 lg:px-6">
              <ChartAreaInteractive />
            </div>
            <DataTable :data="data" />
          </div>
        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
