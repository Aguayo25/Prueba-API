from fastapi import FastAPI
from config.bd_oracle import *



app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello World"}

@app.get('/get_info')
async def get_info_oracle():
    cursor = connection.cursor()
    cursor.execute("SELECT SPRIDEN_FIRST_NAME FROM SPRIDEN WHERE SPRIDEN_ID = '190043150'")
    resultado = cursor.fetchall()

    return resultado

@app.get('/put_info')
async def put_info_oracle():
    cursor = connection.cursor()
    cursor.execute("INSERT INTO trigger_log (log_id, trigger_name, execution_date, result, error_msg) VALUES (secuencia_de_log.NEXTVAL, 'TRG_CASINO_USM', SYSDATE, 'PRUEBA API', NULL)")
    connection.commit()

    




    cursor.close()
    connection.close()

    return "Insercion exitosa"




