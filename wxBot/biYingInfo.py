import http.client
import re
import sys
def getPicInfo():
    httpClient = None
    html_text=""
    #print("####################http request start#####################")     
    try:
        httpClient =  http.client.HTTPConnection('cn.bing.com', 80, timeout=500)
        httpClient.request("GET", "/",None,{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                                            "Accept-Language":"h-CN,zh;q=0.8",
                                            "Content-Type":"text/xml"
                                            }) 
        response = httpClient.getresponse()
        #print(response.status,":",response.reason)
        #print(response.read())
        html_text=response.read()
        html_text=html_text.decode("utf-8")#玛德制杖还要解码，
    except Exception as e:
        print(e)
        sys.exit(0)
    finally:
        if httpClient:
            httpClient.close()
    #print("####################http response ok#####################")     

    try:
        IID= re.findall("<div id=\"lap_w\" data-ajaxiid=\"(.*)\" data-date=\"",html_text)[0]
        IG= re.findall("IG:\"(.*)\",EventID:",html_text)[0]
        #print("IID:",IID,"IG:",IG)
    except Exception as e:
        print(e)

    #print("####################get result#####################")     
    finalResult=""
    try:
        httpClient =  http.client.HTTPConnection('cn.bing.com', 80, timeout=500)
        httpClient.request("GET", "/cnhp/life?IID=SERP."+IID+"&IG="+"IG")
     
        response = httpClient.getresponse()
        html_text=response.read()
        html_text=html_text.decode("utf-8")
        finalResult= re.findall("<div id=\"hplaSnippet\">(.*)</div><div class=\"hplaPvd\"",html_text)[0]
    except Exception as e:
        print(e)
        sys.exit(0)
    print(finalResult)
    return finalResult
