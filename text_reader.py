from pathlib import Path


# Read contents of all .txt files in the directory. Return array of contents of each file.
def read_files(path):
    # Texts of all files
    texts = []
    directory = Path(path)
    # Sort files based on their names
    for file_path in sorted(directory.glob('*.txt')):
        # Text of single file
        text = ""
        if file_path.suffix == ".txt":
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    text += line
        texts.append(text)

    return texts


PAPERS_PATH = (Path(__file__).parent).joinpath("papers/")


def main():
    texts = read_files(PAPERS_PATH)
    for text in texts:
        print("\n\n" + text)

if __name__ == "__main__":
    main()

