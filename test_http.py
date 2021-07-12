import httpx

r = httpx.get('http://163.180.145.123')

print(r)
#<Response [200 OK]>
print(r.status_code)
#200
print(r.headers['content-type'])
#'text/html; charset=UTF-8'
print(r.text)
#'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
