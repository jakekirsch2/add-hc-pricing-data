import urllib.request
import json
import ssl


def parse_file(url):
    """Parse json file"""
    list_of_files = []
    data = list(download_file(url)["reporting_structure"])
    for plan in data:
        if "allowed_amount_file" not in plan:
            continue
        if plan["allowed_amount_file"]["location"] not in list_of_files:
            list_of_files.append(plan["allowed_amount_file"]["location"])
    list_of_files = list(set(list_of_files))
    return list_of_files

def download_file(url):
    """Download file from url"""
    with urllib.request.urlopen(url, context=ssl.SSLContext()) as response:
        data = json.loads(response.read())
    return data