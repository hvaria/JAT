fetch('http://localhost:5000/get-csv-row-count')
    .then(response => response.json())
    .then(data => {
        document.querySelector('.number').innerText = data.row_count;
    })
    .catch(error => console.error('Error:', error));


    
