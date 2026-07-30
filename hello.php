<?php
// --- Backend Logic ---

// Hardcoded mock credentials for the sake of this activity
$valid_username = "admin";
$valid_password = "password123";

$message = "";

// Check if the user submitted the form
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Grab the data typed into the form
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Verify if the credentials match our system
    if ($username === $valid_username && $password === $valid_password) {
        $message = "✅ Login successful! Welcome, " . htmlspecialchars($username) . ".";
    } else {
        $message = "❌ Invalid username or password. Please try again.";
    }
}
?>

<!-- --- Frontend Visuals --- -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Information System - Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-box {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 300px;
        }
        h2 { text-align: center; color: #333; }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #0366d6;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover { background-color: #0056b3; }
        .message { margin-top: 15px; text-align: center; font-weight: bold; }
    </style>
</head>
<body>

<div class="login-box">
    <h2>System Login</h2>
    <form method="POST" action="login.php">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        
        <button type="submit">Login</button>
    </form>
    
    <!-- This PHP block displays the success or error message -->
    <?php if ($message != ""): ?>
        <div class="message"><?php echo $message; ?></div>
    <?php endif; ?>
</div>

</body>
</html>
