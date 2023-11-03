import requests
import json
import os

def login(email,password):
    # 设置请求头
    headers = {
        'Host': 'volkno.herokuapp.com',
        'Connection': 'keep-alive',
        'Content-Length': '68',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="8"',
        'Accept': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.5162 SLBChan/105',
        'Content-Type': 'application/json',
        'Origin': 'https://volkno.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://volkno.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    # 设置请求参数
    data = {
        "app": "volkno",
        "email": email,
        "password": password
    }

    # 将请求参数转换为JSON格式
    data_json = json.dumps(data)

    # 发送POST请求
    url = 'https://volkno.herokuapp.com/account/login'
    response = requests.post(url, headers=headers, data=data_json)

    # 检查响应
    if response.status_code == 200:
        response_data = response.json()
        token = response_data.get('token', '')
        if token:
            return token
        else:
            print("未找到Token")
            return ""
    else:
        print("请求失败")
        print(f"响应状态码: {response.status_code}")
        print(response.text)  # 错误信息
        return ""

def getAll(token,VolknoAudience):
    # 设置请求头
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'volkno.herokuapp.com',
        'Origin': 'https://volkno.com',
        'Referer': 'https://volkno.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
        'VolknoAudience': VolknoAudience,
        'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    # 发送POST请求
    url = 'https://volkno.herokuapp.com/media/list/ALL?'
    response = requests.get(url, headers=headers)

    # 检查响应
    if response.status_code == 200:
        response_data = response.json()
        return response_data
    else:
        print("请求失败")
        print(f"响应状态码: {response.status_code}")
        print(response.text)  # 错误信息
        return ""

def process_json(token,json_data,VolknoAudience):
    for media_id, media_info in json_data.get('data', {}).items():
        item_list = media_info.get('items', {}).get('list', [])
        if item_list:
            media_item_id = item_list[0]
            poster_id = media_info.get('poster_id')
            send_post_request(token, media_id, media_item_id, poster_id,VolknoAudience)

def send_post_request(token,media_id, media_item_id, poster_id,VolknoAudience):
    post_data1 = {
        "media_id": media_id,
        "media_item_id": media_item_id,
        "poster_id": poster_id,
        "page_path": f"/media/{media_id} media_item_id {media_item_id}/{media_item_id}",
        "device": "desktop",
        "device_orientation": "landscape",
        "results": [
            {
                "code": "SUMMARY",
                "challenge_key": "overall-rating",
                "challenge_value": {"rating": 10},
                "media_time_secs": 0,
                "page_location": "video_summary"
            }
        ]
    }
    post_data2 = {
        "media_id": media_id,
        "media_item_id": media_item_id,
        "poster_id": poster_id,
        "page_path": f"/media/{media_id} media_item_id {media_item_id}/{media_item_id}",
        "device": "desktop",
        "device_orientation": "landscape",
        "results": [
            {
                "code": "SUMMARY",
                "challenge_key": "comment",
                "challenge_value": {"comment": "As of my last update in January 2022, I don't have specific information about a film titled Extraction II. If it's a movie released after this date or under a different title, I might not have details about it.However, if it's a sequel to the film Extraction starring Chris Hemsworth, it's expected to maintain the high standard of action and cinematography set by its predecessor. Extraction was praised for its intense action sequences and impressive long-take fight scenes. If Extraction II follows suit, it might be anticipated to continue the trend of engaging and elaborate action choreography, along with remarkable cinematography that captures the intensity of the action sequences.Please note that any specific analysis or reviews would require access to the film or its details, which might not be available in my current dataset."},
                "media_time_secs": 0,
                "page_location": "video_summary"
            }
        ]
    }
    post_data3 = {
        "media_id": media_id,
        "media_item_id": media_item_id,
        "poster_id": poster_id,
        "page_path": f"/media/{media_id} media_item_id {media_item_id}/{media_item_id}",
        "device": "desktop",
        "device_orientation": "landscape",
        "results": [
            {
                "code": "SUMMARY",
                "challenge_key": "tagit",
                "challenge_value": ["Love It", "Awesome", "Funny"],
                "media_time_secs": 0,
                "page_location": "video_summary"
            }
        ]
    }
    post_data4 = {
        "media_id": media_id,
        "media_item_id": media_item_id,
        "poster_id": poster_id,
        "page_path": f"/media/{media_id} media_item_id {media_item_id}/{media_item_id}",
        "device": "desktop",
        "device_orientation": "landscape",
        "results": [
            {
                "code": "SUMMARY",
                "challenge_key": "interestdrivers",
                "challenge_value": {"interests": ["Comedy"],"comment": ""},
                "media_time_secs": 0,
                "page_location": "video_summary"
            }
        ]
    }
    post_data5 = {
        "media_id": media_id,
        "media_item_id": media_item_id,
        "poster_id": poster_id,
        "page_path": f"/media/{media_id} media_item_id {media_item_id}/{media_item_id}",
        "device": "desktop",
        "device_orientation": "landscape",
        "results": [
            {
                "code": "SUMMARY",
                "challenge_key": "demandit",
                "challenge_value": {"platforms": ["Theatre"],"rating": 5},
                "media_time_secs": 0,
                "page_location": "video_summary"
            }
        ]
    }
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': token,
        'Connection': 'keep-alive',
        'Conent-Length': '284',
        'Content-Type': 'application/json',
        'Host': 'volkno.herokuapp.com',
        'Origin': 'https://volkno.com',
        'Prefer': 'safe',
        'Referer': 'https://volkno.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
        'VolknoAudience': VolknoAudience,
        'secch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    url = "https://volkno.herokuapp.com/results"
    response1 = requests.post(url, headers=headers, data=json.dumps(post_data1))
    response2 = requests.post(url, headers=headers, data=json.dumps(post_data2))
    response3 = requests.post(url, headers=headers, data=json.dumps(post_data3))
    response4 = requests.post(url, headers=headers, data=json.dumps(post_data4))
    response5 = requests.post(url, headers=headers, data=json.dumps(post_data5))
    if response1.status_code == 200:
        print(f"1.成功提交数据 for media_id {media_id} media_item_id {media_item_id} 返回数据{response1.text}")
        if response2.status_code == 200:
            print(f"2.成功提交数据 for media_id {media_id} media_item_id {media_item_id} 返回数据{response2.text}")
            if response3.status_code == 200:
                print(f"3.成功提交数据 for media_id {media_id} media_item_id {media_item_id} 返回数据{response3.text}")
                if response4.status_code == 200:
                    print(f"4.成功提交数据 for media_id {media_id} media_item_id {media_item_id} 返回数据{response4.text}")
                    if response5.status_code == 200:
                        print(f"5.成功提交数据 for media_id {media_id} media_item_id {media_item_id} 返回数据{response5.text}")
                    else:
                        print(f"5.提交失败 for media_id {media_id} media_item_id {media_item_id} 返回数据{response5.text}")
                else:
                    print(f"4.提交失败 for media_id {media_id} media_item_id {media_item_id} 返回数据{response4.text}")
            else:
                print(f"3.提交失败 for media_id {media_id} media_item_id {media_item_id} 返回数据{response3.text}")
        else:
            print(f"2.提交失败 for media_id {media_id} media_item_id {media_item_id} 返回数据{response2.text}")
    else:
        print(f"1.提交失败 for media_id {media_id} media_item_id {media_item_id} 返回数据{response1.text}")

def getVolknoAudience(token):
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': token,
        'Connection': 'keep-alive',
        'Conent-Type': 'application/json',
        'Host': 'volkno.herokuapp.com',
        'If-None-Match': 'W/"2027-Dz/cWYOa2qwse7+wvvc5C6cS6fo"',
        'Origin': 'https://volkno.com',
        'Referer': 'https://volkno.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
        'VolknoAudience': '',
        'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    url = 'https://volkno.herokuapp.com/bootstrap'
    response = requests.get(url, headers=headers)

    # 检查响应
    if response.status_code == 200:
        response_data = response.json()
        # 获取 "list" 中的第一个值
        first_list_value = response_data["audiences"]["list"][0]
        # 获取 "hash" 值
        hash_value = response_data["audiences"]["data"][str(first_list_value)]["hash"]
        return hash_value
    else:
        print("请求失败")
        print(f"响应状态码: {response.status_code}")
        print(response.text)  # 错误信息
        v = input("请手动输入VolknoAudience：")
        return v


#打包pyinstaller -i C:\Users\q3133\PycharmProjects\volknohttp\icon.ico --uac-admin -F main.py
if __name__ == '__main__':
    # # 获取桌面路径
    # desktop_path = os.path.expanduser("~/Desktop")
    # # 拼接文件路径
    # file_path = os.path.join(desktop_path, "users.txt")
    # # 打开文件并逐行读取内容
    # try:
    #     with open(file_path, 'r') as file:
    #         for line in file:
    #             # 分割每行的内容，以"----"为分隔符
    #             parts = line.strip().split("----")
    #             if len(parts) == 2:
    #                 email, password = parts
    #                 print(f"账号: {email}, 密码: {password}")
    #                 token = 'Bearer ' + login(email, password)
    #                 print("Token:", token)
    #                 VolknoAudience = getVolknoAudience(token)
    #                 print("VolknoAudience：", VolknoAudience)
    #                 all = getAll(token, VolknoAudience)
    #                 process_json(token, all, VolknoAudience)
    # except FileNotFoundError:
    #     print(f"文件 {file_path} 未找到")
    # except Exception as e:
    #     print(f"发生异常: {str(e)}")
    user_input = input("请输入账号：")
    pass_input = input("请输入密码：")
    token = 'Bearer ' + login(user_input,pass_input)
    print("Token:", token)
    VolknoAudience = getVolknoAudience(token)
    print("VolknoAudience：",VolknoAudience)
    all = getAll(token,VolknoAudience)
    process_json(token,all,VolknoAudience)

