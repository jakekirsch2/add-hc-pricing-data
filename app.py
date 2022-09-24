#curl -m 3610 -X POST https://add-hc-pricing-data-gwmmhrzkra-uc.a.run.app -H "Authorization: bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" -d '{"company": "uhc", "file_url": "https://uhc-tic-mrf.azureedge.net/public-mrf/2022-09-01/2022-09-01_Bind-Benefits--Inc-_TPA_UNITEDHEALTHCARE-CHOICE-PLUS_UCQ_in-network-rates.json.gz", "file_name": "2022-09-01_Bind-Benefits--Inc-_TPA_UNITEDHEALTHCARE-CHOICE-PLUS_UCQ_in-network-rates.json.gz"}'
#curl -m 3610 -X POST http://10.65.0.5:8000 -H "Authorization: bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" -d '{"company": "uhc", "file_url": "https://uhc-tic-mrf.azureedge.net/public-mrf/2022-09-01/2022-09-01_Bind-Benefits--Inc-_TPA_UNITEDHEALTHCARE-CHOICE-PLUS_UCQ_in-network-rates.json.gz", "file_name": "2022-09-01_Bind-Benefits--Inc-_TPA_UNITEDHEALTHCARE-CHOICE-PLUS_UCQ_in-network-rates.json.gz"}'

import os

def main():
    return "Hello Jake"
    # message = request.get_json(force=True)
    # company = message['company']
    # file_url = message['file_url']
    # file_name = message['file_name']
    # os.system(f" curl '{file_url}' | gsutil cp - gs://data-platform-data/{company}/{file_name}")
    # return "SUCCESS"
    #wget 
    
