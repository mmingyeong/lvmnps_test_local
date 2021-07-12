import asyncio
import httpx

async def main():
    #set paramters
    host = '163.180.145.123'
    user = 'admin'
    password = 'irlab'
    scheme = 'http'
    base_url = '%s://%s' % (scheme, host)
    #auth = httpx.DigestAuth(user, password)

    #get http response
    async with httpx.AsyncClient(base_url=base_url) as client:
        response = await client.get(url=base_url)
        print(response)

        #check basic header information
    #    header = response.request.headers
    #    encoding = response.encoding
    #    text = response.text
    #    print(header)
    #    print(encoding)
    #    print(text)

        #check .json
        #await response.json()
        #json = await response.json()
        #print(json)

    #dli = DLI()
    #dli.add_client(host, user, password)
    #json = await dli.get_outlet_state(host, 1)
    #print(json)

asyncio.run(main())

class DLI(object):
    def __init__(self):
        self.clients = {}

    def add_client(self, host: str, user: str, password: str):
        """Adds a client."""

        auth = httpx.DigestAuth(user, password)
        self.clients[host] = httpx.AsyncClient(
            auth=auth,
            base_url=f"http://{host}/restapi",
            headers={},
        )

    async def get_outlet_state(self, host: str, outlet: int) -> bool:
        """Gets the value of the outlet (1-indexed)."""

        outlet -= 1

        if host not in self.clients:
            raise ValueError(f"Client for host {host} not defined.")

        
        r = await self.clients[host].get(f"relay/outlets/{outlet}/state/")
        if r.status_code != 200:
            raise RuntimeError(f"GET returned code {r.status_code}.")

        await self.clients[host].aclose()

        return r.json()

asyncio.run(main())


http://163.180.145.123/outlet?1=OFF
http://163.180.145.123/outlet?3=OFF
http://163.180.145.123/outlet?1=CCL

http://163.180.145.123/outlet?5=OFF
http://163.180.145.123/outlet?5=ON

http://163.180.145.123/outlet?a=OFF
http://163.180.145.123/outlet?a=ON
http://163.180.145.123/outlet?a=CCL


    async def __len__(self):
        """
        :return: Number of outlets on the switch
        """
        if self.__len == 0:
            self.__len = len(await self.statuslist())
        return self.__len

    async def determine_outlet(self, outlet=None):
        """ Get the correct outlet number from the outlet passed in, this
            allows specifying the outlet by the name and making sure the
            returned outlet is an int
        """
        outlets = await self.statuslist()
        if outlet and outlets and isinstance(outlet, str):
            for plug in outlets:
                plug_name = plug[1]
                if plug_name and plug_name.strip() == outlet.strip():
                    return int(plug[0])
        try:
            outlet_int = int(outlet)
            len_int = await self.__len__()
            if outlet_int <= 0 or outlet_int > len_int:
                raise PowerException('Outlet number %d out of range' % outlet_int)
            return outlet_int
        except ValueError:
            raise PowerException('Outlet name \'%s\' unknown' % outlet)
    
    async def status(self, outlet=1):
        """
        Return the status of an outlet, returned value will be one of:
        ON, OFF, Unknown
        """
        outlet = self.determine_outlet(outlet)
        outlets = await self.statuslist()
        if outlets and outlet:
            for plug in outlets:
                if plug[0] == outlet:
                    return plug[2]
        return 'Unknown'

    async def statuslist(self):
        """ Return the status of all outlets in a list,
        each item will contain 3 items plugnumber, hostname and state  """
        outlets = []
        url = await self.geturl('index.htm')
        if not url:
            return None
        soup = BeautifulSoup(url, "html.parser")
        # Get the root of the table containing the port status info
        try:
            root = soup.findAll('td', text='1')[0].parent.parent.parent
        except IndexError:
            # Finding the root of the table with the outlet info failed
            # try again assuming we're seeing the table for a user
            # account insteaed of the admin account (tables are different)
            try:
                self._is_admin = False
                root = soup.findAll('th', text='#')[0].parent.parent.parent
            except IndexError:
                return None
        for temp in root.findAll('tr'):
            columns = temp.findAll('td')
            if len(columns) == 5:
                plugnumber = columns[0].string
                hostname = columns[1].string
                state = columns[2].find('font').string.upper()
                outlets.append([int(plugnumber), hostname, state])
        if self.__len == 0:
            self.__len = len(outlets)
        return outlets