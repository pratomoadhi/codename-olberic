<template>
    <nav class="navbar">
        <router-link to="/">Home</router-link>
        <router-link to="/courses">Courses</router-link>
        <button v-if="isLoggedIn" @click="logout">Logout</button>
        <router-link v-else to="/login">Login</router-link>
    </nav>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const isLoggedIn = !!localStorage.getItem('access')

function logout() {
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
    router.push('/login')
}
</script>

<style scoped>
.navbar {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    background: #f2f2f2;
}

button {
    cursor: pointer;
}
</style>