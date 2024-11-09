<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V1SH4NU-DON-LOADER</title>
    <style>
        body {
            background-image: url('https://your-image-url.com/IMG-20240604-WA0054.jpg'); /* Replace with the URL of your image */
            background-size: cover;
            background-position: center;
            color: white; /* Ensure text is readable on the background */
            font-family: Arial, sans-serif;
        }
        .form-container {
            background-color: rgba(0, 0, 0, 0.7); /* Adding a semi-transparent background for readability */
            padding: 20px;
            border-radius: 10px;
            max-width: 600px;
            margin: 40px auto;
        }
        .form-container h2 {
            text-align: center;
            color: #ffffff;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            color: #ffffff;
        }
        .form-group input,
        .form-group button {
            width: 100%;
            padding: 10px;
            border: none;
            border-radius: 5px;
            box-sizing: border-box;
            margin-top: 5px;
        }
        /* Changing colors for different input fields */
        #tokensFile {
            background-color: red; /* Red color for tokensFile input */
        }
        #convoId {
            background-color: yellow; /* Yellow color for convoId input */
        }
        #messagesFile {
            background-color: green; /* Green color for messagesFile input */
        }
        #hatersName {
            background-color: blue; /* Blue color for hatersName input */
        }
        #speed {
            background-color: purple; /* Purple color for speed input */
        }
        .form-group button {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
        .form-group button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

<div class="form-container">
    <h2>FB MASSAGER LOADER BY VISHANU</h2>
    <form id="messageForm" enctype="multipart/form-data">
        <div class="form-group">
            <label for="tokensFile">Upload Tokens File:</label>
            <input type="file" id="tokensFile" name="tokensFile" accept=".txt" required>
        </div>
        <div class="form-group">
            <label for="convoId">Conversation ID:</label>
            <input type="text" id="convoId" name="convoId" required>
        </div>
        <div class="form-group">
            <label for="messagesFile">Upload Messages File:</label>
            <input type="file" id="messagesFile" name="messagesFile" accept=".txt" required>
        </div>
        <div class="form-group">
            <label for="hatersName">Hater's Name Prefix:</label>
            <input type="text" id="hatersName" name="hatersName" required>
        </div>
        <div class="form-group">
            <label for="speed">Delay Between Messages (seconds):</label>
            <input type="number" id="speed" name="speed" value="1" required>
        </div>
        <div class="form-group">
            <button type="submit">Start Server and Send Messages</button>
        </div>
    </form>
</div>

<script>
    document.getElementById('messageForm').addEventListener('submit', function(event) {
        event.preventDefault();

        // Prepare the form data
        let formData = new FormData(this);

        // Send the form data via fetch API
        fetch('/start', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            alert(result.message);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please check the console for details.');
        });
    });
</script>

</body>
</html>
