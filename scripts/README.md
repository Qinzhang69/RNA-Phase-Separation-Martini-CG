## `scripts/` Directory
Jupyter notebook scripts for data analysis and visualization, organized by manuscript figures:

| Notebook File | Generates | Analysis Description |
|---------------|-----------|----------------------|
| `Fig3b_figS4b_interchain_enrichment.ipynb` | Figure 3b & S4b | Inter-chain C-C/C-G/G-G contacts enrichment |
| `FigS3a_figS5a_CC_CG_GG_intrachain_contacts.ipynb` | Figure S3a & S5a | Intra-chain C-C/C-G/G-G contacts |
| `FigS1d_PO4-Mg_contact.ipynb` | Figure S1d | Phosphate group - Magnesium ion contacts |
| `Fig2a_fig2b_Cluster_count.ipynb` | Figure 2a & 2b | Average cluster count analysis |
| ... (12 notebooks total) | | |

---

## Workflow Instructions

### 1. Obtain Simulation Data
1. Download datasets from Zenodo: (https://zenodo.org/records/15608685)
2. Decompress the archive to your preferred directory.

### 2. Environment Configuration
#### Required Packages:
- Python ≥ 3.8
- Jupyter Lab/Notebook
- MDAnalysis
- NumPy
- Matplotlib
- SciPy

#### 3. Setup:
```bash
# Clone repository
git clone https://github.com/Qinzhang69/RNA-Phase-Separation-Martini-CG.git
cd RNA-Phase-Separation-Martini-CG/

# Install dependencies
pip install mdanalysis numpy matplotlib scipy
```

#### 4. Execute Analysis Notebooks
cd scripts/
jupyter-lab  # or jupyter-notebook

  1. Open the desired notebook

  2. Run cells sequentially using Kernel > Restart & Run All

  3. Install any additional missing packages when prompted:

     pip install missing-package-name

  4. Configure Data Paths
  
  Critical Step: Update path variables in each notebook to match your local data directory.
  Example modification (typically near notebook start):
    # BEFORE
    traj_path = "/media/qzhang04/3xG4C2/zenodo/A_3xG4C2_800uM_12_Na_neutral/lake_10us/"
    
    # AFTER (update to your path)
    traj_path = "/your/local/path/zenodo/A_3xG4C2_800uM_12_Na_neutral/lake_10us/"

