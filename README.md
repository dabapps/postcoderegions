# Postcode Regions
JSON API to find regions for UK postcodes.

A call like: `http://127.0.0.1:8000/?postcode=bn11ag` will return:

    {
      "postcode": "BN11AG",
      "region": "South East",
      "region_code": "E12000008",
      "borough": "",  # London Borough e.g. Camden
    }

## Requirements

- Python 3.2 (or pyenv)

## Installation

    ./build

## Running the server

To run the server in development mode

    env/bin/python server.py

## Building data

The repository includes the region database encoded using marisa-trie.

New data can be downloaded by visiting [http://geoportal.statistics.gov.uk/](http://geoportal.statistics.gov.uk/) and searching for the most up-to-date version of `ONS Postcode Directory`.

The downloaded Zip will contain large csv file (ONSPD_MAY_2015_UK.csv). This should be edited into the following format (postcode, ONS Region):

    | "AB10AA" | "S99999999" |
    | "AB10AB" | "S99999999" |
    | "AB10AD" | "S99999999" |

The can be achieved by cutting the file using bash:
    
    cut -d "," -f1,16 ONSPD_NOV_2016_UK.csv > new-data-filename.csv

You can then rebuild the trie database file by calling

    env/bin/python build_trie.py path/new-data-filename.csv

In order to build the borough dataset a further build is required which involves 2 steps:

   - Download borough csv files from https://www.ordnancesurvey.co.uk/business-and-government/products/code-point-open.html
   - Run .borough_csv_processor.sh from within the directory which contains the csv files. Thsi will output a sigle boroughs.csv file
   - Run  env/bin/python build_borough_trie.py ./boroughs.csv to build the optmized dataset.
   
