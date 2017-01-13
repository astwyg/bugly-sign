# -*- coding: utf-8 -*-

import requests

user_list = [
    {
        "username":"17710432234",
        "passwd":"tmyi5177163"
    },
    {
        "username":"15031221287",
        "passwd":"123123"
    },
    {
        "username":"18201160619",
        "passwd":"123456",
    },
    {
        "username":"18210955909",
        "passwd":"123456",
    },
    {
        "username":"18518488066",
        "passwd":"guojie"
    }
]

def make_order(user):
    s = requests.Session()
    r = s.post("http://life.ctyun.com.cn/admin/ajax/userLogin", json={"userPassword":user.get("passwd"),"userPhone":user.get("username")})
    assert r.status_code == 200
    r = s.post("http://life.ctyun.com.cn/ajax/getTodayMeal", json={"pageNo":1,"pageSize":6,"query":{}})
    meal_id = None
    for meal in r.json().get("returnObj").get("result"):
        if u"西山赢府" in meal["mealName"]:
            meal_id = meal["id"]
            break
    r = s.post("http://life.ctyun.com.cn/ajax/takeOrder", json={"addressId":2, "id":meal_id})
    return r.json().get("returnObj").get("msg")



def make_orders(users):
    for user in users:
        print("开始为{}订餐".format(user["username"]))
        try:
            print(make_order(user))
        except Exception, e:
            print("发生错误:"+str(e))
        print("="*10)


if __name__ == "__main__":
    make_orders(user_list)

