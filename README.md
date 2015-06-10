# postcoderegions
JSON API to find regions for UK postcodes

## Installation

    ./build

### Running the server

To run the server in development mode

    env/bin/python server.py

## Building data

The repository includes the region database encoded using marisa-trie.

New data can be downloaded from visiting `https://geoportal.statistics.gov.uk/geoportal/catalog/main/home.page` and searching for the most up-to-date version of `ONS Postcode Directory`.

The downloaded Zip will contain large csv file (ONSPD_MAY_2015_UK.csv). This should be edited into the following format (postcode, ONS Region):

    | "AB10AA" | "S99999999" |
    | "AB10AB" | "S99999999" |
    | "AB10AD" | "S99999999" |

You can then rebuild the data trie file by calling

    env/bin/python build_trie.py new-data-filename.csv