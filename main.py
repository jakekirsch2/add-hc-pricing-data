#curl -m 3610 -X POST https://add-hc-pricing-data-gwmmhrzkra-uc.a.run.app -H "Authorization: bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" -d '{"company": "uhc", "file_url": "https://uhc-tic-mrf.azureedge.net/public-mrf/2022-09-01/2022-09-01_Bind-Benefits--Inc-_TPA_UNITEDHEALTHCARE-CHOICE-PLUS_UCQ_in-network-rates.json.gz", "file_name": "2022-09-01_Bind-Benefits--Inc-_TPA_UNITEDHEALTHCARE-CHOICE-PLUS_UCQ_in-network-rates.json.gz"}'
#curl -m 3610 -X POST  http://35.225.117.112:80 -H "Authorization: bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" -d '{"company": "uhc", "file_url": "https://uhc-tic-mrf.azureedge.net/public-mrf/2022-09-01/2022-09-01_Bind-Benefits--Inc-_TPA_UNITEDHEALTHCARE-CHOICE-PLUS_UCQ_in-network-rates.json.gz", "file_name": "2022-09-01_Bind-Benefits--Inc-_TPA_UNITEDHEALTHCARE-CHOICE-PLUS_UCQ_in-network-rates.json.gz"}'
#curl -X POST  http://35.225.117.112:80 -H "Authorization: bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" -d '{"company": "testing", "file_url": "https://gbfs.citibikenyc.com/gbfs/en/station_information.json", "file_name": "station_information.json"}'


import os
import argparse

def main(args):
    company = args.company
    file_url = args.file_url
    file_name = args.file_name
    try:
        os.system("gcloud auth list")
        os.system(f"curl '{file_url}' | gsutil cp - gs://data-platform-data/{company}/{file_name}")
        return "Success"
    except Exception as e:
        raise e
    #wget 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", help="Company name")
    parser.add_argument("--file_url", help="File url")
    parser.add_argument("--file_name", help="File name")
    args = parser.parse_args()
    main(args)