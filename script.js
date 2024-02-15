document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];
    if (!file) {
        document.getElementById('error-msg').innerText = 'Please select a file.';
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Handle the response data
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('error-msg').innerText = 'An error occurred while uploading the file.';
    });
});
