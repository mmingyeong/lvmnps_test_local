# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Mingyeong Yang (mingyeong@khu.ac.kr)
# @Date: 2021-07-05

#host: 163.180.145.123
#userid: admin
#passward: irlab
#scheme = 'http'
#base_url = '%s://%s' % (scheme, host)

import asyncio
import lvmpower as ps

async def main():
    
    #set paramters
    host = '163.180.145.123'
    userid = 'admin'
    password = 'irlab'
    
    tasks = []
    dli = ps.LVMPowerSwitch(hostname=host, userid=userid, password=password)
    await dli.add_client()
    #await dli.outlet()

    #await dli.onall()
    #await dli.on('Outlet 5')
    #await dli.offall()
    #await dli.off('Outlet 1')
    await dli.printstatus()
    await dli.close()

    #tasks.append(await dli.offall())
    #tasks.append(await dli.printstatus())
    #await asyncio.gather(*tasks)

asyncio.run(main())
