import requests
import json


class DWFIO:
    # 关于请求信息的参数配置
    # url = "http://i-yopiw3lm.cloud.nelbds.org.cn:8180"
    # username = "admin"
    # passwd = "Dwf2021!"
    '''
    获取账户token
    url: 链接
    username: 用户名
    passwd: 密码
    '''

    def __init__(self, url, username, passwd):
        self.url = url
        self.username = username
        self.passwd = passwd

    def get_token(self):
        full_url = self.url + "/api/app//dwf/v1/app/login?password=" + self.passwd + "&userName=" + self.username
        payload = {}
        headers = {
            'accept': '*/*',
            'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYzNTQxODc0Nn0.U2XWsEsnuU39_cXN4Wfb5mdWlWTKxvhhVaASOHABIVSWckhcTfo4yPri3Z0MAxOFza22NYYIF01_ngt_SKMGfw'
        }
        response = requests.request("GET", full_url, headers=headers, data=payload)
        res_code = json.loads(response.text)["code"]

        if res_code != 200:
            print("get_token() error: ")
            print(json.loads(response.text))
            return -1
        else:
            return json.loads(response.text)["data"]

    '''
    通过类名称（classname）和条件（condition）查询关联类的对象
    '''

    def query_relations_by_condition(self, classname, condition):
        full_url = self.url + "/api/app//dwf/v1/omf/relations/" + classname + "/objects"

        payload = json.dumps({
            "condition": condition
        })
        token = self.get_token()
        headers = {
            'accept': '*/*',
            'Authorization': token,
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=CFD3B3E7D77946060783845AD59ACF5A'
        }
        response = requests.request("POST", full_url, headers=headers, data=payload)
        res = json.loads(response.text)
        if ("code" not in res.keys()) or res["code"] != 200:
            print("query_relations_by_condition() error: ")
            print(response.text)
            return -1
        else:
            # 返回list, 其中的每一个元素都是一个字典类型的对象
            return res["data"]

    def create_obj(self, classname, obj):
        full_url = self.url + "/api/app//dwf/v1/omf/entities/" + classname + "/objects-create"
        payload = json.dumps([
            obj
        ])
        token = self.get_token()
        headers = {
            'accept': '*/*',
            'Authorization': token,
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=CFD3B3E7D77946060783845AD59ACF5A'
        }

        response = requests.request("POST", full_url, headers=headers, data=payload)
        res = json.loads(response.text)
        if ("code" not in res.keys()) or res["code"] != 200:
            print("create_relations() error: ")
            print(response.text)
            return -1
        else:
            # 新建成功
            return res["data"]

    '''
    创建关联类
    '''

    def create_relations(self, classname, obj):
        full_url = self.url + "/api/app//dwf/v1/omf/relations/" + classname + "/objects-create"
        '''
        {
            "leftOid": "3237F985D415A04685A0E573DF588DC5",
            "rightOid": "3B07F010E21F7F4DBF9CB2F406463940"
        }
        '''
        payload = json.dumps([
            obj
        ])
        token = self.get_token()
        headers = {
            'accept': '*/*',
            'Authorization': token,
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=CFD3B3E7D77946060783845AD59ACF5A'
        }

        response = requests.request("POST", full_url, headers=headers, data=payload)
        res = json.loads(response.text)
        if ("code" not in res.keys()) or res["code"] != 200:
            print("create_relations() error: ")
            print(response.text)
            return -1
        else:
            # 新建成功
            return 1

    def edit_obj(self, classname, obj):
        full_url = self.url + "/api/app//dwf/v1/omf/entities/" + classname + "/objects-update?forceUpdate=false"
        payload = json.dumps([
            obj
        ])
        token = self.get_token()
        headers = {
            'accept': '*/*',
            'Authorization': token,
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=CFD3B3E7D77946060783845AD59ACF5A'
        }
        response = requests.request("POST", full_url, headers=headers, data=payload)
        res = json.loads(response.text)
        if ("code" not in res.keys()) or res["code"] != 200:
            print("create_relations() error: ")
            print(response.text)
            return -1
        else:
            # 新建成功
            return 1

    '''
    通过oid删除关联类
    '''

    def delete_relations_by_oid(self, classname, oid):
        full_url = self.url + "/api/app//dwf/v1/omf/relations/" + classname + "/objects-delete"

        payload = json.dumps([
            oid
        ])
        token = self.get_token()
        headers = {
            'accept': '*/*',
            'Authorization': token,
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=CFD3B3E7D77946060783845AD59ACF5A'
        }
        response = requests.request("POST", full_url, headers=headers, data=payload)
        res = json.loads(response.text)
        if ("code" not in res.keys()) or res["code"] != 200:
            print("create_relations() error: ")
            print(response.text)
            return -1
        else:
            # 新建成功
            return 1

    def query_objects_by_condition(self, classname, condition):
        full_url = self.url + "/api/app//dwf/v1/omf/entities/" + classname + "/objects"

        payload = json.dumps({
            "condition": condition
        })
        token = self.get_token()
        headers = {
            'accept': '*/*',
            'Authorization': token,
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=CFD3B3E7D77946060783845AD59ACF5A'
        }
        response = requests.request("POST", full_url, headers=headers, data=payload)
        res = json.loads(response.text)
        if ("code" not in res.keys()) or res["code"] != 200:
            print("query_objects_by_condition() error: ")
            print(response.text)
            return -1
        else:
            # 新建成功
            return res['data']

    '''
    通过oid查询实体类
    '''

    def query_objects_by_oid(self, classname, oid, condition):
        full_url = self.url + "/api/app//dwf/v1/omf/entities/" + classname + "/objects/" + oid
        payload = json.dumps(condition)
        token = self.get_token()
        headers = {
            'accept': '*/*',
            'Authorization': token,
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=CFD3B3E7D77946060783845AD59ACF5A'
        }
        response = requests.request("POST", full_url, headers=headers, data=payload)
        res = json.loads(response.text)
        if (not ("code" in res.keys())) or res["code"] != 200:
            print("query_objects_by_oid() error: ")
            print(response.text)
            return -1
        else:
            # 返回list, 其中的每一个元素都是一个字典类型的对象
            return res["data"]

    def edit_relation_obj(self, classname, obj):

        full_url = self.url + "/api/app//dwf/v1/omf/relations/" + classname + "/objects-update"
        payload = json.dumps([
            obj
        ])
        token = self.get_token()
        headers = {
            'accept': '*/*',
            'Authorization': token,
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=CFD3B3E7D77946060783845AD59ACF5A'
        }
        response = requests.request("POST", full_url, headers=headers, data=payload)
        res = json.loads(response.text)
        if ("code" not in res.keys()) or res["code"] != 200:
            print("create_relations() error: ")
            print(response.text)
            return -1
        else:
            # 新建成功
            return 1