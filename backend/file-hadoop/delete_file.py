import pymysql
import os

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cloud_disk',
    'charset': 'utf8mb4'
}

def delete_file():
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # 查询用户最新上传的文件（动态获取file_id）
        sql = "SELECT * FROM file_info WHERE user_id=1 ORDER BY id DESC LIMIT 1"
        cursor.execute(sql)
        file_data = cursor.fetchone()
        
        if not file_data:
            print({'code':500, 'msg':'文件不存在'})
            return
            
        file_id = file_data['id']
        file_path = file_data['file_path']
        
        # 物理删除文件
        if os.path.exists(file_path):
            os.remove(file_path)
        # 逻辑删除数据库数据
        sql_del = "DELETE FROM file_info WHERE id=%s"
        cursor.execute(sql_del, (file_id,))
        conn.commit()
        
        print({'code':200, 'msg':'文件删除成功', 'data':{'file_id':file_id}})
        cursor.close()
        conn.close()
    except Exception as e:
        print({'code':500, 'msg':f'删除失败：{str(e)}'})

if __name__ == "__main__":
    delete_file()
