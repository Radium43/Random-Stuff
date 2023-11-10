const express = require('express');
const app = express();
const port = 3000;
const codeIdeas = [
    'Build a To-Do App',
    'Create a Weather App',
    'Design a Chat Application',
    'Develop a Blogging Platform',
    'Build a Recipe Finder',
    'Implement a Currency Converter',
    'Create a Music Player',
    'Build a File Explorer',
    'Develop a Quiz App',
    'Design a Personal Portfolio Website',
    'Build a Calculator',
    'Create a Social Media Dashboard',
    'Implement a URL Shortener',
    'Build a Note-Taking App',
    'Develop a Pomodoro Timer',
    'Design a Memory Game',
    'Create a Fitness Tracker',
    'Build a Movie Recommendation App',
    'Implement a Drawing Board',
    'Create a Virtual Dice Roller',
    'Build a Budget Tracker',
    'Develop a News Aggregator',
    'Design a Task Scheduler',
    'Create a Space Invaders Game',
    'Build a Barcode Scanner',
    'Implement a Chatbot',
    'Create a Language Learning App',
    'Develop a Cryptocurrency Tracker',
    'Design a Recipe Sharing Platform',
    'Build a 2D Platformer Game',
    'Build a Chatbot for Customer Support',
    'Create a Personal Finance Tracker',
    'Develop a Virtual Assistant',
    'Design a Weather Dashboard with Maps',
    'Build a Recipe Recommendation System',
    'Implement a Blog Commenting System',
    'Create a Real-time Collaboration Tool',
    'Develop a Sudoku Solver',
    'Build a Chess Game',
    'Design an E-commerce Platform',
    'Implement a Social Media Analytics Dashboard',
    'Create a Password Manager',
    'Build a Space Exploration Simulation',
    'Develop a File Sharing Platform',
    'Design a Virtual Classroom Platform',
    'Create a Video Streaming Service',
    'Build a Traffic Monitoring System',
    'Implement a Code Snippet Manager',
    'Design an Expense Tracker App',
    'Develop a Task Automation Tool',
];

app.get('/random', (req, res) => {
    const randomIndex = Math.floor(Math.random() * codeIdeas.length);
    const randomIdea = codeIdeas[randomIndex];
    res.json({ idea: randomIdea });
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}/Random`);
});

// i got a Bit Lazy and did not want to find a api so i just found a bunch on github and added it