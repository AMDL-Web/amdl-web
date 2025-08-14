import { createI18n } from "vue-i18n";

import zhCN from "../locales/zh-CN.json";
import enUS from "../locales/en-US.json";
import jaJP from "../locales/ja-JP.json";
import frFR from "../locales/fr.json";
import esES from "../locales/es.json";

const messages = {
  "zh-CN": zhCN,
  "en-US": enUS,
  "ja-JP": jaJP,
  "fr-FR": frFR,
  "es-ES": esES,
};

const savedLocale = localStorage.getItem("language") || "zh-CN";

const i18n = createI18n({
  legacy: false,
  locale: savedLocale,
  fallbackLocale: "en-US",
  messages,
});

export default i18n;
