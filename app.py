#curl -m 3610 -X POST https://add-hc-pricing-data-mnirkpcsna-uc.a.run.app/get-cigna -H "Authorization: bearer $(gcloud auth print-identity-token)" -H "Content-Type: application/json" -d '{"url": "https://d25kgz5rikkq4n.cloudfront.net/cost_transparency/mrf/table-of-contents/reporting_month=2023-11/2023-11-01_cigna-health-life-insurance-company_index.json?Expires=1702688709&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9kMjVrZ3o1cmlra3E0bi5jbG91ZGZyb250Lm5ldC9jb3N0X3RyYW5zcGFyZW5jeS9tcmYvdGFibGUtb2YtY29udGVudHMvcmVwb3J0aW5nX21vbnRoPTIwMjMtMTEvMjAyMy0xMS0wMV9jaWduYS1oZWFsdGgtbGlmZS1pbnN1cmFuY2UtY29tcGFueV9pbmRleC5qc29uIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzAyNjg4NzA5fX19XX0_&Signature=LNxqa5JiDXUbaVg6itmXp4dKHLtw7YCOT3kSgTJSjBK4ZJrOZUtPXYJKHHoAHq0NyZzKYXlD-XZJgXwmxeYXPDY8kQgh9P~RULCP8ugpffhasB2eHrDN0xXi6qQFYHXAJiKT0o04gCcs1CT1jg11JfeRKmv5cFxWXq4hoSJ~dqCwnMcE6fwFGZbSr88I8xBz0oJMOrvuXr2MHsaV2rNRsooqhtJwO-EfbNDK4NCMqy9xUD~Fv-s~c8e6w53MX2-2KS3oU~OvF5SZpNEE46LT4nsnlyCRJ1BA01JVDOvZgibzJXETLOVCge3PYScah-ddBLg4prLNQCbEj4ZNB~Kpwg__&Key-Pair-Id=K1NVBEPVH9LWJP"}'

from flask import Flask, request
import os
from cigna.parse_file import parse_file
import asyncio
app = Flask(__name__)

@app.route('/get-cigna', methods = ['POST'])
def get_cigna():
    message = request.get_json(force=True)
    url = message['url']
    if "concurrent_tasks" in message:
        concurrent_tasks = message["concurrent_tasks"]
    else:
        concurrent_tasks = 100
    data = parse_file(url)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = []
    #loop through data 100 at a time
    for i in range(0, len(data), concurrent_tasks):
        #download 100 files at a time
        for link in data[i:i+concurrent_tasks]:
            tasks.append(asyncio.ensure_future(download_data(link)))
        loop.run_until_complete(asyncio.wait(tasks))
        tasks = []        
    return "SUCCESS"
    #wget 
async def download_data(link):
    file_name = link.split("/")
    file_name = file_name[-3] + "/" + file_name[-2] + "/" + file_name[-1]
    file_name = file_name.split("?")[0]
    print(f"Downloading {file_name} from {link}")
    os.system(f" curl '{link}' | gsutil cp - gs://healthcare-raw-files/unacked/cigna/{file_name}")
    print(f"Downloaded {file_name} from {link}")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)