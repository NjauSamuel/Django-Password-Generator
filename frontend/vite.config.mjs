import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import { resolve } from 'path'
import { fileURLToPath } from 'url'

const __dirname = fileURLToPath(new URL('.', import.meta.url))

export default defineConfig({
  root: __dirname,
  plugins: [
    tailwindcss(),
  ],
  build: {
    outDir: resolve(__dirname, '../static/dist'),
    emptyOutDir: true,
    rollupOptions: {
      output: {
        assetFileNames: (assetInfo) => {
          if (assetInfo.name === 'style.css') {
            return 'css/style.css'
          }
          return 'assets/[name][extname]'
        },
      },
    },
  },
  base: '/static/dist/',
})
