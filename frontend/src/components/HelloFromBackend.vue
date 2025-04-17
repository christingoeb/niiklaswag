<!-- frontend/src/components/HelloFromBackend.vue -->
<template>
    <div>
        <p>{{ message }}</p>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const message = ref('Warte auf Antwort...')

onMounted(async () => {
    try {
        const res = await axios.get('http://127.0.0.1:5000/api/hello')
        message.value = res.data.message
    } catch (error) {
        console.error('Fehler beim Abrufen:', error)
        message.value = 'Fehler: ' + error.message
    }
})

</script>