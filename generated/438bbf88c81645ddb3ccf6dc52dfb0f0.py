
import argparse

def search(query: str, data: list[str]) -> list[str]:
    """
    Searches for a query string within a list of strings and returns a list of matching elements.

    :param query: The string to search for.
    :param data: The list of strings to search within.
    :return: A list of strings that match the query.
    """
    return [item for item in data if query.lower() in item.lower()]

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Search through a list of items.")
    parser.add_argument("query", type=str, help="The string to search for.")
    parser.add_argument("data_file", type=argparse.FileType('r'), help="File containing data to search through, one item per line.")

    args = parser.parse_args()

    # Read the data from the file
    with args.data_file as file:
        data = [line.strip() for line in file]

    # Perform the search
    results = search(args.query, data)

    # Print the results
    if results:
        print("Matches found:")
        for result in results:
            print(result)
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()
