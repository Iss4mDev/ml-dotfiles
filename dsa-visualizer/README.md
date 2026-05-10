# Algorithm Visualizer

I created this project to make learning Data Structures and Algorithms (DSA) a bit more intuitive. It's one thing to read about Bubble Sort in a book, but it's another thing entirely to watch the bars move and see the sorting happen in real-time.

## Features
- **Real-time Sorting:** Watch a Bubble Sort algorithm organize data right in your browser.
- **Interactive UI:** You can generate new random data and start the sorting process with a click.
- **Java Backend Logic:** The core algorithm logic is written in Java, serving as the foundation for the visualization.

## Tech Stack
- **Frontend:** HTML5, CSS3 (Modern Flexbox layout), and Vanilla JavaScript.
- **Backend:** Java (for the core algorithm implementations).

## How to Run It

### 1. Clone the Repository
```bash
git clone https://github.com/Iss4mDev/issam-soubra-portfolio.git
cd issam-soubra-portfolio/dsa-visualizer
```

### 2. View the Visualization
Simply open the `dsa_visualizer.html` file in any modern web browser (Chrome, Firefox, Safari, etc.). No server setup is required!

### 3. Run the Java Logic (Optional)
If you want to see the algorithm run in your terminal:
```bash
javac dsa_visualizer.java
java DSAVisualizer
```

## How it Works
The visualizer uses an asynchronous JavaScript function to step through the sorting process, updating the DOM (the bars you see on screen) at each step so you can follow along with the logic.

---
**Author:** Issam Soubra
