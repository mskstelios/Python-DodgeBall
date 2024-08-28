
<h1>Dodge Ball Game</h1>

<h2>Overview</h2>
<p>This project is a simple dodge ball game built using Python and Pygame. The player controls a circle with the mouse and tries to dodge enemies while collecting points by colliding with a square. The goal is to reach a score of 100 to win the game.</p>

<h2>Features</h2>
<ul>
    <li><strong>Player Control</strong>: Move the player-controlled circle using the mouse.</li>
    <li><strong>Difficulty Levels</strong>: Choose from Easy, Medium, Hard, and Impossible levels.</li>
    <li><strong>Collision Detection</strong>: Detects collisions between the player and the square to increase the score, and between the player and enemies to end the game.</li>
    <li><strong>Winning Condition</strong>: Reach a score of 100 to win the game.</li>
    <li><strong>Game Over</strong>: If the player collides with an enemy, the game is over, and the player can choose to restart or quit.</li>
</ul>

<h2>Prerequisites</h2>
<p>Before you begin, ensure you have met the following requirements:</p>
<ul>
    <li><strong>Python 3.x</strong>: This application requires Python 3.x. You can download it from <a href="https://www.python.org/" target="_blank">python.org</a>.</li>
    <li><strong>Pygame</strong>: Install Pygame by running the command:</li>
</ul>
<pre><code>pip install pygame</code></pre>

<h2>Installation</h2>
<ol>
    <li><strong>Clone the Repository</strong>:
        <pre><code>git clone https://github.com/mskstelios/Python-DodgeBall.git</code></pre>
    </li>
    <li><strong>Navigate to the Project Directory</strong>:
        <pre><code>cd Python-DodgeBall</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li><strong>Run the Application</strong>:
        <pre><code>python dodge.py</code></pre>
    </li>
    <li><strong>Playing the Game</strong>:
        <ul>
            <li>Use the mouse to move the circle.</li>
            <li>Collide with the square to increase your score.</li>
            <li>Enemies will appear as your score increases; avoid colliding with them.</li>
            <li>Reach a score of 100 to win.</li>
            <li>If you collide with an enemy, you will lose the game and be presented with options to restart or quit.</li>
            <li>You can press <strong>'R'</strong> to restart the game and <strong>'Q'</strong> to quit.</li>
        </ul>
    </li>
</ol>

</ul>

<h2>Media</h2>
<ul>
    <li><code>background.jpg</code>: The background image for the game window.</li>
    <li><code>square_hit.ogg</code>: Sound effect played when the player collides with the square.</li>
    <li><code>lose_sound.ogg</code>: Sound effect played when the player loses the game.</li>
    <li><code>win_sound.ogg</code>: Sound effect played when the player wins the game.</li>
</ul>

</body>
</html>

