let lastRowCount = 0;

function checkRowCount() {
    fetch('http://localhost:5000/get-csv-row-count')
        .then(response => response.json())
        .then(data => {
            const currentRowCount = data.row_count;
            if (currentRowCount > lastRowCount) {
                lastRowCount = currentRowCount;
                chrome.notifications.create('', {
                    type: 'basic',
                    iconUrl: 'icon.png',
                    title: 'Row Count Updated',
                    message: `New row count: ${currentRowCount}`
                });
            }
        })
        .catch(error => console.error('Error:', error));
}

// Poll every 5 seconds (5000 milliseconds)
setInterval(checkRowCount, 5000);
