import pymysql
import os

# 数据库连接配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cloud_disk',
    'charset': 'utf8mb4'
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

# 文件删除核心函数（逻辑删除+可选物理删除）
def delete_file(file_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # 1. 查询文件信息（获取file_path和file_name，用于日志和物理删除）
        query_sql = "SELECT file_name, file_path FROM file_info WHERE id=%s"
        cursor.execute(query_sql, (file_id,))
        file_data = cursor.fetchone()
        if not file_data:
            cursor.close()
            conn.close()
            return {"code": 500, "msg": "文件不存在"}

        file_name = file_data['file_name']
        file_path = file_data['file_path']

        # 2. 逻辑删除（核心：更新is_delete=1）
        update_sql = "UPDATE file_metadata SET is_delete=1, update_time=NOW() WHERE id=%s"
        cursor.execute(update_sql, (file_id,))
        conn.commit()

        # 3. 可选：物理删除服务器上的文件
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"【物理删除文件】file_id={file_id}, file_name={file_name}, path={file_path}")

        cursor.close()
        conn.close()

        # 打印日志
        print(f"【逻辑删除文件】file_id={file_id}, file_name={file_name}")
        return {"code": 200, "msg": "文件删除成功"}
    except Exception as e:
        print(f"【删除失败】file_id={file_id}, error={str(e)}")
        return {"code": 500, "msg": f"文件删除失败：{str(e)}"}

# 测试删除（代码块完整闭合）
if __name__ == "__main__":
    # 替换为实际的file_id进行测试（注释也完整，无语法缺失）
    result = delete_file(1)
    print(result)
    pass
