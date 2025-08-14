import { createApp } from "vue";
import "./global.styl";
import App from "./App.vue";

// 引入element-plus
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";

// 引入i18n
import i18n from "./i18n";
import * as ElementPlusIconsVue from "@element-plus/icons-vue";

const app = createApp(App);

// 注册element-plus图标组件
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}

app.use(ElementPlus);
app.use(i18n);
app.mount("#app");
