import asyncio
import httpx

async def main():
    #set paramters
    host = '163.180.145.123'
    user = 'admin'
    password = 'irlab'
    scheme = 'http'
    base_url = '%s://%s' % (scheme, host)
    url = 'index.com'
    full_url = "%s/%s" % (base_url, url)
    auth = httpx.DigestAuth(user, password)

    #login
    login_url = '%s/login.tgi' % base_url
    data = {
    'Username': user,
    'Password': password
    }
    headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded'}

    #get http response
    async with httpx.AsyncClient(auth=auth) as client:
        base = await client.get(url=base_url)
        #try to login
        login = await client.post(url=login_url, data=data, headers=headers)
        #if login.status_code != 200:
        #    raise Exception('fail to login.')
        """
        full = await client.get(url=full_url)
        if full.status_code != 200:
            raise Exception('fail to access index.htm')
        """
        
        print(base)
        print(base.text)
        print(login)
    #print(login.text)

asyncio.run(main())
