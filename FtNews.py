import requests as rq
from bs4 import BeautifulSoup
import pandas as pd


Newsurl= 'https://www.ft.com/stream/7e37c19e-8fa3-439f-a870-b33f0520bcc0'
Newsheader={ 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "if-none-match": "W/\"36703-2WbtVcM11dQPZPVj+8wCfOoMDuk\"",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "_ga=GA1.1.2004618750.1733296233; spoor-id=cm49jtqao000035796vu2qdf2; permutive-id=5cdb42bf-f33b-47f1-97f2-16465742cdd8; _ga_2DSMN2JH8F=GS1.1.1733296233.1.0.1733296240.0.0.0; FTAllocation=f65aa494-eeaf-4c21-b942-f2517de7dba1; FTClientSessionId=b5dcdf1e-a397-40da-9a9d-a7eb8a29eff2; o-typography-fonts-loaded=1; __exponea_etc__=9acdf954-c7fd-4d40-85a5-d98331090b20; usnatUUID=d4cb2bd1-07f5-46f7-a2b7-3ecfa2d785e8; __exponea_time2__=-0.8374736309051514; consentUUID=2065dd8e-6e17-4f87-a935-3dfe6c0d37b7_38; consentDate=2024-12-09T06:30:17.936Z; FTConsent=marketingBypost%3Aoff%2CmarketingByemail%3Aoff%2CmarketingByphonecall%3Aoff%2CmarketingByfax%3Aoff%2CmarketingBysms%3Aoff%2CenhancementBypost%3Aoff%2CenhancementByemail%3Aoff%2CenhancementByphonecall%3Aoff%2CenhancementByfax%3Aoff%2CenhancementBysms%3Aoff%2CbehaviouraladsOnsite%3Aoff%2CdemographicadsOnsite%3Aon%2CrecommendedcontentOnsite%3Aon%2CprogrammaticadsOnsite%3Aon%2CcookiesUseraccept%3Aoff%2CcookiesOnsite%3Aoff%2CmembergetmemberByemail%3Aoff%2CpermutiveadsOnsite%3Aoff%2CpersonalisedmarketingOnsite%3Aon; FTCookieConsentGDPR=true"
  }
NewsResq=rq.get(url=Newsurl, headers= Newsheader) 

Newssoup= BeautifulSoup(NewsResq.content,'html.parser')

allnews= Newssoup.select('div[class="o-teaser-collection o-teaser-collection--stream"]>ul>li')

ALLNEWS=[]
for i in allnews:
    dates= i.select_one('div[class="stream-card__date"]> time')
    if dates:
        DATE= dates.attrs['datetime']
    mainheading= i.select_one('div[class="o-teaser__meta"]>a')
    if mainheading:
        MAINHEADING= mainheading.text
    heading=i.select_one('div[class="o-teaser__heading"]>a')
    if heading:
        HEADING=heading.text
    content= i.select_one('p[class="o-teaser__standfirst"]>a')
    if content:
        CONTENT=content.text
    img= i.select_one('div[class="o-teaser__image-placeholder"]>img')
    if img:
       IMAGE={
        'Src': img.attrs['data-src'],
        'Alt': img.attrs['alt']
        }
    NEWSDATA={
        'Date': DATE,
        'Highlights': MAINHEADING,
        'Heading':HEADING ,
        'Smallheading': CONTENT,
        'Image': IMAGE
    }
    ALLNEWS.append(NEWSDATA)


Pd=pd.DataFrame(ALLNEWS)
Pd.to_csv('News.csv')