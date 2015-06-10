import sys
import csv
import marisa_trie


def rebuild(filename):

    print("Rebuilding trie based on CSV file: %s" % filename)

    buffer = {}

    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for line in csvreader:
            postcode = line[0].strip()
            region = line[1].strip().encode('utf-8')  # values should be byte
            buffer[postcode] = region

    trie = marisa_trie.BytesTrie(buffer.items())
    trie.save('data/regions.marisa')
    print("Done")


if __name__ == "__main__":
    filename = sys.argv[1]
    rebuild(filename)
