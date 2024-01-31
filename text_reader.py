from pathlib import Path
import json

def read_files(path):
    """
    Reads contents of all .txt files in the directory.

    Args:
        path (str): Path to the directory with text files

    Returns:
        List of strings. Each string is contents of one file
    """

    # Texts of all files
    texts = []
    directory = Path(path)
    # Sort files based on their names
    for file_path in sorted(directory.rglob("paper_*.txt")):
        # Text of single file
        text = ""
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                text += line
        texts.append(text)

    return texts

def load_json_triplets(ref_triplets):
    """
    Converts a single string of triplets into a list of JSON objects.

    Args:
        ref_triplets (str): A large string containing all triplets from the file
    Returns:
        List of JSON objects. Each object represents one triplet from the file
    """
    json_triplets = []
    if "No triplets" not in ref_triplets:
        # Load string into a JSON object
        try:
            parsed_json = json.loads(ref_triplets)
            for triplet in parsed_json:
                json_triplets.append(triplet)
        except:
            raise Exception("LLM output is not a valid JSON!")
    return json_triplets


def write_triplets(path, triplets):
    """
    Writes all triplets in files with according names.

    Args:
        path (str): Path to the directory with text files
        triplets (list): List of JSON objects. One per file
    """
    directory = Path(path)
    count = 0
    for file_path in sorted(directory.rglob("paper_*.txt")):
        file_number = file_path.stem.split("_")[1]
        content_path = path / f"{file_number}" / f"content_{file_number}.txt"

        # Each triplet corresponds to the current file
        with open(content_path, "w") as file:
            file.write(json.dumps(triplets[count], indent=4))
        count += 1

