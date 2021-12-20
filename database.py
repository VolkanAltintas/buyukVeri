import function
import sqlite3
# db=sqlite3.connect('xx.db')
db=sqlite3.connect('deneme.db')
#db1=sqlite3.connect('C:/Users/volka/OneDrive/Masaüstü/sqlite/deneme1.db')

imlec=db.cursor()
kmt="CREATE TABLE IF NOT EXISTS veriler(ad,soyad,yas)"
imlec.execute(kmt)

#imlec.execute("""CREATE TABLE 
#veriler(ad,soyad,yas)""")
"""
kmt="INSERT INTO veriler VALUES('Bünyamin','Efe',20)"
imlec.execute(kmt)
"""
#db.commit()
"""
kmt="Select * from veriler"
imlec.execute(kmt)

bilgiler=imlec.fetchall()
print(bilgiler)

for bilgi in imlec:
    print(bilgi)
"""
"""
kmt="Select * from veriler where ad=?"
imlec.execute(kmt,('Gökhan',))
bilgi = imlec.fetchone()

print("İsim : "+str(bilgi[0]))
print("Soyisim : "+str(bilgi[1]))
print("Yas : "+str(bilgi[2]))

kmt="select * from veriler"
imlec.execute(kmt)
bilgiler=imlec.fetchmany(4)
print(bilgiler)


kmt="Select * from veriler"
imlec.execute(kmt)

for bilgi in range(2):
    print(imlec.fetchone())


kmt="UPDATE veriler SET yas = ? where ad=?"
imlec.execute(kmt,(60,'Volkan'))
db.commit()

kmt="Select * from veriler"
imlec.execute(kmt)
bilgiler=imlec.fetchall()
print(bilgiler)
"""

kmt="Delete from veriler where ad = ?"
imlec.execute(kmt,('Bünyamin',))
db.commit()

"""
kmt="Select * from veriler"
imlec.execute(kmt)
bilgiler=imlec.fetchall()
print(bilgiler)
"""
kmt="Select * from veriler"
bilgiler=function.sorgula(db,kmt).fetchall()
print(bilgiler)


db.close()