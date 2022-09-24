const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      "^/customer": {
        target: "http://localhost:8002",
        secure: false,
        changeOrigin: true,
        pathRewrite: {
          "^/customer": "/api",
        },
        logLevel: "debug",
      },
      "^/storage": {
        target: "http://localhost:8003",
        secure: false,
        changeOrigin: true,
        pathRewrite: {
          "^/storage": "/api",
        },
        logLevel: "debug",
      },
    },
  },
})
