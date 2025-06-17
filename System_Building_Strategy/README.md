# RNA System Construction Protocol

## Repository Structure
```
System_Building_Strategy/
├── 3xG4C2_12_17mMNacl_10mMMgcl2_30nm/              # Step-by-step construction example
│── TPRs_3xG4C2_system/                             # Production-ready .tpr files for all 3xG4C2 system
```

## Case Study: 3xG4C2 RNA System
- `3xG4C2_12_17mMNacl_10mMMgcl2_30nm/`:  
  Step-by-step guide for building 12-strand 3xG4C2 system with:
  - 17mM NaCl, 10mM MgCl₂  
  - 30nm simulation box

```bash
# 1. Initial System Preparation (All salt conditions)
gmx editconf -f 3xG4C2.pdb -box 15 10 15 -center 7.5 5 7.5 -o 3xG4C2_151015.gro
gmx solvate -cp 3xG4C2_151015.gro -cs water.gro -o 3xG4C2_solv.gro -p topol.top

# 2. Salt Addition (Condition-specific)
./17NaCl_10MgCl2.py

# 3. Energy Minimization
gmx grompp -f ../MDPs/min.mdp -c ion_2.gro -p topol.top -o min.tpr -maxwarn 3
gmx mdrun -v -deffnm min -nt 4

# 4. System Replication (12-strand construct)
gmx genconf -f min.gro -o min_12.gro -dist 0 0 0 -nbox 2 3 2
# Remember to update topol.top for 12 molecules!

# 5. Re-minimization
gmx grompp -f ../MDPs/min.mdp -c min_12.gro -p topol.top -o min12.tpr -maxwarn 3
gmx mdrun -v -deffnm min12

# 6. Equilibration & Production
gmx make_ndx -f min12.gro # Create W_ION group
gmx grompp -f ../MDPs/eq.mdp -c min12.gro -p topol.top -o eq.tpr -n index.ndx -maxwarn 3
gmx mdrun -v -deffnm eq -nt 10 -pin on -pinstride 1 -pinoffset 0 -gpu_id 0

gmx grompp -f ../MDPs/md.mdp -c eq.gro -t eq.cpt -p topol.top -o md.tpr -maxwarn 3
gmx mdrun -v -deffnm md -nt 10 -pin on -pinstride 1 -pinoffset 0 -gpu_id 0

    Note: This protocol has been applied to:

        5xG4C2 systems (12-strands)

        8xG4C2 systems (12-strands)

        Salt concentrations: 0-696mM NaCl / 0-417mM MgCl₂
```

### Production Systems
Pre-built Simulation Inputs

All production-ready systems are available in TPRs_3xG4C2_system/:

| File Name | RNA Strands | Box Size (nm) | NaCl concentration (mM)| MgCl₂ concentration (mM) |
|---------------|-----------|----------------------|-----------|----------------------|
| `A_3xG4C2_800uM_12_Na_neutral.tpr` | 12 | 30 x 30 x 30 | 0 | 0 |
| `A_3xG4C2_800uM_12_17mMNaCl_10mMMgCl2.tpr` | 12 | 30 x 30 x 30 | 17 | 10 |
| ... (12 tprs total) | | |

---

> The revelant trajectories for all replicas are available on [Zenodo](https://zenodo.org/records/15608685)


