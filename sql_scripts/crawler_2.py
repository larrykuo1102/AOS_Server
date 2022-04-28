import requests
from bs4 import BeautifulSoup
import re

def crawler():
    r = requests.get("https://www.vghtc.gov.tw/Module/SearchBySymptom?WebMenuID=5EACAD3A-F4B5-4E48-A8A2-FC48A28856C7").text
    soup = BeautifulSoup(r, "html.parser")
    soupp = soup.find_all("table", class_="px640up", width="100%")

    res={}
    for i in soupp: # i=table, ii=td1
        for ii in i.find_all("td" ,width="20%"):
            symp = re.split("[^\u4e00-\u9fa5]+", ii.find_next_siblings()[-1].string)
            try:
                symp.remove('')
                symp.remove('')
            except:
                pass
            for iii in ii:
                if iii not in res:
                    res[iii.string] = symp
                else:
                    res[iii.string] = list(set(res[iii.string]).union(set(symp)))
            try:
                for iii in (ii.find_next_sibling().string).split("、"):
                    if iii not in res:
                        res[iii] = symp
                    else:
                        res[iii] = list(set(res[iii]).union(set(symp)))
            except:
                pass
    for i in res:
        res["".join(re.findall('[\u4e00-\u9fa5]+', i))] = res.pop(i)
    return res
