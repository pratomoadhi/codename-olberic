<template>
    <form @submit.prevent="login" class="max-w-sm mx-auto p-4 border rounded shadow">
        <h2 class="text-xl font-bold mb-2">Login</h2>
        <input v-model="username" placeholder="Username" class="w-full mb-2 p-2 border" />
        <input v-model="password" type="password" placeholder="Password" class="w-full mb-2 p-2 border" />
        <button class="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded" type="submit">
            Login
        </button>
        <p v-if="error" class="text-red-500 mt-2">{{ error }}</p>
    </form>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const password = ref('')
const error = ref('')

const login = async () => {
    try {
        const res = await axios.post('http://localhost:8000/api/token/', {
            username: username.value,
            password: password.value,
        })
        localStorage.setItem('access', res.data.access)
        localStorage.setItem('refresh', res.data.refresh)
        alert('Logged in successfully!')
        window.location.reload()
    } catch (err) {
        console.error(err)  // Log the full error to console for debugging
        error.value = 'Invalid credentials'
    }
}
</script>