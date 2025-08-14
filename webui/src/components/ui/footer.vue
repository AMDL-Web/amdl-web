<template>
  <div class="footer">
    <a href="https://github.com/AMDL-Web/webui">AMDL Webui</a> |
    {{ $t("footer.version") }}: {{ gitVersion }}
  </div>
</template>

<script setup lang="ts">
import { useI18n } from "vue-i18n";

defineProps<{ gitVersion: string }>();

const { t: $t } = useI18n();
</script>

<style scoped>
.footer {
  text-align: center;
  color: #fff;
  font-size: 20px;
  font-weight: 700;
}

.footer a {
  color: #fff;
  text-decoration: none;
}
</style>
