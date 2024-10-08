document.getElementById('prediction-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const last_locked_hour = document.getElementById('last_locked_hour').value;
    const last_locked_min = document.getElementById('last_locked_min').value;
    const current_time_hour = document.getElementById('current_time_hour').value;
    const current_time_min = document.getElementById('current_time_min').value;

    const data = {
        last_locked_hour: Number(last_locked_hour),
        last_locked_min: Number(last_locked_min),
        current_time_hour: Number(current_time_hour),
        current_time_min: Number(current_time_min)
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = `Prediction: ${data.prediction}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
