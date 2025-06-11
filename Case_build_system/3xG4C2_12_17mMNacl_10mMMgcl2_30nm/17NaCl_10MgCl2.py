#!/usr/bin/env python

import MDAnalysis as md
import subprocess

                     ### Concentration in Molar
nacl_CONCENTRATION = 0.017
mgcl_CONCENTRATION = 0.010

### neutralize
subprocess.call(f"gmx grompp -f min.mdp -c 3xG4C2_solv.gro -p topol.top -o ion.tpr -maxwarn 3"
 , shell=True)
p = subprocess.Popen(f'gmx genion -s ion.tpr -o ion.gro -p topol.top -pname NA -pq +1 -nname CL -nq -1 -neutral'
, stdin=subprocess.PIPE, shell=True, universal_newlines=True)
p.communicate('W')
p.wait()

### Calculate NaCL and MgCl number of atoms
u = md.Universe('ion.gro')
Waternumber = len(u.select_atoms('resname W').residues)  # total number of waters in the box after neutralization

nacl_num = int((nacl_CONCENTRATION * Waternumber * 4) / 55.5)
mgcl_num = int((mgcl_CONCENTRATION * Waternumber * 4) / 55.5)

### Add NaCl
subprocess.call(f"gmx grompp -f min.mdp -c ion.gro -p topol.top -o ion_1.tpr -maxwarn 3"
 , shell=True)
p = subprocess.Popen(f'gmx genion -s ion_1.tpr -o ion_1.gro -p topol.top -pname NA -pq +1 -nname CL -nq -1 -np {nacl_num} -nn {nacl_num}'
, stdin=subprocess.PIPE, shell=True, universal_newlines=True)
p.communicate('W')
p.wait()

### Add MGCl
subprocess.call(f"gmx grompp -f min.mdp -c ion_1.gro -p topol.top -o ion_2.tpr -maxwarn 3"
 , shell=True)
p = subprocess.Popen(f'gmx genion -s ion_2.tpr -o ion_2.gro -p topol.top -pname MG -pq +2 -nname CL -nq -1 -np {mgcl_num} -nn {mgcl_num*2}'
, stdin=subprocess.PIPE, shell=True, universal_newlines=True)
p.communicate('W')
p.wait()
