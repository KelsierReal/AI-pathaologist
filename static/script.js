document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    // Drag-and-drop functionality
    const dropZone = document.querySelector('.drop-zone');
    const fileInput = document.querySelector('#image-upload');
    const submitBtn = document.querySelector('#submit-btn');
    const resultText = document.querySelector('#result-text');
    const imagePreview = document.querySelector('#image-preview');
    const loadingSpinner = document.querySelector('#loading');

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        const files = e.dataTransfer.files;
        if (files.length) {
            fileInput.files = files;
        }
    });

    dropZone.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length) {
            dropZone.querySelector('p').textContent = `Selected: ${fileInput.files[0].name}`;
        }
    });

    // Form submission with AJAX
    submitBtn.addEventListener('click', () => {
        if (!fileInput.files.length) {
            alert('Please select an image.');
            return;
        }

        const formData = new FormData();
        formData.append('image', fileInput.files[0]);

        loadingSpinner.style.display = 'block';
        resultText.innerHTML = '';
        image
