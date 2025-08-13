<script setup lang="ts">
import { ref } from 'vue';

const inputText = ref('');
const handleSubmit = () => {
  console.log(inputText.value);
}
</script>



<template>
  <div class="center-container">
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
</template>



<style scoped>

.center-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
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
}  
</style>
