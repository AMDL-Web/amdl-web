<template>
  <div>
    <!-- 侧边栏触发按钮 -->
    <div class="sidebar-trigger" @click="toggleSidebar">
      <button class="button">
        <div class="button-box">
          <span class="button-elem">
            <svg viewBox="0 0 46 40" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M43.700001,40.000481L2.3000031,40.000481C1.0324402,40.003761,0.0024528503,38.980076,0,37.714554L0,36.572334C0.0024528503,35.306816,1.0324402,34.283131,2.2999954,34.286407L43.700001,34.286407C44.967556,34.283131,45.997543,35.306816,46,36.572334L46,37.714554C45.997543,38.980072,44.967556,40.003757,43.700001,40.000481ZM43.700001,22.858265L13.800003,22.858265C12.532444,22.86154,11.50246,21.837858,11.5,20.572342L11.5,19.430119C11.50246,18.164602,12.532444,17.140921,13.800003,17.144196L43.700001,17.144196C44.966976,17.140919,45.996723,18.163698,46,19.428637L46,20.572338C45.997543,21.837852,44.967556,22.861536,43.700001,22.858265ZM43.700001,5.716053L2.3000031,5.716053C1.0321999,5.7185097,0.0024528503,4.6944008,0,3.4286423L0,2.2849388C0.003276825,1.0200005,1.0330238,-0.002784729,2.3000031,0.00049591064L43.700001,0.00049591064C44.967556,-0.0027809143,45.997543,1.0209045,46,2.2864189L46,3.4286423C45.997543,4.6941566,44.967556,5.7178383,43.700001,5.716053Z"
              />
            </svg>
          </span>
          <span class="button-elem">
            <svg viewBox="0 0 46 40" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M43.700001,40.000481L2.3000031,40.000481C1.0324402,40.003761,0.0024528503,38.980076,0,37.714554L0,36.572334C0.0024528503,35.306816,1.0324402,34.283131,2.2999954,34.286407L43.700001,34.286407C44.967556,34.283131,45.997543,35.306816,46,36.572334L46,37.714554C45.997543,38.980072,44.967556,40.003757,43.700001,40.000481ZM43.700001,22.858265L13.800003,22.858265C12.532444,22.86154,11.50246,21.837858,11.5,20.572342L11.5,19.430119C11.50246,18.164602,12.532444,17.140921,13.800003,17.144196L43.700001,17.144196C44.966976,17.140919,45.996723,18.163698,46,19.428637L46,20.572338C45.997543,21.837852,44.967556,22.861536,43.700001,22.858265ZM43.700001,5.716053L2.3000031,5.716053C1.0321999,5.7185097,0.0024528503,4.6944008,0,3.4286423L0,2.2849388C0.003276825,1.0200005,1.0330238,-0.002784729,2.3000031,0.00049591064L43.700001,0.00049591064C44.967556,-0.0027809143,45.997543,1.0209045,46,2.2864189L46,3.4286423C45.997543,4.6941566,44.967556,5.7178383,43.700001,5.716053Z"
              />
            </svg>
          </span>
        </div>
      </button>
    </div>

    <!-- 弹出式侧边栏 -->
    <el-drawer
      v-model="sidebarVisible"
      :title="t('sidebar.title')"
      direction="ltr"
      size="300px"
    >
      <div class="sidebar-content">
        <!-- 链接列表 -->
        <div class="links">
          <h3>{{ t("sidebar.link.title") }}</h3>
          <el-menu
            mode="vertical"
            :default-active="activeLink"
            @select="handleLinkSelect"
          >
            <el-menu-item index="1">
              <el-link href="https://github.com/AMDL-Web/" target="_blank">{{
                t("sidebar.link.github")
              }}</el-link>
            </el-menu-item>
            <el-menu-item index="2">
              <el-link
                href="https://github.com/AMDL-Web/webui/issues"
                target="_blank"
                >{{ t("sidebar.link.issue") }}</el-link
              >
            </el-menu-item>
            <el-menu-item index="3">
              <el-link
                href="https://github.com/AMDL-Web/webui"
                target="_blank"
                >{{ t("sidebar.link.discussions") }}</el-link
              >
            </el-menu-item>
          </el-menu>
        </div>

        <!-- 语言切换 -->
        <div class="language-switch">
          <h3>{{ t("sidebar.language") }}</h3>
          <el-select
            v-model="currentLocale"
            @change="changeLocale"
            placeholder="选择语言"
            style="width: 100%"
          >
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </div>
      </div>
    </el-drawer>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useI18n } from "vue-i18n";

const { t } = useI18n();

// 侧边栏可见性
const sidebarVisible = ref(false);

// 激活的链接
const activeLink = ref("1");

// 国际化
const { locale } = useI18n();
const currentLocale = ref("zh-CN");

// 语言选项
const options = [
  {
    value: "zh-CN",
    label: "中文",
  },
  {
    value: "en-US",
    label: "English",
  },
  {
    value: "ja-JP",
    label: "日本語",
  },
  {
    value: "fr-FR",
    label: "Français",
  },
  {
    value: "es-ES",
    label: "Español",
  },
];

// 切换侧边栏
const toggleSidebar = () => {
  sidebarVisible.value = !sidebarVisible.value;
};

// 处理链接选择
const handleLinkSelect = (index: string) => {
  activeLink.value = index;
};

// 切换语言
const changeLocale = () => {
  locale.value = currentLocale.value;
  // 保存用户选择的语言到localStorage
  localStorage.setItem("language", currentLocale.value);
  // 修改网页头的lang属性
  document.documentElement.lang = currentLocale.value;
};

// 页面加载时读取用户之前选择的语言
onMounted(() => {
  const savedLanguage = localStorage.getItem("language");
  if (savedLanguage) {
    currentLocale.value = savedLanguage;
    locale.value = savedLanguage;
  }
});
</script>

<style scoped lang="stylus">
.sidebar-trigger
  position fixed
  top 20px
  left 20px
  z-index 1000

.sidebar-content
  padding 20px

.links
.language-switch
  margin-bottom 30px

  h3
    margin-top 0


.button
  display block
  position relative
  width 56px
  height 56px
  margin 0
  overflow hidden
  outline none
  background-color transparent
  cursor pointer
  border 0

  &:before
  &:after
    content ""
    position absolute
    border-radius 50%
    inset 7px

  &:before
    border 4px solid #f0eeef
    transition opacity 0.4s cubic-bezier(0.77, 0, 0.175, 1) 80ms,
               transform 0.5s cubic-bezier(0.455, 0.03, 0.515, 0.955) 80ms

  &:after
    border 4px solid #96daf0
    transform scale(1.3)
    transition opacity 0.4s cubic-bezier(0.165, 0.84, 0.44, 1),
               transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)
    opacity 0

  &:hover:before
  &:focus:before
    opacity 0
    transform scale(0.7)
    transition opacity 0.4s cubic-bezier(0.165, 0.84, 0.44, 1),
               transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94)

  &:hover:after
  &:focus:after
    opacity 1
    transform scale(1)
    transition opacity 0.4s cubic-bezier(0.77, 0, 0.175, 1) 80ms,
               transform 0.5s cubic-bezier(0.455, 0.03, 0.515, 0.955) 80ms

.button-box
  display flex
  position absolute
  top 0
  left 0

.button-elem
  display block
  width 20px
  height 20px
  margin 17px 18px 0 18px
  transform rotate(180deg)
  fill #f0eeef

.button:hover .button-box
.button:focus .button-box
  transition 0.4s
  transform translateX(-56px)
</style>
