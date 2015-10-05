from flask import Flask, request, jsonify
import marisa_trie


app = Flask(__name__)


db = marisa_trie.BytesTrie()
db.load('data/regions.marisa')

borough_db = marisa_trie.BytesTrie()
borough_db.load('data/boroughs.marisa')


LONDON = 'London'


REGION_MAPPINGS = {
    "E12000001": "North East",
    "E12000002": "North West",
    "E12000003": "Yorkshire and The Humber",
    "E12000004": "East Midlands",
    "E12000005": "West Midlands",
    "E12000006": "East of England",
    "E12000007": LONDON,
    "E12000008": "South East",
    "E12000009": "South West",
    "W99999999": "Wales",
    "S99999999": "Scotland"
}


BOROUGH_MAPPINGS = {
    'E09000001': 'City of London',
    'E09000002': 'Barking and Dagenham',
    'E09000003': 'Barnet',
    'E09000004': 'Bexley',
    'E09000005': 'Brent',
    'E09000006': 'Bromley',
    'E09000007': 'Camden',
    'E09000008': 'Croydon',
    'E09000009': 'Ealing',
    'E09000010': 'Enfield',
    'E09000011': 'Greenwich',
    'E09000012': 'Hackney',
    'E09000013': 'Hammersmith and Fulham',
    'E09000014': 'Haringey',
    'E09000015': 'Harrow',
    'E09000016': 'Havering',
    'E09000017': 'Hillingdon',
    'E09000018': 'Hounslow',
    'E09000019': 'Islington',
    'E09000020': 'Kensington and Chelsea',
    'E09000021': 'Kingston upon Thames',
    'E09000022': 'Lambeth',
    'E09000023': 'Lewisham',
    'E09000024': 'Merton',
    'E09000025': 'Newham',
    'E09000026': 'Redbridge',
    'E09000027': 'Richmond upon Thames',
    'E09000028': 'Southwark',
    'E09000029': 'Sutton',
    'E09000030': 'Tower Hamlets',
    'E09000031': 'Waltham Forest',
    'E09000032': 'Wandsworth',
    'E09000033': 'City of Westminster',
}


@app.route('/')
def lookup():
    if 'postcode' not in request.args:
        return jsonify(detail="Please supply a 'postcode' parameter"), 400

    try:
        postcode = request.args['postcode'].replace(' ', '').upper()
        region_code = db[postcode][0].decode("utf-8")
        region = REGION_MAPPINGS[region_code]

        borough = ''
        if region == LONDON:
            borough_code = borough_db[postcode][0].decode("utf-8")
            borough = BOROUGH_MAPPINGS.get(borough_code, '')

        return jsonify(postcode=postcode, region_code=region_code, region=region, borough=borough)
    except:
        return jsonify(detail="Failed to lookup postcode"), 400


if __name__ == "__main__":
    app.run(debug=True)
