from chain import (create_tokenizer, create_llm, 
                    create_chain, extract_triplets, 
                    refactor_triplets)
from pathlib import Path
from text_reader import read_files, write_triplets, load_json_triplets
from triplet_messages import triplet_messages
from refactor_messages import refactor_messages
import json
import sys

PAPERS_PATH = (Path(__file__).parent).joinpath("papers/")
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

def main():
    """
    Entrypoint
    """

    # Create tokenizer, llm and 2 chains based on them
    tokenizer = create_tokenizer(MODEL_NAME)
    llm = create_llm(MODEL_NAME, tokenizer, 0, 0.9, 0.1)
    triplet_chain = create_chain(triplet_messages, llm, tokenizer)
    refactor_chain = create_chain(refactor_messages, llm, tokenizer)

    # Read all files
    print("Loading files...")
    files = read_files(PAPERS_PATH)
    print("Files loaded!")

    # List of JSON objects. One per file
    all_triplets = []

    # Extract triplets from each file
    for i, file in enumerate(files):
        raw_triplets = extract_triplets(triplet_chain, file)
        ref_triplets = refactor_triplets(refactor_chain, raw_triplets)
        json_triplets = load_json_triplets(ref_triplets)
        all_triplets.append(json_triplets)

    print("Triplets extracted!")
    print("Writing triplets into files...")
    # Write triplets in corresponding files
    write_triplets(PAPERS_PATH, all_triplets)
    print("Triplets written into files!")

if __name__ == "__main__":
    main()
