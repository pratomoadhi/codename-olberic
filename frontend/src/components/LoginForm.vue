<template>
    <form @submit.prevent="login" class="login-form">
        <h2 class="login-title">Login to Your Account</h2>

        <div class="form-group">
            <label for="username" class="form-label">Username</label>
            <input v-model="username" id="username" placeholder="Enter your username" class="form-input" />
        </div>

        <div class="form-group">
            <label for="password" class="form-label">Password</label>
            <input v-model="password" id="password" type="password" placeholder="Enter your password"
                class="form-input" />
        </div>

        <button type="submit" class="login-button">
            Login
        </button>

        <p v-if="error" class="login-error">{{ error }}</p>
    </form>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const username = ref('');
const password = ref('');
const error = ref('');
const emit = defineEmits(['login-success']);

const login = async () => {
    try {
        const res = await axios.post('http://localhost:8000/api/token/', {
            username: username.value,
            password: password.value,
        });
        localStorage.setItem('access', res.data.access);
        localStorage.setItem('refresh', res.data.refresh);
        localStorage.setItem('userId', res.data.user_id);

        emit('login-success');
    } catch (err) {
        console.error(err);
        error.value = 'Invalid credentials';
    }
};
</script>

<style scoped>
.login-form {
    max-width: 400px;
    /* Equivalent to max-w-md */
    margin: 40px auto;
    /* Equivalent to mt-10 mx-auto */
    padding: 24px;
    /* Roughly equivalent to p-6 */
    background-color: white;
    border: 1px solid #e5e7eb;
    /* Equivalent to border border-gray-200 */
    border-radius: 12px;
    /* Equivalent to rounded-2xl */
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    /* Equivalent to shadow-md */
}

.dark .login-form {
    background-color: #272727;
    /* Dark background */
    border-color: #4a5568;
    /* Dark border */
}

.login-title {
    font-size: 1.5rem;
    /* Slightly smaller than text-2xl for better readability */
    font-weight: bold;
    color: #374151;
    /* Equivalent to text-gray-800 */
    margin-bottom: 16px;
    /* Equivalent to mb-4 */
    text-align: center;
}

.dark .login-title {
    color: #f3f4f6;
    /* Dark text */
}

.form-group {
    margin-bottom: 16px;
    /* Equivalent to mb-4 */
}

.form-label {
    display: block;
    margin-bottom: 4px;
    /* Equivalent to mb-1 */
    font-size: 0.875rem;
    /* Equivalent to text-sm */
    font-weight: medium;
    color: #4b5563;
    /* Equivalent to text-gray-700 */
}

.dark .form-label {
    color: #d1d5db;
    /* Dark text */
}

.form-input {
    width: 100%;
    /* Equivalent to w-full */
    padding: 8px 16px;
    /* Roughly equivalent to px-4 py-2 */
    border: 1px solid #d1d5db;
    /* Equivalent to border border-gray-200 */
    border-radius: 8px;
    /* Equivalent to rounded-lg */
    outline: none;
    /* Remove default focus outline */
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

.form-input:focus {
    border-color: #38a169;
    /* Equivalent to focus:ring-green-400 (border color) */
    box-shadow: 0 0 0 2px rgba(56, 161, 105, 0.5);
    /* Equivalent to focus:ring-green-400 (ring) */
}

.dark .form-input {
    background-color: #374151;
    /* Dark background */
    color: #f9fafb;
    /* Dark text */
    border-color: #4a5568;
    /* Dark border */
}

.login-button {
    width: 100%;
    /* Equivalent to w-full */
    background-color: #48bb78;
    /* Equivalent to bg-green-500 */
    color: white;
    font-weight: bold;
    /* Equivalent to font-semibold */
    padding: 8px 16px;
    /* Equivalent to py-2 px-4 */
    border-radius: 8px;
    /* Equivalent to rounded-lg */
    transition: background-color 0.15s ease-in-out;
    /* Equivalent to transition duration-200 */
    cursor: pointer;
    border: none;
}

.login-button:hover {
    background-color: #38a169;
    /* Equivalent to hover:bg-green-600 */
}

.login-error {
    color: #e53e3e;
    /* Equivalent to text-red-500 */
    font-size: 0.875rem;
    /* Equivalent to text-sm */
    margin-top: 12px;
    /* Equivalent to mt-3 */
    text-align: center;
    /* Equivalent to text-center */
}
</style>