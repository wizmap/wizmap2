import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import router from './routers/index.js'

loadFonts()

// createApp(App)
//   .use(vuetify)
//   .mount('#app')


const app = createApp(App).use(vuetify)
app.use(router)  // router 추가
app.mount('#app')

