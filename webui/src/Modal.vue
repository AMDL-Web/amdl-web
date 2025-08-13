<template>
  <Teleport to="body">
    <Transition name="modal">
      <div v-if="isVisible" class="modal-overlay" @click="handleOverlayClick">
        <div class="modal-container" @click.stop>
          <div class="modal-content">
            <slot>
              {{ message }}
            </slot>
          </div>
          <button class="modal-close-btn" @click="close">关闭</button>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';

interface Props {
  modelValue?: boolean;
  message?: string;
}

const props = withDefaults(defineProps<Props>(), {
  modelValue: false,
  message: ''
});

const emit = defineEmits<{
  'update:modelValue': [value: boolean];
  'close': [];
}>();

const isVisible = ref(props.modelValue);

watch(() => props.modelValue, (newVal) => {
  isVisible.value = newVal;
  if (newVal) {
    document.body.style.overflow = 'hidden';
  } else {
    document.body.style.overflow = '';
  }
});

const close = () => {
  isVisible.value = false;
  emit('update:modelValue', false);
  emit('close');
  document.body.style.overflow = '';
};

const handleOverlayClick = (e: MouseEvent) => {
  if (e.target === e.currentTarget) {
    close();
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-container {
  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: saturate(1.2) blur(15px);
  -webkit-backdrop-filter: saturate(1.2) blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.75);
  border-radius: 20px;
  width: 90vw;
  min-width: 360px;
  max-width: 640px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.modal-content {
  padding: 30px;
  text-align: center;
  font-size: 16px;
  color: #333;
}

.modal-close-btn {
  width: 100%;
  padding: 15px;
  background-color: #ff4444;
  color: white;
  border: none;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.modal-close-btn:hover {
  background-color: #cc0000;
}

/* 过渡动画：更顺滑的弹出/关闭 */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 420ms cubic-bezier(0.22, 1, 0.36, 1);
}

.modal-enter-active .modal-container,
.modal-leave-active .modal-container {
  transition: transform 420ms cubic-bezier(0.22, 1, 0.36, 1), opacity 420ms cubic-bezier(0.22, 1, 0.36, 1);
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container {
  transform: translateY(12px) scale(0.98);
  opacity: 0;
}

.modal-leave-to .modal-container {
  transform: translateY(8px) scale(0.98);
  opacity: 0;
}
</style>
