import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), vueJsx()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      '^/customer': {
        target: 'http://localhost:8020',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/customer/, '/api')
      },
      '^/storage': {
        target: 'http://localhost:8030',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/storage/, '/api')
      }
    }
  }
})
