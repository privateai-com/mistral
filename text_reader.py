from pathlib import Path
import json

PAPERS_PATH = (Path(__file__).parent).joinpath("papers/")

# Read contents of all .txt files in the directory. Return array of contents of each file.
# @param path Path to directory with papers files
def read_files(path):
    # Texts of all files
    texts = []
    directory = Path(path)
    # Sort files based on their names
    for file_path in sorted(directory.rglob('paper_*.txt')):
        # Text of single file
        text = ""
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                text += line
        texts.append(text)

    return texts


# Write all triplets in files with according names
# @param path Path to directory with papers files
# @param triplets List of JSON objects. One per file
def write_triplets(path, triplets):
    directory = Path(path)
    count = 0
    for file_path in sorted(directory.rglob('paper_*.txt')):
        file_number = file_path.stem.split('_')[1]
        content_path = path / f"{file_number}" / f"content_{file_number}.txt"

        # Each triplet corresponds to the current file
        with open(content_path, 'w') as file:
            file.write(json.dumps(triplets[count], indent=4))
        count += 1
