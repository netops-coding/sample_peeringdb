#! /usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen, HTTPError
from json import loads
import sys

def get_peeringdb(pdp_type, pdp_id):
    pdb_url = 'https://beta.peeringdb.com/api/%s/%s'% (pdp_type, pdp_id)

    try :
        result_json = urlopen(pdb_url).read()
        result_dict = loads(result_json)
    except HTTPError, err:
        if err.code == 404:
            return None
    return result_dict


if __name__ == '__main__' :
    as_num = sys.argv[1]

    # get company and AS information 
    as_info_dict = get_peeringdb('asn', as_num)
    company_name = as_info_dict["data"][0]["org"]["name"]
    company_website = as_info_dict["data"][0]["website"]

    print as_num
    print company_name
    print company_website

    print '='*30
    
    # get IX information
    for netixlan_set in as_info_dict["data"][0]["netixlan_set"]:
        ixlan_id = netixlan_set["ixlan_id"]
        ipaddr4 = netixlan_set["ipaddr4"]
        ipaddr6 = netixlan_set["ipaddr6"]
        
        ixlan_info_dict = get_peeringdb('ixlan', ixlan_id)
        ix_name =  ixlan_info_dict["data"][0]["ix"]["org"]["name"]

        print ix_name
        print ipaddr4
        print ipaddr6
        print '='*30
