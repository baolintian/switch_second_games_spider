import requests
import json
from DWFIO import *
url = "https://shop42406197.youzan.com/wscshop/goods-api/goodsByTagAlias.json?alias=mpwlx8zb&pageSize=100&json=1"

payload={}
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cookie': 'DO_CHECK_YOU_VERSION=1; KDTSESSIONID=YZ923949055372083200YZvALRIAYB; nobody_sign=YZ923949055372083200YZvALRIAYB; _kdt_id_=42214029; yz_log_ftime=1640328221551; yz_log_uuid=c6d48fad-5f5a-68c3-ea4a-df302f971981; yz_log_seqb=1640328221840; trace_sdk_context_banner_id=f.91933887~image_ad.5~0~zEMVI3zx; trace_sdk_context_pv_id=/wscshop/showcase/feature~e9a08941-b59f-499c-a2f3-6127ab856e62; yz_log_seqn=61; KDTSESSIONID=YZ923956086883667968YZLpobCwQ0; nobody_sign=YZ923956086883667968YZLpobCwQ0'
}

response = requests.request("GET", url, headers=headers, data=payload)

dwfio = DWFIO(url="http://i-hxb22khs.cloud.nelbds.org.cn:8180", username="admin", passwd="5649052e")

response_json = json.loads(response.text)
item_list = response_json["data"]["list"]
item_length = len(item_list)
# 数量会超过99吗
items = []
results = dwfio.query_objects_by_condition("SwitchGame", "and 1=1")
for result in results:
  dwfio.delete_relations_by_oid("SwitchGame", result["oid"])
for item in item_list:
  temp = []
  temp.append((item['title']))
  temp.append(eval(item['activityPrice']))

  temp.append((item['totalSoldNum']))
  temp.append((item['totalStock']))
  temp.append((item['imageUrl']))
  temp.append((item['url']))
  items.append(temp)
  obj = {
    "gameName": temp[0],
    "price": int(temp[1]),
    "totalSell": temp[2],
    "totalStock": temp[3],
    "imageUrl": temp[5],
    "image": temp[4]
  }
  dwfio.create_obj("SwitchGame", obj)

print(items)