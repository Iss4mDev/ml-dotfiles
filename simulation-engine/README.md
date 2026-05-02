# High-Performance Simulation Engine

## Project Description

This project presents a C++ engine meticulously designed for high-performance simulations. It demonstrates robust principles of efficient memory management and computational logic, making it suitable for scenarios requiring fast and reliable simulations.

## Features

*   **Particle-Based Simulation:** Simulates the movement and interaction of particles.
*   **Efficient Memory Management:** Implemented in C++ for optimal performance and control over system resources.
*   **Euler Integration:** Uses a simple Euler integration method for updating particle positions.
*   **Basic Boundary Checks:** Includes logic for particles to 
bounce back when hitting boundaries.
*   **Performance Measurement:** Includes basic timing mechanisms to evaluate simulation speed.

## Technologies Used

*   C++
*   `iostream` for input/output operations
*   `vector` for dynamic arrays (particles)
*   `cmath` for mathematical functions
*   `chrono` for performance timing

## How to Use

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Iss4mDev/ml-dotfiles.git
    cd ml-dotfiles
    ```

2.  **Compile the engine:**

    ```bash
    g++ simulation_engine.cpp -o simulation_engine
    ```

3.  **Run the simulation:**

    ```bash
    ./simulation_engine
    ```

## Example

```cpp
int main() {
    SimulationEngine engine(0.01);
    
    // Add some initial particles
    engine.addParticle(10, 10, 1.5, 2.0, 1.0);
    engine.addParticle(50, 50, -1.0, 0.5, 1.5);
    engine.addParticle(80, 20, 0.5, -1.5, 0.8);

    std::cout << "Starting simulation..." << std::endl;
    engine.run(1000);
    engine.displayState();

    return 0;
}
```

## Author

Issam Soubra
