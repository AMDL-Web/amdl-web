<script setup lang="ts">
import { ref } from "vue";
import { useI18n } from "vue-i18n";
import taskPush_Button from "./components/ui/buttons/taskPush.vue";
import input_shadow from "./components/ui/Form/inputShadow.vue";
import Footer from "./components/ui/footer.vue";
import Sidebar from "./components/ui/Sidebar.vue";
const gitVersion = "{{gitVersion}}";

const { t } = useI18n();

const inputRef = ref<InstanceType<typeof input_shadow> | null>(null);

const pushTask = () => {
  const inputValue = inputRef.value?.input?.value || "";
  console.log("Input value:", inputValue);
};
</script>

<template>
  <div class="container">
    <Sidebar />
    <div class="form-container">
      <input_shadow ref="inputRef" :text="t('form.songUrl')" />
      <div class="button-wrapper">
        <taskPush_Button @click="pushTask" :text="t('form.push')" />
      </div>
    </div>
  </div>
  <Footer :gitVersion="gitVersion" />
</template>
<style scoped lang="stylus">
.container
  height 95vh
  display flex
  margin 0 auto
  justify-content center
  align-items center

.form-container
  width 100vw
  display flex
  justify-content center
  align-items center
  gap 10px

  @media (max-width: 767px)
    flex-direction column

.button-wrapper
  display inline-block
  width 250px
  overflow visible
</style>
