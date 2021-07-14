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
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0', 
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    #get http response
    #modify auth 
    #try to test it (authentication)
    async with httpx.AsyncClient() as client:
        base = await client.get(url=base_url)
        #try to login
        login = await client.post(url=login_url,auth=auth, data=data, headers=headers)
        index = await client.get(url=full_url, auth=auth, headers=headers)
        #if login.status_code != 200:
        #    raise Exception('fail to login.')
        """
        full = await client.get(url=full_url)
        if full.status_code != 200:
            raise Exception('fail to access index.htm')
        """
        
        print(base)
        #print(base.text)
        print(login)
        #print(login.text)
        print(index)
        print(index.text)

asyncio.run(main())
