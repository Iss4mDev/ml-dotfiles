High-Performance Simulation Engine
Project Description
I built this simulation engine in C++ to explore what's actually possible when you take memory management seriously. The goal was simple: make something fast, make it reliable, and understand every byte of what's happening under the hood. It's been one of my most hands-on projects for bridging low-level programming with real computational logic.
Features

Particle-Based Simulation: Tracks how particles move and interact with each other over time.
Manual Memory Control: Written in C++ so I have direct control over how resources are allocated and freed, no garbage collector babysitting me.
Euler Integration: Straightforward method for stepping particle positions forward each frame; simple but effective for this scale.
Boundary Collision Logic: Particles detect edges and bounce back, keeping the simulation contained and realistic.
Built-in Performance Timing: I wired in timing from the start so I could actually measure speed and spot bottlenecks early.

Technologies Used

C++
iostream for input/output operations
vector for managing the dynamic particle list
cmath powers the math behind movement calculations
chrono for recording and measuring simulation performance

How to Use

Clone the repository:

bash    git clone https://github.com/Iss4mDev/ml-dotfiles.git
    cd ml-dotfiles

Compile the engine:

bash    g++ simulation_engine.cpp -o simulation_engine

Run the simulation:

bash    ./simulation_engine
Example
cppint main() {
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
Author
Issam Soubra
