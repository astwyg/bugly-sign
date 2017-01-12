# -*- coding: utf-8 -*-

import requests

user_list = [
    {
        "username":"17710432234",
        "passwd":"tmyi5177163"
    }
]

def make_order(user):
    s = requests.Session()
    r = s.post("http://life.ctyun.com.cn/admin/ajax/userLogin", json={"userPassword":user.get("passwd"),"userPhone":user.get("username")})
    assert r.status_code == 200
    r = s.post("http://life.ctyun.com.cn/ajax/getTodayMeal", json={"pageNo":1,"pageSize":6,"query":{}})
    meal_id = None
    for meal in r.json().get("returnObj").get("result"):
        if "西山赢府" in meal["mealName"]:
            meal_id = meal["id"]
            break
    r = s.post()



def make_orders(users):
    for user in users:
        print("开始为{}订餐".format(user["username"]))
        print(make_order(user))


if __name__ == "__main__":
    global user_list
    make_orders(user_list)

