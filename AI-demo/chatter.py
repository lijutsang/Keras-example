import json
import urllib.request

api_url = "http://openapi.tuling123.com/openapi/api/v2"
while True:
    text_input = input('我：')
    if(str(text_input) == 'q'):
        break
    req = {
    "perception":
    {
        "inputText":
        {
            "text": text_input
        },

        "selfInfo":
        {
            "location":
            {
                "city": "深圳",
                "province": "广东",
                "street": "龙岗"
            }
        }
    },

    "userInfo": 
    {
        "apiKey": "9cec86d1079f41988ba16ae82132acdc",
        "userId": "OnlyUseAlphabet"
    }
    }
# print(req)
# 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
# print(req)

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(response_str)
    response_dic = json.loads(response_str)
    # print(response_dic)

    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    print('机器人的回答：')
    print('code：' + str(intent_code))
    print('text：' + results_text)

