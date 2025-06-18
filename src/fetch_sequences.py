from Bio import Entrez, SeqIO

Entrez.email = "sarab4space@gmail.com"  # replace with your actual email

def fetch_sequences_from_ncbi(ids, output_fasta_path):
    """
    Fetches sequences from NCBI using a list of GenBank IDs and saves them to a FASTA file.
    """
    print(f"Fetching {len(ids)} sequences from NCBI...")
    with Entrez.efetch(db="nucleotide", id=ids, rettype="fasta", retmode="text") as handle:
        records = list(SeqIO.parse(handle, "fasta"))
        SeqIO.write(records, output_fasta_path, "fasta")
    print(f"Saved to {output_fasta_path}")
