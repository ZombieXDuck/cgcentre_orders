<template>
  <div id="app">
    <aside class="side-menu">
      <p class="side-menu-title">
        CGCenter Orders
      </p>
      <ul class="list-group">
        <li class="side-menu-list-item-container">
          <router-link class="side-menu-list-item" to="suppliers">
            Suppliers
          </router-link>
        </li>
        <li class="side-menu-list-item-container">
          <router-link class="side-menu-list-item" to="orders">Orders</router-link>
        </li>
      </ul>
    </aside>
    <div class="router-view-container">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.side-menu {
  padding: 50px 0 0 0;
  width: 300px;
  height: 100vh;
  position: absolute;
  background: #323439;
}

.side-menu-title {
  color: #c3c3c3!important;
  margin-bottom: 20px;
  font-size: 1.2em;
}

.side-menu-list-item-container {
  color: #c3c3c3!important;
  margin: 10px 0;
}

.side-menu-list-item {
  color: #c3c3c3!important;
}

.router-link-exact-active {
  color: white!important;
  text-decoration: underline;
}

.router-view-container {
  width: 100%;
  padding-left: 300px;
  padding-top: 44px;
  overflow: auto;
}
</style>
