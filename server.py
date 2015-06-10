from flask import Flask, request, jsonify
import marisa_trie


app = Flask(__name__)


db = marisa_trie.BytesTrie()
db.load('data/regions.marisa')


REGION_MAPPINGS = {
    "E12000001": "North East",
    "E12000002": "North West",
    "E12000003": "Yorkshire and The Humber",
    "E12000004": "East Midlands",
    "E12000005": "West Midlands",
    "E12000006": "East of England",
    "E12000007": "London",
    "E12000008": "South East",
    "E12000009": "South West"
}


@app.route('/')
def lookup():
    if 'postcode' not in request.args:
        return jsonify(detail="Please supply a 'postcode' parameter"), 400

    try:
        postcode = request.args['postcode'].replace(' ', '').upper()
        region_code = db[postcode][0].decode("utf-8")
        region = REGION_MAPPINGS[region_code]
        return jsonify(postcode=postcode, region_code=region_code, region=region)
    except:
        return jsonify(detail="Failed to lookup postcode"), 400


if __name__ == "__main__":
    app.run(debug=True)
