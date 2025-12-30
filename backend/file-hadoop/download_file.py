import pymysql
import os

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cloud_disk',
    'charset': 'utf8mb4'
}

def download_file():
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # 查询用户最新上传的文件（动态获取file_id，不再硬编码）
        sql = "SELECT * FROM file_info WHERE user_id=1 ORDER BY id DESC LIMIT 1"
        cursor.execute(sql)
        file_data = cursor.fetchone()
        
        if not file_data:
            print({'code':500, 'msg':'文件不存在'})
            return
            
        file_id = file_data['id']
        file_path = file_data['file_path']
        if os.path.exists(file_path):
            print({'code':200, 'msg':'文件下载成功', 'data':{'file_id':file_id, 'file_path':file_path}})
        else:
            print({'code':500, 'msg':'文件路径不存在'})
            
        cursor.close()
        conn.close()
    except Exception as e:
        print({'code':500, 'msg':f'下载失败：{str(e)}'})

if __name__ == "__main__":
    download_file()
