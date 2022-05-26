import random
import pymysql

host = 'localhost'
user = 'root'
passwd = '123456'
db = 'relic'
db = pymysql.connect(host=host, port=3306, user=user, passwd=passwd, db=db, charset='utf8')
cur = db.cursor()
cur.execute("Truncate device_data")
cur.execute("Truncate risk_time_area_data")
allarea = []
for i in range(43):
    lon = random.uniform(110,111)
    lat = random.uniform(30,31)
    area = [lon,lat]
    allarea.append(area)

device_id = 0
for i in range(120):
    area_id = random.randint(1,43)
    device_type = random.randint(1,2)
    cur.execute("insert into device_data (device_id,area_id,device_type,coordinate_long,coordinate_lati) values (%s,%s,%s,%s,%s);",(str(device_id),str(area_id),str(device_type),str(allarea[area_id-1][0]),str(allarea[area_id-1][1])))
    cur.connection.commit()
    device_id += 1

cur.execute("select anomalous_event_id from anomalous_event_data where anomalous_event_id > 40000")
allevent = cur.fetchall()
for i in range(200):
    time = random.randint(1,10000) + 1651310000
    risk_id = 4
    anomalous_event_id = allevent[random.randint(0,len(allevent)-1)][0]
    area_id = area_id = random.randint(1,43)
    cur.execute("insert into risk_time_area_data (time,risk_id,anomalous_event_id,area_id) values (%s,%s,%s,%s);",(str(time),str(risk_id),str(anomalous_event_id),str(area_id)))
    cur.connection.commit()

db.close()