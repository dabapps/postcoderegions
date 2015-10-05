import sys
import csv
import marisa_trie


def rebuild(filename):

    print("Rebuilding trie based on borough CSV file: %s" % filename)

    borough_data = {}

    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for line in csvreader:
            postcode = line[0].strip()
            borough_code = line[1].strip().encode('utf-8')  # values should be byte
            borough_data[postcode] = borough_code

    trie = marisa_trie.BytesTrie(borough_data.items())
    trie.save('data/boroughs.marisa')
    print("Done")


if __name__ == "__main__":
    filename = sys.argv[1]
    rebuild(filename)
