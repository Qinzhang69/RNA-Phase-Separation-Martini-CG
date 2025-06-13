# RNA Phase Separation - Martini Coarse-Grained Simulations

This repository contains simulation protocols and analysis scripts for the study *"A glimpse of RNA phase separation under the Martini lens"*. All data follows FAIR principles (Findable, Accessible, Interoperable, Reusable).

## Repository Structure
RNA-Phase-Separation-Martini-CG/
├── System_Building_Strategy/              # Initial system construction protocols
│   └── 3xG4C2_12_17mMNacl_10mMMgcl2_30nm/  # Sample system building case
|   └── TPRs_3xG4C2_system/                 # All tpr files for all 3xG4C2 salt conditions
├── ITPs/                          # Force field parameter files (.itp)
├── MDPs/                          # GROMACS simulation parameter files (.mdp)
├── scripts/                       # Analysis pipelines (Jupyter/Python)
├── LICENSE                        # MIT License
└── README.md                      # Project overview


> **Detailed folder contents** are documented in each subfolder's README.md

## Citation
If using this work, please cite our upcoming manuscript:

```bibtex
@Article{RNAPhaseSep2025,
  title = {A glimpse of RNA phase separation under the Martini lens},
  author = {Zhang, Qin and Souza, Paulo Telles and {Collaborators}},
  journal = {J. Phys. Chem. Lett.},
  year = {2023},
  doi = {manuscript in submission}
}


License

Distributed under the MIT License.
For academic use, attribution is appreciated via citation above.

Contact

 Corresponding Authors: Paulo Telles de Souza: paulo.telles_de_souza@ens-lyon.fr

 Qin Zhang: 202111022406@std.uestc.edu.cn