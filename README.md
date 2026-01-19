<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Logistic Regression – Student Pass Prediction Web App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            padding: 20px;
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: #ffffff;
            padding: 25px;
            border-radius: 10px;
        }
        h1 {
            color: #2c3e50;
        }
        h2 {
            color: #34495e;
            margin-top: 25px;
        }
        ul {
            margin-left: 20px;
        }
        hr {
            margin: 25px 0;
        }
        pre {
            background: #eef2f5;
            padding: 15px;
            border-radius: 8px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

<div class="container">

    <h1>Logistic Regression – Student Pass Prediction Web App</h1>

    <h2>📌 Project Overview</h2>
    <p>
        This project is a Machine Learning web application that predicts whether a student will
        <strong>Pass or Fail</strong> based on:
    </p>
    <ul>
        <li>Study Hours</li>
        <li>Attendance Percentage</li>
    </ul>
    <p>
        It uses <strong>Logistic Regression</strong>, a supervised classification algorithm, and
        integrates the trained model with a simple web interface using Flask.
    </p>

    <hr>

    <h2>🎯 Objective</h2>
    <p>To demonstrate an <strong>end-to-end Machine Learning project</strong>, including:</p>
    <ul>
        <li>Data preparation</li>
        <li>Model training</li>
        <li>Model deployment</li>
        <li>Web integration</li>
    </ul>

    <hr>

    <h2>🧠 Algorithm Used</h2>
    <ul>
        <li>Logistic Regression (Binary Classification)</li>
    </ul>
    <p><strong>Output:</strong></p>
    <ul>
        <li>1 → Pass</li>
        <li>0 → Fail</li>
    </ul>

    <hr>

    <h2>🛠 Technologies Used</h2>
    <ul>
        <li>Python</li>
        <li>Flask</li>
        <li>Scikit-learn</li>
        <li>Pandas</li>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
    </ul>

    <hr>

    <h2>📁 Project Structure</h2>
    <pre>
logistic-regression-project/
│
├── model.py
├── app.py
├── model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
    </pre>

</div>

</body>
</html>
