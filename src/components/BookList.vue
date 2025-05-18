<template>
    <div class="max-w-xl mx-auto mt-6 p-4 bg-white rounded shadow">
        <h2 class="text-2xl font-semibold mb-4">Book List</h2>

        <ul class="mb-4">
            <li v-for="book in books" :key="book.id" class="mb-2 flex justify-between items-center">
                <div>
                    <strong>{{ book.title }}</strong> by {{ book.author }}
                </div>
                <button @click="editBook(book)"
                    class="ml-2 px-2 py-1 bg-yellow-500  rounded hover:bg-yellow-600 text-sm">
                    Edit
                </button>
            </li>
        </ul>

        <button @click="toggleForm" class="mb-4 px-4 py-2 bg-blue-600  rounded hover:bg-blue-700">
            {{ showForm ? 'Cancel' : 'Add Book' }}
        </button>

        <div v-if="showForm" class="border-t pt-4">
            <form @submit.prevent="handleSubmit">
                <div class="mb-2">
                    <label class="block text-sm">Title:</label>
                    <input v-model="form.title" type="text" class="w-full px-2 py-1 border rounded" required />
                </div>
                <div class="mb-2">
                    <label class="block text-sm">Author:</label>
                    <input v-model="form.author" type="text" class="w-full px-2 py-1 border rounded" required />
                </div>
                <div class="mb-2">
                    <label class="block text-sm">Published Date:</label>
                    <input v-model="form.published_date" type="date" class="w-full px-2 py-1 border rounded" required />
                </div>
                <button type="submit" class="mt-2 px-4 py-2 bg-green-600  rounded hover:bg-green-700">
                    {{ editMode ? 'Update Book' : 'Submit' }}
                </button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            books: [],
            showForm: false,
            editMode: false,
            editingBookId: null,
            form: {
                title: '',
                author: '',
                published_date: ''
            }
        };
    },
    created() {
        this.fetchBooks();
    },
    methods: {
        fetchBooks() {
            axios.get('http://127.0.0.1:8000/api/books/')
                .then(response => {
                    this.books = response.data;
                })
                .catch(error => {
                    console.error(error);
                });
        },
        toggleForm() {
            this.resetForm();
            this.showForm = !this.showForm;
        },
        handleSubmit() {
            if (this.editMode) {
                this.updateBook();
            } else {
                this.submitBook();
            }
        },
        submitBook() {
            axios.post('http://127.0.0.1:8000/api/books/', this.form)
                .then(() => {
                    this.fetchBooks();
                    this.resetForm();
                    this.showForm = false;
                })
                .catch(error => {
                    console.error(error);
                });
        },
        editBook(book) {
            this.form.title = book.title;
            this.form.author = book.author;
            this.form.published_date = book.published_date;
            this.editMode = true;
            this.editingBookId = book.id;
            this.showForm = true;
        },
        updateBook() {
            axios.put(`http://127.0.0.1:8000/api/books/${this.editingBookId}/`, this.form)
                .then(() => {
                    this.fetchBooks();
                    this.resetForm();
                    this.showForm = false;
                })
                .catch(error => {
                    console.error(error);
                });
        },
        resetForm() {
            this.form = {
                title: '',
                author: '',
                published_date: ''
            };
            this.editMode = false;
            this.editingBookId = null;
        }
    }
};
</script>

<style scoped>
input:focus {
    outline: none;
    border-color: #3182ce;
    box-shadow: 0 0 0 1px #3182ce;
}

button {
    color: black;
}
</style>