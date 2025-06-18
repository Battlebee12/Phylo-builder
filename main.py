from src.tree_builder import build_and_plot_tree
from src.fetch_sequences import fetch_sequences_from_ncbi

if __name__ == "__main__":
    genbank_ids = [
        "L26328.1",
        "L26327.1",
        "AY360331.1",
        "JX473574.1"  # You can swap or verify this
    ]

    output_fasta = "data/ncbi_sequences.fasta"
    fetch_sequences_from_ncbi(genbank_ids, output_fasta)

    build_and_plot_tree(output_fasta)
