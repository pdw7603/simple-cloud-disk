import pymysql
import time
import random
import string
import os

# 数据库连接配置（适配你的环境）
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cloud_disk',
    'charset': 'utf8mb4'
}

# 获取数据库连接
def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

# 生成6位字母数字随机串
def get_random_str():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# 生成YYYYMMDDHHmmss格式时间戳
def get_timestamp():
    return time.strftime('%Y%m%d%H%M%S', time.localtime())

# 文件上传核心函数
def upload_file(file_path, user_id=1):
    try:
        # 1. 基础校验：判断文件是否存在且大小大于0
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return {"code": 500, "msg": "文件不能为空"}

        # 2. 获取文件基础信息
        original_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        # 简单判断文件类型（可根据需求扩展）
        file_ext = os.path.splitext(original_name)[1].lower()
        file_type_map = {'.pdf': 'application/pdf', '.png': 'image/png', '.txt': 'text/plain', '.jpg': 'image/jpeg'}
        file_type = file_type_map.get(file_ext, 'application/octet-stream')

        # 3. 生成唯一存储文件名
        timestamp = get_timestamp()
        random_str = get_random_str()
        save_file_name = f"{timestamp}_{random_str}_{original_name}"

        # 4. 拼接绝对存储路径
        base_path = "/opt/cloud-disk/upload/"
        target_file_path = os.path.join(base_path, save_file_name)

        # 5. 复制文件到目标目录（模拟文件上传写入）
        with open(file_path, 'rb') as src_file, open(target_file_path, 'wb') as dst_file:
            dst_file.write(src_file.read())

        # 6. 插入file_info表（预编译SQL，防注入）
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO file_metadata (file_name, file_path, file_size, file_type, user_id)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (original_name, target_file_path, file_size, file_type, user_id))
        file_id = cursor.lastrowid  # 获取新插入的文件ID
        conn.commit()
        cursor.close()
        conn.close()

        # 7. 返回规范结果
        return {
            "code": 200,
            "msg": "文件上传成功",
            "data": {
                "file_id": file_id,
                "file_name": original_name,
                "file_path": target_file_path,
                "user_id": user_id
            }
        }
    except Exception as e:
        # 异常捕获，打印日志
        print(f"【上传失败】user_id={user_id}, error={str(e)}")
        return {"code": 500, "msg": f"文件上传失败：{str(e)}"}

# 测试上传（可替换为你的本地测试文件路径）
if __name__ == "__main__":
    # 示例：上传服务器上的/test.txt文件（可先创建该文件：echo "test" > /test.txt）
    test_file_path = "/test_download.txt"
    result = upload_file(test_file_path)
    print(result)
