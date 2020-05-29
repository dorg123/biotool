import requests
import xml.etree.ElementTree as xml
import json
import ntplib
from datetime import datetime
from pytz import timezone
import biogate


def ncbi_query(util='search', **params):
    params['tool'] = biogate.__name__
    params['email'] = biogate.__email__
    return requests.get(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/e{util}.fcgi', params).content.decode().strip()


retmax = 100000
dbs = sorted(json.loads(ncbi_query('info', retmode='json'))['einforesult']['dblist'])


def search(term, db='pubmed'):
    if db not in dbs:
        raise ValueError(f'Database {db!r} is not a valid database id in NCBI\'s API.')
    history_server_response = ncbi_query('search', term=term, usehistory='y', retmode='json', retmax=0, db=db)
    history_server_response = json.loads(history_server_response)
    webenv = history_server_response['esearchresult']['webenv']
    query_key = history_server_response['esearchresult']['querykey']
    count = int(history_server_response['esearchresult']['count'])
    ids = []
    for retstart in range(0, count, retmax):
        response = ncbi_query('search', usehistory='y', retmode='json', webenv=webenv, query_key=query_key,
                              retmax=retmax, retstart=retstart, db=db)
        response_idlist = json.loads(response)['esearchresult']['idlist']
        ids.extend(response_idlist)
    return ids


def main():
    # print(dbs)
    # print(len(search('hemoglobin', db='protein')))
    # print(ncbi_query('fetch', db='protein', id=160797, rettype='fasta', retmode='text'))
    c = ntplib.NTPClient()
    response = c.request('time.google.com')
    print(datetime.utcfromtimestamp(response.tx_time))


if __name__ == '__main__':
    main()