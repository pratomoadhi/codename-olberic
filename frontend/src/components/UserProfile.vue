<template>
    <div class="profile-container">
        <h1 class="profile-title">User Profile</h1>

        <div class="profile-info">
            <h2>Personal Information</h2>
            <p><strong>Username:</strong> {{ userProfile.username }}</p>
            <p v-if="userProfile.email"><strong>Email:</strong> {{ userProfile.email }}</p>
        </div>

        <div class="enrollments">
            <h2>Your Enrollments</h2>
            <ul v-if="enrollmentList.length">
                <li v-for="enrollment in enrollmentList" :key="enrollment.id" class="enrollment-item">
                    <strong>Course:</strong> {{ enrollment.course.title }}
                    <span v-if="enrollment.enrollment_date">
                        (Enrolled on: {{ enrollment.enrollment_date }})
                    </span>
                </li>
            </ul>
            <p v-else class="no-enrollments">You are not currently enrolled in any courses.</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const userProfile = ref({});
const enrollmentList = ref([]);
const error = ref('');

onMounted(async () => {
    try {
        const userId = localStorage.getItem('userId');

        if (userId) {
            // Fetch user profile data using the /api/user/:id endpoint
            const profileResponse = await axios.get(`http://localhost:8000/api/users/${userId}/`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('access')}`
                }
            });
            userProfile.value = profileResponse.data;
        } else {
            error.value = 'User ID not found.';
            console.error('User ID not found in local storage.');
            // Optionally handle the case where the user ID is not available
        }

        // // Fetch user's enrollment list (assuming an endpoint like /api/enrollments/user/)
        // const enrollmentResponse = await axios.get('http://localhost:8000/api/enrollments/user/', {
        //     headers: {
        //         Authorization: `Bearer ${localStorage.getItem('access')}`
        //     }
        // });
        // enrollmentList.value = enrollmentResponse.data;

    } catch (err) {
        console.error('Error fetching profile or enrollments:', err);
        error.value = 'Failed to load profile information.';
        // Optionally handle unauthorized errors (e.g., redirect to login)
        if (err.response && err.response.status === 401) {
            // Handle unauthorized access
            console.error('Unauthorized. Redirecting to login.');
            // router.push('/login'); // Assuming you are using Vue Router
        }
    }
});
</script>

<style scoped>
.profile-container {
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile-title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 20px;
    text-align: center;
    color: #333;
}

.profile-info {
    margin-bottom: 30px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.profile-info h2 {
    font-size: 1.5rem;
    margin-bottom: 10px;
    color: #555;
}

.profile-info p {
    margin-bottom: 8px;
    color: #777;
}

.enrollments h2 {
    font-size: 1.5rem;
    margin-bottom: 10px;
    color: #555;
}

.enrollments ul {
    list-style: none;
    padding: 0;
}

.enrollment-item {
    padding: 10px 0;
    border-bottom: 1px solid #eee;
}

.enrollment-item:last-child {
    border-bottom: none;
}

.no-enrollments {
    color: #999;
    font-style: italic;
}
</style>