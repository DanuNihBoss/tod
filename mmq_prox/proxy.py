

import requests, os, shutil
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor

try: shutil.rmtree(
    'get_proxy/__pycache__'
  )
except: pass

proxy_list = []
valid_proxy = []

def prox():
  print('''
\033[94m[1]\033[0m Auto Get the proxy \033[93mHTTP/HTTPS\033[0m
\033[94m[2]\033[0m Auto Get the proxy \033[95mSSL\033[0m
\033[94m[3]\033[0m Chose File
  ''')
  ask = int(
    input(
      '\033[94m[?]\033[0m Chose : '
    )
  )
  if ask == 1:
    return proxy_net(
    )
  elif ask == 2:
    return proxy_ssl(
    )
  elif ask == 3:
    return from_file(
    )
  else:
    exit(
      '\n\033[94m[!]\033[0m \033[91mNummber not found [Go to the hell bro]!\033[0m'
    )

def proxy_checker(prox):
  try:
    global valid_proxy
    if requests.get(
       'http://ip.ml.youngjoygame.com:30220/myip',
          verify=False,
          proxies=prox,
          timeout=10
        ).status_code == 200:
      valid_proxy.append(
        prox
      )
    print(
      end='\r\033[94m[+]\033[0m Searching \033[92m(%s)\033[0m proxy valid.'%(
        len(
          valid_proxy
        )
      ),
      flush=True
    )
  except: pass

def proxy_net():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://free-proxy-list.net/',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip()
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
def proxy_ssl():
  print(
    '\033[94m[+]\033[0m Searching Proxy'
  )
  r = requests.get(
    'https://www.sslproxies.org/',
    headers={'user-agent':'chrome'}
  ).text
  soup = bs(
    r,
    'html.parser'
  )
  proxs = soup.find(
    'textarea'
  ).text.split(
    '\n'
  )
  [
    proxy_list.append({
      'http':'http://'+e.strip(),
      'https':'https://'+e.strip(),
    }) if len(
      e.strip(
      ).split(
        ':'
      )
    ) == 2 else None for e in proxs
  ]
  if len(
    proxy_list
  ) != 0:
    with ThreadPoolExecutor(
      max_workers=50
      ) as thread:
      [
        thread.submit(
          proxy_checker,(
            prox
          )
        ) for prox in proxy_list
      ]
    if len(
      valid_proxy
    ) != 0:
      print(
        '\n'
      )
      return valid_proxy
    else: exit(
      '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again\033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found\033[0m'
  )
def from_file():
  print(
    '\n\033[94m[!]\033[0m Delim Proxy (ip:port)'
  )
  list = input(
    '\033[94m[+]\033[0m List proxy \033[93m(ex: proxy.txt) : \033[0m'
  )
  if os.path.exists(
    list
  ):
    for data in open(
      list,
      'r',
      encoding='utf-8'
    ).readlines(
      ):
      prox = data.strip(
      ).split(
        ':'
      )
      try:
        if prox[0] and prox[1]:
          proxy_list.append({
            'http': 'http://'+data.strip(),
            'https': 'https://'+data.strip(),
          })
      except: pass
    if len(
      proxy_list
    ) != 0:
      print(
        '\033[94m[+]\033[0m Total \033[92m(%s)\033[0m proxy' %(
          str(
            len(
              proxy_list
            )
          )
        )
      )
      print(
        '\033[94m[+]\033[0m Searching Proxy'
      )
      with ThreadPoolExecutor(
        max_workers=500
      ) as thread:
        [
          thread.submit(
            proxy_checker,(
              prox
            )
          ) for prox in proxy_list
        ]
      if len(
        valid_proxy
      ) != 0:
        print(
          '\n'
        )
        return valid_proxy
      else: exit(
        '\033[94m[+]\033[0m \033[91mSorry, Proxy Not Found\033[0m . \033[93mTry Again \033[0m'
      )
    else: exit(
      '\033[94m[!]\033[0m \033[91mSorry, Proxy Not Found \033[0m'
    )
  else: exit(
    '\033[94m[!]\033[0m File Not Found "{0}"'.format(
      list
    )
  )
