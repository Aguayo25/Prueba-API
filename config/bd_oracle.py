import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir="C:\opt\oracle\instantclient_21_8")
dsn = cx_Oracle.makedsn(host='10.30.17.220', port=1521, service_name='TRNG')
connection = cx_Oracle.connect(user='BANINST1', password='u_pick_it', dsn=dsn)