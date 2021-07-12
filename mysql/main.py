# -*- coding: utf-8 -*-
# 모듈 호출
import pymysql
# DB에 연결함
conn = pymysql.connect(host='localhost', user='service', password='local', database='mytest', charset='utf8mb4')
# 커서를 만듬
cursor = conn.cursor()
# 커서에 쿼리를 얻어서 실행 시킴
cursor.execute('SELECT Itemno, Category, FoodName, Company, Price FROM supermarket;')
# 한 행을 가져옴
row = cursor.fetchone()
# 행이 존재할 때까지, 하나씩 행을 증가시키면서 1번째 컬럼을 숫자 2째번 컬럼을 문자로 출력함
while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()
#연결을 닫음
conn.close()
