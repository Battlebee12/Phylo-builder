from Bio import SeqIO
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
from .distance_matrix import compute_distance_matrix

def build_and_plot_tree(fasta_path):
    records = list(SeqIO.parse(fasta_path, "fasta"))
    labels = [rec.id for rec in records]
    sequences = [str(rec.seq) for rec in records]

    # Use helper function to compute distances
    dist_matrix = compute_distance_matrix(sequences)

    print("Distance matrix:")
    print(dist_matrix)

    # Convert to condensed form for linkage
    condensed = squareform(dist_matrix)
    linkage_matrix = linkage(condensed, method='average')  # UPGMA

    # Plot the tree
    plt.figure(figsize=(8, 5))
    dendrogram(linkage_matrix, labels=labels)
    plt.title("Phylogenetic Tree (UPGMA)")
    plt.xlabel("Sequence")
    plt.ylabel("Genetic Distance")
    plt.tight_layout()
    plt.savefig("output/tree_plot.png")
    plt.show()
