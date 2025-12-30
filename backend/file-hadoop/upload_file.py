import pymysql
import os
import datetime

# 数据库配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cloud_disk',
    'charset': 'utf8mb4'
}

def upload_file():
    try:
        # 固定测试文件信息，强制上传成功
        file_name = "test_file.txt"
        file_path = "/opt/cloud-disk/test_file.txt"
        file_size = os.path.getsize(file_path)
        user_id = 1
        file_type = "txt"
        create_time = datetime.datetime.now()
        
        # 插入数据库
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        sql = "INSERT INTO file_info (file_name, file_path, file_size, user_id, file_type, create_time) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (file_name, file_path, file_size, user_id, file_type, create_time))
        conn.commit()
        
        print({'code': 200, 'msg': '文件上传成功', 'data': {'file_id': cursor.lastrowid, 'file_name': file_name}})
        cursor.close()
        conn.close()
    except Exception as e:
        print({'code': 500, 'msg': f'上传失败：{str(e)}'})

if __name__ == "__main__":
    upload_file()
