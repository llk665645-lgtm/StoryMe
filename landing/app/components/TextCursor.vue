<template>
  <div class="fixed inset-0 pointer-events-none z-[9999] overflow-hidden" ref="containerRef">
    <div
      v-for="item in trail"
      :key="item.id"
      class="text-cursor-item absolute select-none will-change-transform text-3xl"
      :ref="(el) => animateItem(el, item)"
    >
      {{ text }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import gsap from 'gsap';

interface TextCursorProps {
  text?: string;
  delay?: number;
  spacing?: number;
  followMouseDirection?: boolean;
  randomFloat?: boolean;
  exitDuration?: number;
  maxPoints?: number;
}

interface TrailItem {
  id: number;
  x: number;
  y: number;
  angle: number;
}

const props = withDefaults(defineProps<TextCursorProps>(), {
  text: '⚛️',
  delay: 0.01,
  spacing: 30,
  followMouseDirection: true,
  randomFloat: true,
  exitDuration: 0.8,
  maxPoints: 50
});

const trail = ref<TrailItem[]>([]);
const idCounter = ref(0);
let lastX = 0;
let lastY = 0;
let isFirstMove = true;

const handleMouseMove = (e: MouseEvent) => {
  const x = e.clientX;
  const y = e.clientY;
  
  if (isFirstMove) {
    lastX = x;
    lastY = y;
    isFirstMove = false;
    addItem(x, y, 0);
    return;
  }

  const dx = x - lastX;
  const dy = y - lastY;
  const dist = Math.sqrt(dx * dx + dy * dy);

  if (dist >= props.spacing) {
    const angle = Math.atan2(dy, dx) * (180 / Math.PI);
    const steps = Math.floor(dist / props.spacing);
    
    for (let i = 1; i <= steps; i++) {
        const t = (props.spacing * i) / dist;
        const newX = lastX + dx * t;
        const newY = lastY + dy * t;
        addItem(newX, newY, angle);
    }
    
    lastX = x;
    lastY = y;
  }
};

const addItem = (x: number, y: number, angle: number) => {
  const SAFETY_LIMIT = Math.max(props.maxPoints, 50);

  if (trail.value.length > SAFETY_LIMIT) {
    trail.value.shift();
  }

  trail.value.push({
    id: idCounter.value++,
    x,
    y,
    angle: props.followMouseDirection ? angle : 0
  });
};

const animateItem = (el: Element | ComponentPublicInstance | null, item: TrailItem) => {
  if (!el) return;
  const element = el as HTMLElement;
  
  if (element.dataset?.animated) return;
  element.dataset.animated = 'true';

  gsap.set(element, {
    x: item.x,
    y: item.y,
    rotation: item.angle,
    scale: 0.5,
    opacity: 0
  });

  gsap.to(element, {
    scale: 1,
    opacity: 1,
    duration: 0.1,
    ease: "power2.out",
    onComplete: () => {
        gsap.to(element, {
            x: item.x + (props.randomFloat ? (Math.random() * 60 - 30) : 0),
            y: item.y + (props.randomFloat ? (Math.random() * 60 - 30) : 0),
            opacity: 0,
            scale: 0.2,
            rotation: item.angle + (props.randomFloat ? (Math.random() * 180 - 90) : 0),
            duration: props.exitDuration,
            ease: "power2.in",
            onComplete: () => {
                removeItem(item.id);
            }
        });
    }
  });
};

const removeItem = (id: number) => {
  const index = trail.value.findIndex(i => i.id === id);
  if (index !== -1) {
    trail.value.splice(index, 1);
  }
};

onMounted(() => {
  window.addEventListener('mousemove', handleMouseMove);
});

onUnmounted(() => {
  window.removeEventListener('mousemove', handleMouseMove);
  trail.value = [];
});
</script>
