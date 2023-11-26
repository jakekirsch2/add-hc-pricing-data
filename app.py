#curl -m 3610 -X POST https://add-hc-pricing-data-gwmmhrzkra-uc.a.run.app -H "Authorization: bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" -d '{"company": "uhc", "file_url": "https://uhc-tic-mrf.azureedge.net/public-mrf/2022-09-01/2022-09-01_Bind-Benefits--Inc-_TPA_UNITEDHEALTHCARE-CHOICE-PLUS_UCQ_in-network-rates.json.gz", "file_name": "2022-09-01_Bind-Benefits--Inc-_TPA_UNITEDHEALTHCARE-CHOICE-PLUS_UCQ_in-network-rates.json.gz"}'

from flask import Flask, request
import os
from cigna import parse_file
app = Flask(__name__)

@app.route('/get-cigna', methods = ['POST'])
def get_cigna():
    message = request.get_json(force=True)
    url = message['url']
    data = parse_file(url)
    for link in data:
        file_name = link.split('/')[-1]
        print(f"Downloading {file_name} from {link}")
        os.system(f" curl '{link}' | gsutil cp - gs://data-platform-data/unacked/{file_name}")
    return "SUCCESS"
    #wget 
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)