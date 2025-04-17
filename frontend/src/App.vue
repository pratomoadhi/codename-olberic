<!-- <script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div>
    <a href="https://vite.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" />
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style> -->

<template>
  <main class="p-6 font-sans">
    <div class="flex justify-between items-center mb-4">
      <h1 class="text-2xl font-bold">Digital Learning Platform</h1>
      <div>
        <button v-if="isLoggedIn" @click="showCourses"
          class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 mr-2">
          Courses
        </button>
        <button v-if="isLoggedIn" @click="showProfile"
          class="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 mr-2">
          Profile
        </button>
        <button v-if="isLoggedIn" @click="logout" class="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600">
          Logout
        </button>
      </div>
    </div>

    <LoginForm v-if="!isLoggedIn && currentPage === 'login'" @login-success="checkLogin" />
    <CourseList v-else-if="isLoggedIn && currentPage === 'courses'" />
    <UserProfile v-else-if="isLoggedIn && currentPage === 'profile'" />
  </main>
</template>

<script setup>
import { ref } from 'vue';
import CourseList from './components/CourseList.vue';
import LoginForm from './components/LoginForm.vue';
import UserProfile from './components/UserProfile.vue';

const isLoggedIn = ref(localStorage.getItem('access') !== null);
const currentPage = ref('courses');

function logout() {
  localStorage.removeItem('access');
  localStorage.removeItem('refresh');
  isLoggedIn.value = false;
  currentPage.value = 'login';
}

// Recheck login status after LoginForm emits success
function checkLogin() {
  isLoggedIn.value = localStorage.getItem('access') !== null;
  if (isLoggedIn.value) {
    currentPage.value = 'courses';
  } else {
    currentPage.value = 'login';
  }
}

function showProfile() {
  currentPage.value = 'profile';
}

function showCourses() {
  currentPage.value = 'courses';
}
</script>
