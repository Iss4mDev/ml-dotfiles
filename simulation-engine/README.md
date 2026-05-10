# Particle Physics Simulation Engine

I built this C++ engine to dive deep into how physics simulations actually work under the hood. Instead of relying on high-level libraries, I wanted to handle the memory management and math myself to see how much performance I could squeeze out of it.

## Why I Built This
Most modern engines hide the "boring" stuff like memory allocation and integration steps. I wanted to see the "boring" stuff. This project was a way for me to bridge the gap between low-level C++ and real-world computational logic.

## Core Features
- **Particle Dynamics:** Real-time tracking of position, velocity, and mass for multiple objects.
- **Manual Memory Control:** No garbage collection here. I handle the resources directly to keep things lean.
- **Euler Integration:** A straightforward but effective way to step the simulation forward frame by frame.
- **Bounce Logic:** Particles detect the boundaries of their 100x100 world and bounce back with a bit of energy loss for realism.
- **Performance Tracking:** Built-in timers to measure exactly how long each simulation run takes.

## Tech Stack
- **Language:** C++
- **Libraries:** `iostream` (I/O), `vector` (dynamic lists), `cmath` (physics math), `chrono` (timing).

## Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/Iss4mDev/issam-soubra-portfolio.git
cd issam-soubra-portfolio/simulation-engine
```

### 2. Compile the Code
You'll need a C++ compiler like `g++` installed.
```bash
g++ simulation_engine.cpp -o simulation_engine
```

### 3. Run the Simulation
```bash
./simulation_engine
```

## Quick Example
Here's a snippet of how the engine is initialized and run in the code:

```cpp
int main() {
    // Start the engine with a 0.01s time step
    PhysicsEngine engine(0.01);
    
    // Drop some particles into the world
    engine.spawnParticle(10.0, 10.0, 2.5, 3.0, 1.0);
    engine.spawnParticle(50.0, 50.0, -1.2, 0.8, 1.5);
    
    // Run for 5000 steps
    engine.run(5000);
    engine.printStatus();
    
    return 0;
}
```

---
**Author:** Issam Soubra
