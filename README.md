# ABAQUS Automation
*Iterative part topology optimization by minimum-stress element pruning in **Python** with **ABAQUS** backend.*

This code accompanies a final project submission for **MECH 321: Deformable Solids** at McGill University in Montreal, Canada.

## Context
In this project, we were tasked with optimizing a simple 2D part geometry to withstand a 7 mm deformation at 850 N of force while minimizing mass.
Other constraints included a minimum 10 mm radius of material about holes, a maximum of 5 internal cuts, and a minimum cutting radius of 10 mm. 
The final part geometry was lasercut from 3 mm acrylic (the material properties of acrylic were given) and stress-tested in real life.

The FEA (stress simulation) software supplied for the project was **ABAQUS Student Edition**, but the repetitive nature of the task called for some **Python**.

## Code
The Python functions used for automating the broad strokes of ABAQUS are included in `abaqusMacros.py`:
  * `partSetup()` builds the part geometry, creates a section, assigns a material, applies an instance, submits the job for simulation, and saves a screenshot of the analysis results in the working directory.
  * `submitJob()` submits a job for simulation and saves a screenshot of the results.
  * `removeElement()` is where it gets more interesting. This function opens a `.inp` file (the file that defines a simulation), creates an array of elements and their connections, removes the unwanted element and writes an updated `.inp`.
  * `findMin()` uses a bubblesort algorithm to find the element with the lowest stress, then passes that element's index to `removeElement()`.
  
By running `findMin()` then `submitJob()` a finite number of times, the code provides direction to an optimized part geometry.

## Limitations
After the major bugs in the code were ironed out, a glaring flaw in the optimization methodology remained. Elements in ABAQUS tend to be square-shaped (or triangular or pentagonal). This means that removing an element from the edge of a part leaves several sharp corners. This makes mechanical engineers shudder. Sharp corners in manufactured parts tend to cause stress concentrations, because they prevent internal stresses from evenly distributing. Thus, the corners created by the method skewed the location of low-stress elements.

To remedy this problem, we manually fine-tuned the part after coarse-grained optimization by the *algorithm*.

In the future, having learned the basics of the ABAQUS-Python interface, I would implement a state-of-the-art optimization algorithm while focusing on speed, convergence, and verifiability.
