const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  // devServer: {
  //   proxy: {
  //     "/api": {
  //       target: "http://localhost:8001",
  //     },
  //     // "/staff": {
  //     //   target: "http://localhost:8001",
  //     //   changeOrigin: true,
  //     //   pathRewrite: {
  //     //     "^/staff": "/api",
  //     //   },
  //     // },
  //     // "/staff": {
  //     //   target: "http://localhost:8001",
  //     //   changeOrigin: true,
  //     //   pathRewrite: {
  //     //     "^/staff": "/api",
  //     //   },
  //     // },
  //     "/customer": {
  //       target: "http://localhost:8002",
  //     },
  //     "/storage": {
  //       target: "http://localhost:8003",
  //     },
  //   },
  // },
});
