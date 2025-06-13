### You can find the necessary files and step-by-step instructions to build a 12-strand 3xG4C2 RNA system with 17mM NaCl, 10mM MgCl₂, and a 30nm simulation box. The same strategy has been applied to build the 5xG4C2 and 8xG4C2 RNA systems under varying salt concentrations. 

### The first two steps are common for all salt conditions: prepare a 15 nm × 10 nm × 15 nm solvent box system for salt addition
gmx editconf -f 3xG4C2.pdb -box 15 10 15 -center 7.5 5 7.5 -o 3xG4C2_151015.gro
gmx solvate -cp 3xG4C2_151015.gro -cs water.gro -o 3xG4C2_solv.gro -p topol.top

### Add desired salt concentration automatically via Python script
./17NaCl_10MgCl2.py

### Energy minimization
gmx grompp -f min.mdp -c ion_2.gro -p topol.top -o min.tpr -maxwarn 3
gmx mdrun -v -deffnm min -nt 4

### Replicate system to create 12-strands RNA in a 30 nm × 30 nm × 30 nm box
gmx genconf -f min.gro -o min_12.gro -dist 0 0 0 -nbox 2 3 2
### Update topol.top file for 12 molecules (manual step)

### Energy minimization for replicated system
gmx grompp -f min.mdp -c min_12.gro -p topol.top -o min12.tpr -maxwarn 3
gmx mdrun -v -deffnm min12

### Create index group for water and ions (W_ION)
gmx make_ndx -f min12.gro

### Equilibration and production MD
gmx grompp -f eq.mdp -c min12.gro -p topol.top -o eq.tpr -n index.ndx -maxwarn 3
gmx mdrun -v -deffnm eq -nt 10 -pin on -pinstride 1 -pinoffset 0 -gpu_id 0

gmx grompp -f md.mdp -c eq.gro -t eq.cpt -p topol.top -o md.tpr -maxwarn 3
gmx mdrun -v -deffnm md -nt 10 -pin on -pinstride 1 -pinoffset 0 -gpu_id 0

### Required MDP and ITP files are located in MDPS/ and ITPs/ directories
### The trajectories for all replicas are available on Zenodo: https://zenodo.org/records/15608685
