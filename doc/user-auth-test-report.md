# 用户认证模块接口测试报告
## 一、 测试基础信息
- 测试执行人：成员 A
- 测试时间：项目第 5 天
- 测试环境：CentOS 7 + JDK 1.8 + MySQL 5.7 + SpringBoot 2.7.18 + JJWT 0.11.5
- 测试工具：curl 命令（命令行）
- 测试范围：用户注册接口、用户登录接口、身份校验接口

## 二、 核心测试用例及结果
### 1.  用户注册接口
- 请求方式：POST
- 请求地址：http://localhost:8080/api/user/register
- 请求头：Content-Type: application/json
- 正常请求参数：{"username":"testA","password":"123456","email":"testA@163.com"}
- 正常测试结果：返回 {"msg":"注册成功！","code":200}，MySQL user 表中新增对应用户数据（密码为 BCrypt 加密格式）
- 异常测试用例：用户名重复（传入已存在的 username）
- 异常测试结果：返回 {"msg":"用户名已存在","code":500}，无新增用户数据，测试通过

### 2.  用户登录接口
- 请求方式：POST
- 请求地址：http://localhost:8080/api/user/login
- 请求头：Content-Type: application/json
- 正常请求参数：{"username":"testA","password":"123456"}
- 正常测试结果：返回 {"msg":"登录成功！","code":200,"data":"JWT令牌字符串"}，令牌格式合规（三段式，以 . 分隔）
- 异常测试用例：密码错误（传入正确用户名，错误密码）
- 异常测试结果：返回 {"msg":"密码错误","code":500}，无 JWT 令牌返回，测试通过

### 3.  身份校验接口
- 请求方式：POST
- 请求地址：http://localhost:8080/api/user/verifyToken
- 请求头：Content-Type: application/json
- 正常请求参数：{"token":"登录接口返回的有效 JWT 令牌"}
- 正常测试结果：返回 {"msg":"令牌有效","code":200,"data":{"username":"testA","userId":1}}
- 异常测试用例：传入无效令牌（篡改令牌字符串/令牌过期）
- 异常测试结果：返回 {"msg":"令牌无效","code":500}，测试通过

## 三、 问题记录与解决方案
1.  问题1：JWT 生成报错（Illegal base64 character: '_'）
   - 原因：密钥包含下划线，不符合标准 Base64 字符要求
   - 解决方案：删除密钥中的下划线，使用纯字母数字组合的合法密钥
2.  问题2：JWT 签名报错（WeakKeyException）
   - 原因：密钥长度不足 256 位（128 位），不满足 HS256 算法安全要求
   - 解决方案：延长密钥至 32 位以上（256 位），满足 JWA 规范
3.  问题状态：所有问题已解决，接口功能正常

## 四、 测试总结
1.  功能完整性：用户认证模块 3 个核心接口功能均实现，满足业务需求
2.  测试有效性：正常场景与异常场景均测试覆盖，结果符合预期
3.  整体结论：用户认证模块接口可用，无功能缺陷，可提交验收
