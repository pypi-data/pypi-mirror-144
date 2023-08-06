# Adaptive multilevel splitting simulation 

## Installation

```bash
git clone <repo url>
cd AMS_Lammps
export AMS_Lammps_ROOT=$(pwd)
export PATH=$(pwd)/bin:$PATH
export PYTHONPATH=$(pwd):$PYTHONPATH
```

to automatically load the environment, one can append the following lines
to ~/.bashrc (Linux) or ~/.bash_profile (MacOS)

```bash
export AMS_Lammps_ROOT=#the path you copy the source code
export PATH=${AMS_Lammps_ROOT}/bin:$PATH
export PYTHONPATH=${AMS_Lammps_ROOT}:$PYTHONPATH
```

### prerequisites

* Numpy
* LimpyAp

## use the software

```bash
run_ams -input <input filename for parameters>
```

## Algorithm

 1. read initial configuration
 2. run initial MD 
 3. scan the hitting points at the initial RC surface
 4. store configurations of the hitting points
 5. run multiple simulations with these configurations as starting points
 6. batch analysis of RC for the trajectories
 7. determine killing levels and new starting points
 8. repeat 5-7 till it hits the final states

## user input needed

* hyper-parameters for AMS
  * xi_min, intermediate value to start the reaction
  * xi_max, maximum reaction coordinate for final configurations
  * xi_initial, value for initial basin
  * xi_final, value for final basin
  * N, total number of replica for each iteration
  * k, number of replicas to kill at each iteration
* parameters for MD/MC simulations
  * which package to use
  * input files for the package
  * temprary work folder

## package integration

* for MD/MC engine
  * LAMMPS
  * CP2K
  * homebrew ND energy landscape explorer
  * homebrew MC code for discrete-state hamiltonian
* for collective variable analysis
  * PLUMED
  * Tensorflow

## References

This code follows the algorithm in J. Comput. Chem. 2019, 40, 1198–1208 by Laura J. S. Lopes and Tony Lelièvre.

