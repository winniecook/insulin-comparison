# insulin-comparison
Comparative analysis tool for insulin-related proteins. Fetches sequences, calculates GC content, identifies ORFs, and generates visualizations for INS, IGF1, INSR, IGF1R, and IRS1. Ideal for bioinformatics research in diabetes and cancer studies.
# Insulin-related Protein Analyser

This project provides a comprehensive analysis of GC content and Open Reading Frame (ORF) distributions for key proteins in the insulin signaling pathway. It fetches sequences from NCBI, calculates GC content, identifies ORFs, and generates comparative visualizations.

## Features

- Retrieves sequences for INS, IGF1, INSR, IGF1R, and IRS1 from NCBI
- Calculates GC content distribution along each sequence
- Identifies Open Reading Frames (ORFs) in each sequence
- Generates two comparative visualizations:
  1. GC content distribution across all proteins
  2. ORF locations for all proteins
- Provides summary statistics for each protein

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/winniecook/insulin-comparison.git
   cd insulin-comparison
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open the `comparative_protein_analyzer.py` file and replace `"your_email@example.com"` with your actual email address (required for NCBI E-utilities).

2. Run the script:
   ```
   python comparative_protein_analyzer.py
   ```

3. The script will generate two PNG files:
   - `comparative_gc_content.png`: Shows GC content distribution
   - `comparative_orf_locations.png`: Displays ORF locations

## Output

The script provides both terminal output and visual representations:

1. Terminal output includes:
   - Sequence length
   - Average GC content
   - Number of ORFs for each protein

2. Generated graphs:
   - GC content distribution graph
   - ORF location visualization

Both graphs include summary statistics for quick reference.

