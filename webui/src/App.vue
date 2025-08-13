<script setup lang="ts">
import { ref } from 'vue';
import Modal from './Modal.vue';

const inputText = ref('');
const showModal = ref(false);

const handleSubmit = () => {
  console.log(inputText.value);
  // 显示成功弹窗
  showModal.value = true;
  // 清空输入框
  inputText.value = '';
}
</script>



<template>
  <div class="center-container" :class="{ 'blur-background': showModal }">
    <div class="input-group">
      <input 
        type="text" 
        placeholder="Enter your text" 
        v-model="inputText" 
        maxlength="10000"
        @keydown.enter="handleSubmit"
      />
      <button @click="handleSubmit">Submit</button>
    </div>
  </div>
  
  <!-- 弹窗组件 -->
  <Modal 
    v-model="showModal" 
    message="发送成功"
  />
</template>



<style scoped>

.center-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  transition: filter 0.3s ease;
}

.center-container.blur-background {
  filter: blur(3px);
}

.input-group {
  display: flex;
  flex-direction: column;
}

.input-group input {
  padding: 10px;
  width: 300px;
  border-radius: 20px;
  border: 1px solid #ccc;
  outline: none;
  box-sizing: border-box;
}

.input-group button {
  padding: 10px 20px;
  width: 300px;
  margin-top: 10px;
  border-radius: 20px;
  border: 1px solid #ccc;
  background-color: #42b983;
  cursor: pointer;
  box-sizing: border-box;
  transition: background-color 0.3s ease;
}

.input-group button:hover {
  background-color: #35a372;
}
</style>
