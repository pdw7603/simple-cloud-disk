package com.pdw7603.cloud.disk.service;

import com.pdw7603.cloud.disk.entity.User;
import com.pdw7603.cloud.disk.mapper.UserMapper;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import io.jsonwebtoken.SignatureAlgorithm;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import javax.crypto.SecretKey;

/**
 * 用户业务逻辑层，处理注册、登录业务
 */
@Service
public class UserService {
    @Autowired
    private UserMapper userMapper;

    // BCrypt密码加密器
    private BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();

    /**
     * 用户注册
     * @param username 用户名
     * @param password 明文密码
     * @param email 邮箱
     * @return 注册结果（true=成功，false=失败）
     */
    public boolean userRegister(String username, String password, String email) {
        // 1. 校验用户名是否已存在
        User existingUser = userMapper.findUserByUsername(username);
        if (existingUser != null) {
            // 用户名已存在，注册失败
            return false;
        }
        // 2. 密码加密
        String encryptPassword = passwordEncoder.encode(password);
        // 3. 新增用户
        User newUser = new User(username, encryptPassword, email);
        int affectedRows = userMapper.insertUser(newUser);
        return affectedRows == 1;
    }

    /**
     * 用户登录
     * @param username 用户名
     * @param password 明文密码
     * @return JWT token（登录成功）/null（登录失败）
     */
public String userLogin(String username, String password) {
    // 1. 根据用户名查询用户
    User user = userMapper.findUserByUsername(username);
    if (user == null) {
        // 用户不存在，登录失败
        return null;
    }
    // 2. 校验密码（明文密码与加密密码比对）
    boolean passwordMatch = passwordEncoder.matches(password, user.getPassword());
    if (!passwordMatch) {
        // 密码不匹配，登录失败
        return null;
    }
    // 3. 生成JWT token（有效期1小时）
    Map<String, Object> claims = new HashMap<String, Object>();
    claims.put("username", username);
    claims.put("userId", user.getId());
    
    // 核心修改：使用新版API生成256位安全密钥（自动满足HS256要求）
    SecretKey secretKey = Keys.secretKeyFor(SignatureAlgorithm.HS256);
    
    String token = Jwts.builder()
            .setClaims(claims)
            .setIssuedAt(new Date())
            .setExpiration(new Date(System.currentTimeMillis() + 3600 * 1000)) // 1小时过期
            .signWith(secretKey) // 使用自动生成的安全密钥签名
            .compact();
    return token;
}
}
