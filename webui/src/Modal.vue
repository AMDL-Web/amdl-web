<script setup lang="ts">
  import { defineProps, defineEmits } from 'vue';

  const props = defineProps({
    isVisible: {
      type: Boolean,
      required: false,
    },
    message: {
      type: String,
      default: '这是一个弹窗',
    }
  });

  const emit = defineEmits(['close']);
  const closeModal = () => {
    emit('close');
  }
</script>



<template>
  <div class="modal-backdrop" v-if="isVisible" @click="closeModal">
    <div class="modal-content">
      <div class="modal-body">
        <p>{{ message }}</p>
      </div>
      <div class="modal-footer">
        <button class="close-button" @click="closeModal">Close</button>
      </div>
    </div>
  </div>
</template>



<style scoped>
/* 遮罩层样式 */
.modal-backdrop {
  /* 固定定位，覆盖整个视口 */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* 使用 Flexbox 居中弹窗 */
  display: flex;
  justify-content: center;
  align-items: center;
  /* 背景颜色，带透明度 */
  background-color: rgba(0, 0, 0, 0.5);
  /* 使用 backdrop-filter 实现背景模糊效果 */
  /* backdrop-filter: blur() 是一个 CSS 属性，可以对元素后面的区域进行滤镜处理 */
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px); /* 兼容性前缀 */
  z-index: 1000; /* 确保弹窗在最上层 */
}

/* 弹窗主体样式 */
.modal-content {
  /* 设置弹窗主体样式 */
  background-color: #fff;
  border-radius: 20px;
  padding: 20px;
  width: 300px;
  /* 阴影效果，让弹窗更立体 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  /* 阻止点击弹窗内容时触发遮罩层的点击事件 */
  cursor: default;
}

/* 弹窗内容区样式 */
.modal-body {
  text-align: center;
  margin-bottom: 20px;
}

/* 弹窗底部按钮区样式 */
.modal-footer {
  text-align: center;
}

/* 关闭按钮样式 */
.close-button {
  width: 100%;
  padding: 10px 20px;
  border-radius: 20px;
  border: 1px solid transparent;
  background-color: #e57373; /* 红色背景 */
  color: white;
  cursor: pointer;
  box-sizing: border-box;
}
</style>