package com.pdw7603.cloud.disk.mapper;

import com.pdw7603.cloud.disk.entity.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

/**
 * 用户数据访问层，操作MySQL数据库
 */

@Repository
public class UserMapper {
    // 自动注入JdbcTemplate，简化数据库操作
    @Autowired
    private JdbcTemplate jdbcTemplate;

    /**
     * 根据用户名查询用户
     * @param username 用户名
     * @return User对象（不存在返回null）
     */
    public User findUserByUsername(String username) {
        String sql = "select id, username, password, email, create_time from user where username = ?";
        try {
            return jdbcTemplate.queryForObject(sql, new BeanPropertyRowMapper<User>(User.class), username);
        } catch (Exception e) {
            // 查询不到用户时抛出异常，返回null
            return null;
        }
    }

    /**
     * 新增用户（注册功能）
     * @param user 用户对象
     * @return 受影响行数（1=成功，0=失败）
     */
    public int insertUser(User user) {
        String sql = "insert into user (username, password, email, create_time) values (?, ?, ?, now())";
        return jdbcTemplate.update(sql, user.getUsername(), user.getPassword(), user.getEmail());
    }
}

