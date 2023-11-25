import http.client
import json

conn = http.client.HTTPSConnection("e1dgy3.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "destinations": [
                {
                    "to": "14168807375"
            "title": "This is sample subject"
        }
    ]
})
headers = {
    'Authorization': 'App 6b73fe625d87a5c18f90b039a8e95547-d0870171-eace-47f1-9ba0-16f18db2628e',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/mms/1/advanced", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))