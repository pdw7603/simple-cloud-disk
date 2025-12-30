import pymysql
import os

# 数据库连接配置
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'cloud_disk',
    'charset': 'utf8mb4'
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

# 文件下载核心函数（返回文件内容，模拟流返回）
def download_file(file_id, save_local_path="/opt/cloud-disk/download/"):
    try:
        # 创建下载目录
        if not os.path.exists(save_local_path):
            os.makedirs(save_local_path, 0o777)

        conn = get_db_connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        # 1. 查询文件信息（仅查询未删除的文件）
        sql = "SELECT file_name, file_path FROM file_info WHERE id=%s AND is_delete=0"
        cursor.execute(sql, (file_id,))
        file_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if not file_data:
            return {"code": 500, "msg": "文件不存在"}

        file_name = file_data['file_name']
        file_path = file_data['file_path']

        # 2. 校验文件是否存在
        if not os.path.exists(file_path):
            return {"code": 500, "msg": "服务器上的物理文件不存在"}

        # 3. 读取文件并保存到本地下载目录（模拟浏览器下载）
        target_download_path = os.path.join(save_local_path, file_name)
        with open(file_path, 'rb') as src_file, open(target_download_path, 'wb') as dst_file:
            dst_file.write(src_file.read())

        # 打印日志
        print(f"【文件下载成功】file_id={file_id}, file_name={file_name}, 保存路径={target_download_path}")
        return {
            "code": 200,
            "msg": "文件下载成功",
            "data": {
                "file_name": file_name,
                "save_path": target_download_path
            }
        }
    except Exception as e:
        print(f"【下载失败】file_id={file_id}, error={str(e)}")
        return {"code": 500, "msg": f"文件下载失败：{str(e)}"}

# 测试下载（代码块完整闭合）
if __name__ == "__main__":
    # 替换为实际的file_id进行测试
    result = download_file(2)
    print(result)
    pass
