import requests
import json
from bs4 import BeautifulSoup

def crawler():
  r = requests.get('https://www.e-ms.com.tw/information/Man/man.html#99')
  r.encoding = 'utf-8' # 改編碼
  response = r.text

  res_soup = BeautifulSoup( response, "html.parser" )

  #print( res_soup.body.table ) 

  outcome = {}
  data = res_soup.find_all('table')

  final = []
  # print(data)
  for d in data[4:]:
    raw_data = d.find_all('tr')
    #print( raw_data, len( raw_data ) )
    for td in raw_data[1:] :
      #symptom = td.find_all('td')[0]

      subject = td.find_all('td')[1].get_text().split('、')
      symptom = td.find_all('td')[0].get_text().split('、')
    
      #print( type( symptom ) )
      for i in range( len(symptom)) :
        outcome[symptom[i].strip()] = subject
  return outcome
  

# print( dict )

# path = 'data.txt'
# f = open( path, 'w' )
# json.dump( dict, f, ensure_ascii=False )
# f.close


