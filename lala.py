from app import app
from flask import request, session
from link import create,find

@app.route('/sendform', methods=['POST'])
def keepform():
    data = request.get_json()
    name=data['name']
    gender=data['gender']
    grade=data['grade']
    area=data['area']
    college=data['college']
    phone=data['phone']
    department=data['department']
    faceTime=data['faceTime']
    introduction=data['introduction']
    
    result = find(phone)
    if result:
        return {
            'errcode': 400,
            'errmsg': '已被填写，请重新填写'
        }, 400
    
    rowcount = create(name,gender,grade,area,college,phone,department,faceTime,introduction)
    if rowcount > 0:
        return {
            'errcode': 0,
            'errmsg': '祝贺你，报名成功'
        }, 200
    
    return {
        'errcode': 400,
        'errmsg': '请检查网络或其他设置'
    }, 400