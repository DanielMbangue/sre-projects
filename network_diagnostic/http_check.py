import requests
def check_http(url, timeout=5):
    try:
        response = requests.get(url,timeout=5)
        success = 200 <= response.status_code < 300
        elapsed_ms = response.elapsed.total_seconds() * 1000
        return(success,response.status_code,elapsed_ms)
    except requests.exceptions.RequestException:
        return(False, None,None)