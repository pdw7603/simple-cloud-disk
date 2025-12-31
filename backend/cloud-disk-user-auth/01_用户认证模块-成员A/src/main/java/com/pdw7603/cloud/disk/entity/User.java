package com.pdw7603.cloud.disk.entity;

import java.util.Date;

/**
 *用户实体类，对应MySQL cloud_disk.user表
 */

public class User {
    // 主键id
    private Long id;
    // 用户名（唯一）
    private String username;
    // 密码（加密存储）
    private String password;
    // 创建时间
    private Date createTime;

    // 无参构造方法
    public User() {
    }

    // 有参构造方法（不含id和createTime，由数据库自动生成）
    public User(String username, String password) {
        this.username = username;
        this.password = password;
    }

    // getter和setter方法（必须添加，支持属性赋值和取值）
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Date getCreateTime() {
        return createTime;
    }

    public void setCreateTime(Date createTime) {
        this.createTime = createTime;
    }
}
