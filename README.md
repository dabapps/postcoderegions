# Postcode Regions
JSON API to find regions for UK postcodes.

A call like: `http://127.0.0.1:5000/?postcode=bn11ag` will return:

    {
      "postcode": "BN11AG",
      "region": "South East",
      "region_code": "E12000008"
    }


## Installation

    ./build

### Running the server

To run the server in development mode

    env/bin/python server.py

## Building data

The repository includes the region database encoded using marisa-trie.

New data can be downloaded by visiting [https://geoportal.statistics.gov.uk/geoportal/catalog/main/home.page](https://geoportal.statistics.gov.uk/geoportal/catalog/main/home.page) and searching for the most up-to-date version of `ONS Postcode Directory`.

The downloaded Zip will contain large csv file (ONSPD_MAY_2015_UK.csv). This should be edited into the following format (postcode, ONS Region):

    | "AB10AA" | "S99999999" |
    | "AB10AB" | "S99999999" |
    | "AB10AD" | "S99999999" |

You can then rebuild the trie database file by calling

    env/bin/python build_trie.py path/new-data-filename.csv