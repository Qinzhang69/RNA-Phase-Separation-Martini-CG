# RNA-Phase-Separation-Martini-CG

This repository contains the code and resources related to our research manuscript. Below is a structured overview of the repository contents and instructions for using the scripts.


## Repository Structure

```
RNA_Salt_Interaction_Analysis/
├── Case_build_system/              # Example system construction cases
│   └── 3xG4C2_12_17mMNacl_10mMMgcl2_30nm/  # Sample system building case
├── ITPs/                          # Force field include files (.itp)
├── MDPs/                          # GROMACS simulation parameter files (.mdp)
├── scripts/                       # Jupyter notebook analysis scripts
└── README.md                      # This file
```


### 1. Case_build_system/
Contains example directories demonstrating how to build RNA simulation systems. For example:
- `3xG4C2_12_17mMNacl_10mMMgcl2_30nm/`: Sample case for constructing a 12-strands of 3xG4C2 RNA system with 17mM NaCl, 10mM MgCl₂, and a 30nm simulation box. Open the Readme.txt file and follow the instructions to build the system step by step.


### 2. ITPs/
Holds all force field include files (.itp) required for simulations, including:
- Residue type definitions
- Ion parameter files
- Custom molecule descriptions


### 3. MDPs/
Contains GROMACS simulation parameter files (.mdp) for different simulation stages:
- `min.mdp`: Energy minimization parameters
- `eq.mdp`: Equilibration phase parameters
- `md.mdp`: Production run parameters


### 4. scripts/
Jupyter notebook scripts for data analysis and visualization, organized by manuscript figures:
- `Fig3b_figS4b_interchain_enrichment.ipynb`: Generates Figure 3b and Supplemental Figure S4b (inter-chain C-C/C-G/G-G contacts enrichment analysis)
- `FigS3a_figS5a_CC_CG_GG_intrachain_contacts.ipynb`: Generates Supplemental Figure S3a and S5a (intra-chain C-C/C-G/G-G contacts analysis)
- `FigS1d_PO4-Mg_contact.ipynb`: Generates Supplemental Figure S1d (Phosphate group - Magnesium ion contact analysis)
- `Fig2a_fig2b_Cluster_count.ipynb`:Generates Figure 2a and 2b (Average cluster count analysis) 
- ... (12 scripts total, named by their corresponding manuscript of Supplemental figures)


## How to Use the Scripts

### 1. Download Data
1. Obtain simulation data from Zenodo: [DOI: 10.5281/zenodo.15608685](https://zenodo.org/records/15608685)
2. Decompress the data to your local directory.

### 2. Environment Setup
#### Required Dependencies:
- Python 3.8+
- Jupyter Lab/Notebook
- MDAnalysis (`pip install mdanalysis`)
- Additional packages: `numpy`, `matplotlib`, `scipy`, `pickle`

#### Installation Steps:
1. Clone the repository:
```bash
git clone https://github.com/Qinzhang69/RNA-Phase-Separation-Martini-CG.git
cd RNA-Phase-Separation-Martini-CG/
```

2. Install missing packages (as needed):
```bash
pip install mdanalysis numpy matplotlib scipy
```


### 3. Run Analysis Scripts
1. Navigate to the scripts directory:
```bash
cd scripts/
```

2. Launch Jupyter Lab:
```bash
jupyter-lab
```

3. Open a notebook (e.g., `Fig1i_figS1b_SASA.ipynb`).
4. Run cells sequentially. If prompted, install missing packages:
```bash
pip install <package-name>
```


### 4. Configure Data Paths
- Update file paths in the scripts to match your decompressed Zenodo data directory.
- Ensure the script expects the data structure (e.g., `./media/qzhang04/...`).


## Citation
If you use this code or data, please cite our manuscript (manuscript in submission):
```
[A glimpse of RNA phase separation under the Martini lens]
```


## License
This project is licensed under the MIT License - see the `LICENSE` file for details.


## Contact
For questions or support, contact: `202111022406@std.uestc.edu.cn`