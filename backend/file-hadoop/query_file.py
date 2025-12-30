import pymysql

# 数据库连接配置（和上传脚本一致）
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'cloud_disk',
    'charset': 'utf8mb4'
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

# 功能1：查询指定用户的所有文件（user_id=1）
def query_user_files(user_id=1):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # 返回字典格式数据
        sql = """
            SELECT id, file_name, file_path, file_size, file_type, create_time
            FROM file_metadata
            WHERE user_id=%s AND is_delete=0
            ORDER BY create_time DESC
        """
        cursor.execute(sql, (user_id,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        # 打印日志
        print(f"【查询用户文件】user_id={user_id}, 文件数量={len(data)}")
        return {"code": 200, "msg": "查询成功", "data": data}
    except Exception as e:
        print(f"【查询失败】user_id={user_id}, error={str(e)}")
        return {"code": 500, "msg": f"查询失败：{str(e)}"}

# 功能2：查询单个文件详情（根据file_id）
def query_file_detail(file_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = """
            SELECT id, file_name, file_path, file_size, file_type, user_id, create_time
            FROM file_info
            WHERE id=%s AND is_delete=0
        """
        cursor.execute(sql, (file_id,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        if not data:
            return {"code": 500, "msg": "文件不存在或已删除"}
        # 打印日志
        print(f"【查询文件详情】file_id={file_id}, file_name={data['file_name']}")
        return {"code": 200, "msg": "查询成功", "data": data}
    except Exception as e:
        print(f"【查询详情失败】file_id={file_id}, error={str(e)}")
        return {"code": 500, "msg": f"查询详情失败：{str(e)}"}

# 测试查询
if __name__ == "__main__":
    # 测试查询用户1的所有文件
    user_files = query_user_files(1)
    print("用户1的所有文件：", user_files)

    # 测试查询单个文件（替换为实际的file_id，可从用户文件查询结果中获取）
    # file_detail = query_file_detail(1)
    # print("单个文件详情：", file_detail)
