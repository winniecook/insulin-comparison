# Comparative Protein Sequence Analyzer

A versatile bioinformatics tool for comparative analysis of DNA sequences encoding related proteins. This tool fetches sequences from NCBI, calculates GC content distributions, identifies Open Reading Frames (ORFs), and generates publication-ready visualizations for comparative analysis.

## Features

### Core Analysis Capabilities
- **Sequence Retrieval**: Automatically fetches DNA sequences from NCBI using protein IDs
- **GC Content Analysis**: Calculates and visualizes GC content distribution along sequences using sliding window analysis
- **ORF Detection**: Identifies Open Reading Frames with customizable minimum length thresholds
- **Comparative Visualization**: Generates side-by-side comparisons of multiple protein sequences
- **Statistical Summary**: Provides comprehensive statistics for each analyzed sequence

### Output Visualizations
1. **GC Content Distribution Graph**: Smoothed line plots showing GC content variation across sequences
2. **ORF Location Map**: Visual representation of ORF positions and lengths across all sequences
3. **Summary Statistics**: Integrated data tables with sequence length, average GC content, and ORF counts

## Use Cases

This tool is particularly valuable for:
- **Comparative genomics studies** - analyzing related genes across species or gene families
- **Pathway analysis** - comparing genes within the same biological pathway
- **Evolutionary studies** - examining sequence conservation and divergence
- **Drug target research** - analyzing therapeutic target genes and related proteins
- **Cancer research** - comparing tumor suppressor genes or oncogenes
- **Metabolic studies** - analyzing enzymes in metabolic pathways

## Installation

### Prerequisites
- Python 3.7 or higher
- Required Python packages (see requirements.txt)

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/winniecook/comparative-protein-analyzer.git
   cd comparative-protein-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure NCBI access:
   - Open `dna-sequence-analyzer-6.py`
   - Replace `"your_email@example.com"` with your email address (required for NCBI E-utilities)

## Usage

### Basic Usage
```bash
python dna-sequence-analyzer-6.py
```

### Customizing Your Analysis

To analyze your own set of proteins, modify the `proteins` dictionary in the main function:

```python
proteins = {
    "GENE1": "NM_000001",  # Replace with your NCBI accession numbers
    "GENE2": "NM_000002",
    "GENE3": "NM_000003",
    # Add as many proteins as needed
}
```

### Example Protein Sets

**Insulin Signaling Pathway** (default):
```python
proteins = {
    "INS": "NM_000207",    # Insulin
    "IGF1": "NM_000618",   # Insulin-like Growth Factor 1
    "INSR": "NM_000208",   # Insulin Receptor
    "IGF1R": "NM_000875",  # IGF1 Receptor
    "IRS1": "NM_005544"    # Insulin Receptor Substrate 1
}
```

**Tumor Suppressor Genes**:
```python
proteins = {
    "TP53": "NM_000546",   # p53
    "RB1": "NM_000321",    # Retinoblastoma
    "BRCA1": "NM_007294",  # Breast Cancer 1
    "BRCA2": "NM_000059",  # Breast Cancer 2
    "APC": "NM_000038"     # Adenomatous Polyposis Coli
}
```

**Glycolysis Enzymes**:
```python
proteins = {
    "HK1": "NM_000188",    # Hexokinase 1
    "PFKM": "NM_000289",   # Phosphofructokinase
    "ALDOA": "NM_000034",  # Aldolase A
    "GAPDH": "NM_002046",  # Glyceraldehyde-3-phosphate dehydrogenase
    "PKM": "NM_002654"     # Pyruvate Kinase
}
```

## Output Files

The tool generates several output files:

### Sequence Files
- `{PROTEIN_NAME}.fasta` - Individual FASTA files for each protein

### Visualizations
- `comparative_gc_content.png` - GC content distribution comparison
- `comparative_orf_locations.png` - ORF location visualization

### Terminal Output
```
INS sequence length: 1430 bp
INS average GC content: 61.25%
INS number of ORFs: 3
---
IGF1 sequence length: 7562 bp
IGF1 average GC content: 56.78%
IGF1 number of ORFs: 12
---
```

## Customization Options

### Adjusting Analysis Parameters

You can modify several parameters in the code:

- **GC Content Window Size**: Change `window_size=100` in `calculate_gc_content()`
- **Minimum ORF Length**: Modify `min_length=100` in `find_orfs()`
- **Smoothing Window**: Adjust `np.ones(50)/50` in plotting functions
- **Figure Dimensions**: Modify `figsize` parameters in plotting functions

### Adding New Analysis Features

The modular structure makes it easy to add new analyses:
- Codon usage analysis
- Amino acid composition
- Secondary structure prediction
- Phylogenetic analysis

## Requirements

```
biopython>=1.79
numpy>=1.21.0
matplotlib>=3.5.0
requests>=2.25.0
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
```bash
git clone https://github.com/winniecook/comparative-protein-analyzer.git
cd comparative-protein-analyzer
pip install -r requirements.txt
# Make your changes
# Test your changes
# Submit a pull request
```

