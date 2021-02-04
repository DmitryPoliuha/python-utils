import requests
from requests.utils import quote, unquote, urlparse, urlunparse
from urllib.parse import parse_qsl, urlencode

# Change json query param of request
parsed_url = list(urlparse(request.url))
query_params = dict(parse_qsl(parsed_url[4]))
data_param = json.loads(query_params["data"])
data_param["page"] += 1
query_params["data"] = json.dumps(data_param, separators=(',', ':'))
query_string = urlencode(query_params)
parsed_url[4] = query_string
url = urlunparse(parsed_url)
response = requests.request(request.method, url, headers=request.headers)
