<h1>Week 8 Supermarket Simulation</h1>

**Project Goal:** To build a Supermarket Simulation that simulates customer behaviour moving through the aisles of a supermarket based on the MCMC model

<h2> Description</h2>

- Data previously collected on customer behaviour in a store is used to create a probability matrix on transition states at one-minute intervals.

- Based on this probability matrix, the MCMC model is used to generate a CSV table that illustrates customers behaviours from when they enter to when the leave the store at one-minute intervals.

<h2>Project Set-Up</h2>

- This was model was developed as a group during Week 8 of Spiced Academy. All team files are stored in a separate GitHub repo. 

- The current working model of my student-code repo was developed outside of the full Supermarket Simulator created as a team. Two classes, Supermarket and Customer, were created to model how a single customer acts and how mulitple customers behave respectively. A single 'input collecter' takes data from the user (store opening/closing times etc) to then begin the simulation and generate an example of a single day at the store.

- A single CSV output file of the model is stored as "simulated_market_output.csv"

- TODO - this folder needs to be cleaned a bit to separate team files from solo work. A single runthru file is required to demonstrate full group work.

- TODO - a numpy-array based animation of customers moving through the store would be nice, but an extra bonus to be added after graduation.

