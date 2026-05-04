<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="layout">
    <!-- 顶部 Header -->
    <header class="layout-header">
      <nav class="layout-nav">
        <a href="">111111111</a>
        <RouterLink to="/" class="nav-link">Home</RouterLink>
        <RouterLink to="/about" class="nav-link">About</RouterLink>
      </nav>
    </header>

    <!-- 中间内容区 -->
    <main class="layout-main">
      <RouterView />
    </main>

    <!-- 底部 Footer -->
    <footer class="layout-footer">
      <p>&copy;2026 interset-wq</p>
    </footer>
  </div>
</template>

<style scoped>
/* 整体布局容器，实现 footer 自动吸底 */
.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  margin: 0;
}

/* 顶部导航栏 */
.layout-header {
  border-bottom: 1px solid #e5e7eb;
  background-color: pink;
  height: 50px;
  padding: 0 2rem;
}

.layout-nav {
  display: flex;
  gap: 2rem;
  height: 64px;
  align-items: center;
}

.nav-link {
  text-decoration: none;
  font-size: 1.25rem;
  color: #42b883;
  font-weight: 600;
  transition: color 0.2s;
}

.nav-link:hover {
  color: #35495e;
}

.nav-link.router-link-exact-active {
  color: #35495e;
  border-bottom: 2px solid #35495e;
}

/* 中间内容区：占满剩余高度，不挤压 footer */
.layout-main {
  flex: 1;
  padding: 1rem 2rem;
}

/* 页脚 */
.layout-footer {
  border-top: 1px solid #e5e7eb;
  text-align: center;
  padding: 1.5rem 0;
  font-size: 0.9rem;
  color: #6b7280;
  background-color: #f9fafb;
}
</style>
