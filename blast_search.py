import time
from tqdm import tqdm
from Bio.Blast import NCBIWWW, NCBIXML

cache = {}  # Store BLAST results using query_id as key

def get_blast_result(query_id, AAsequence):
    try:
        if query_id in cache:
            return cache[query_id]
        else:
            # Display connecting message
            print("Connecting to NCBI...")
            
            # Query search
            print("Querying NCBI database...")
            
            blast_result = NCBIWWW.qblast("blastp", "swissprot", AAsequence)
            
            # Store the result in the cache
            cache[query_id] = blast_result
            
            # Display research message
            print("Processing BLAST results...")
            
            # Simulate research progress (can be replaced with actual checking of BLAST status)
            for _ in tqdm(range(5), desc="Progress"):
                time.sleep(2)  # Simulate processing time
            
            # Display completion message
            print("BLAST search completed successfully.")
            
            # Return query_id and blast_record
            return blast_result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
query_id = "KAF8065798.1"
AAsequence = "maaggrsaallallwlgcslmlllpparaarapgelssqlllssgmhllsdqsslapegllglsaaqraspllanpatrsvfaadsalartatardeawrrggdaaagrpaaagggraarrrgrgrsaalrggfdldvsatlaalqsisycanlsdvaawnctrcaripn"

blast_result = get_blast_result(query_id, AAsequence)

if blast_result:
    # Parse the BLAST result
    blast_record = NCBIXML.read(blast_result)
    
    # Print out the hits or any relevant information
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            print("****Alignment****")
            print("sequence:", alignment.title)
            print("length:", alignment.length)
            print("e value:", hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)
