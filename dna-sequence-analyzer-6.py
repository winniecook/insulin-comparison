# comparative_protein_analyzer.py

import numpy as np
import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio import Entrez
from Bio.SeqUtils import gc_fraction
import requests
import re

# Set your email for Entrez
Entrez.email = "your_email@example.com"  # Replace with your email

def retrieve_sequence(protein_id, filename):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id={protein_id}&rettype=fasta&retmode=text"
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "w") as f:
            f.write(response.text)
        print(f"Sequence for {protein_id} retrieved and saved as {filename}")
    else:
        print(f"Failed to retrieve sequence for {protein_id}. Status code: {response.status_code}")
        exit(1)

def read_fasta(file_path):
    return list(SeqIO.parse(file_path, "fasta"))[0]

def calculate_gc_content(sequence, window_size=100):
    gc_contents = []
    for i in range(0, len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        gc_contents.append(gc_fraction(window) * 100)
    return gc_contents

def find_orfs(sequence, min_length=100):
    orfs = []
    for frame in range(3):
        for match in re.finditer(r'(?=(ATG(?:...)*?(?:TAA|TAG|TGA)))', str(sequence[frame:])):
            if len(match.group(1)) >= min_length:
                start = match.start() + frame
                end = start + len(match.group(1))
                orfs.append((start, end))
    return orfs

def plot_gc_content_comparison(gc_contents_dict, protein_info):
    plt.figure(figsize=(14, 8))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    for (name, gc_contents), color in zip(gc_contents_dict.items(), colors):
        smoothed_gc = np.convolve(gc_contents, np.ones(50)/50, mode='valid')
        plt.plot(smoothed_gc, label=name, color=color, linewidth=2)
    
    plt.xlabel("Position in Sequence (per 100 bp window)", fontsize=12)
    plt.ylabel("GC Content (%)", fontsize=12)
    plt.title("Comparative GC Content Analysis of Insulin-related Proteins", fontsize=14)
    plt.legend(fontsize=10, loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add text box with protein information
    info_text = "\n".join([f"{name}: {info['length']} bp, GC: {info['gc']:.2f}%, ORFs: {info['orfs']}" 
                           for name, info in protein_info.items()])
    plt.text(0.02, 0.02, info_text, transform=plt.gca().transAxes, fontsize=9,
             verticalalignment='bottom', bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig("comparative_gc_content.png", dpi=300)
    plt.close()

def plot_orf_locations(orf_dict, protein_info):
    plt.figure(figsize=(14, 10))
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    y_positions = np.arange(len(orf_dict)) * 0.5
    
    for (name, orfs), y_pos, color in zip(orf_dict.items(), y_positions, colors):
        for start, end in orfs:
            plt.plot([start, end], [y_pos, y_pos], color=color, linewidth=6)
        plt.text(-500, y_pos, name, fontsize=10, va='center', ha='right')
    
    plt.xlabel("Position in Sequence (bp)", fontsize=12)
    plt.yticks([])
    plt.title("ORF Locations in Insulin-related Proteins", fontsize=14)
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)
    
    # Add text box with protein information
    info_text = "\n".join([f"{name}: {info['length']} bp, GC: {info['gc']:.2f}%, ORFs: {info['orfs']}" 
                           for name, info in protein_info.items()])
    plt.text(0.02, 0.02, info_text, transform=plt.gca().transAxes, fontsize=9,
             verticalalignment='bottom', bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig("comparative_orf_locations.png", dpi=300)
    plt.close()

def main():
    proteins = {
        "INS": "NM_000207",
        "IGF1": "NM_000618",
        "INSR": "NM_000208",
        "IGF1R": "NM_000875",
        "IRS1": "NM_005544"
    }
    
    gc_contents_dict = {}
    orf_dict = {}
    protein_info = {}
    
    for name, protein_id in proteins.items():
        filename = f"{name}.fasta"
        retrieve_sequence(protein_id, filename)
        sequence = read_fasta(filename)
        gc_contents = calculate_gc_content(sequence.seq)
        orfs = find_orfs(sequence.seq)
        
        gc_contents_dict[name] = gc_contents
        orf_dict[name] = orfs
        protein_info[name] = {
            'length': len(sequence),
            'gc': np.mean(gc_contents),
            'orfs': len(orfs)
        }
        
        print(f"{name} sequence length: {len(sequence)} bp")
        print(f"{name} average GC content: {np.mean(gc_contents):.2f}%")
        print(f"{name} number of ORFs: {len(orfs)}")
        print("---")
    
    plot_gc_content_comparison(gc_contents_dict, protein_info)
    plot_orf_locations(orf_dict, protein_info)

if __name__ == "__main__":
    main()
