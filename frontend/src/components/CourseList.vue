<template>
    <div class="course-container">
        <h1 class="title">Course List</h1>
        <button @click="openCreateModal" class="create-btn">Create New Course</button>

        <div v-if="courses.length" class="course-list">
            <div v-for="course in courses" :key="course.id" class="course-card">
                <div class="course-card-header">
                    <h3 class="course-title">{{ course.title }}</h3>
                    <div class="course-actions">
                        <button @click="editCourse(course)" class="btn-edit">Edit</button>
                        <button @click="deleteCourse(course.id)" class="btn-delete">Delete</button>
                    </div>
                </div>
                <p class="course-description">{{ course.description }}</p>
            </div>
        </div>
        <p v-else class="no-courses">No courses available.</p>

        <!-- Modal for creating/editing courses -->
        <div v-if="showModal" class="modal">
            <div class="modal-content">
                <h2>{{ editingCourse ? 'Edit' : 'Create' }} Course</h2>
                <input type="text" v-model="courseForm.title" placeholder="Course Title" class="input-field" />
                <textarea v-model="courseForm.description" placeholder="Course Description"
                    class="input-field"></textarea>
                <div class="modal-actions">
                    <button @click="submitCourse" class="btn-submit">{{ editingCourse ? 'Save' : 'Create' }}</button>
                    <button @click="closeModal" class="btn-cancel">Cancel</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            courses: [],
            showModal: false,
            editingCourse: null,
            courseForm: {
                title: '',
                description: ''
            }
        };
    },
    methods: {
        fetchCourses() {
            axios.get('http://localhost:8000/api/courses/')
                .then(response => {
                    this.courses = response.data;
                })
                .catch(error => {
                    console.error('There was an error fetching courses:', error);
                });
        },
        openCreateModal() {
            this.showModal = true;
            this.editingCourse = null;
            this.courseForm = { title: '', description: '' };
        },
        closeModal() {
            this.showModal = false;
        },
        submitCourse() {
            if (this.editingCourse) {
                // Update existing course
                axios.put(`http://localhost:8000/api/courses/${this.editingCourse.id}/`, this.courseForm)
                    .then(() => {
                        this.fetchCourses();
                        this.closeModal();
                    });
            } else {
                // Create new course
                axios.post('http://localhost:8000/api/courses/', this.courseForm)
                    .then(() => {
                        this.fetchCourses();
                        this.closeModal();
                    });
            }
        },
        editCourse(course) {
            this.editingCourse = course;
            this.courseForm = { ...course };
            this.showModal = true;
        },
        deleteCourse(courseId) {
            axios.delete(`http://localhost:8000/api/courses/${courseId}/`)
                .then(() => {
                    this.fetchCourses();
                })
                .catch(error => {
                    console.error('There was an error deleting the course:', error);
                });
        }
    },
    mounted() {
        this.fetchCourses();
    }
};
</script>

<style scoped>
.course-container {
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
}

.title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 20px;
    text-align: center;
}

.create-btn {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-bottom: 30px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    font-size: 1rem;
}

.create-btn:hover {
    background-color: #45a049;
}

.course-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
}

.course-card {
    background-color: #f4f4f4;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.course-card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.course-title {
    font-size: 1.5rem;
    font-weight: bold;
    color: #333;
    /* Ensure text is visible */
}

.course-actions button {
    background-color: #f0ad4e;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
    margin-left: 5px;
}

.course-actions .btn-edit {
    background-color: #5bc0de;
}

.course-actions .btn-delete {
    background-color: #d9534f;
}

.course-actions button:hover {
    opacity: 0.8;
}

.course-description {
    font-size: 1rem;
    margin-top: 10px;
    color: #333;
}

.no-courses {
    text-align: center;
    font-size: 1.2rem;
    color: #999;
}

.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    background-color: white;
    padding: 30px;
    border-radius: 8px;
    width: 400px;
    max-width: 90%;
}

.input-field {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

.input-field:focus {
    border-color: #4CAF50;
}

.modal-actions {
    display: flex;
    justify-content: space-between;
}

.btn-submit,
.btn-cancel {
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

.btn-submit {
    background-color: #4CAF50;
    color: white;
}

.btn-submit:hover {
    background-color: #45a049;
}

.btn-cancel {
    background-color: #d9534f;
    color: white;
}

.btn-cancel:hover {
    background-color: #c9302c;
}
</style>