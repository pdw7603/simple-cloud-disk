package com.pdw7603.cloud.disk.controller;

import com.pdw7603.cloud.disk.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

/**
 * 用户接口层，暴露注册、登录接口
 */
@RestController
@RequestMapping("/api/user")
public class UserController {
    @Autowired
    private UserService userService;

    /**
     * 用户注册接口
     * @param paramMap 接收前端传入的用户名、密码、邮箱
     * @return JSON响应结果
     */
    @PostMapping("/register")
    public Map<String, Object> register(@RequestBody Map<String, String> paramMap) {
        // 正确创建HashMap，泛型类型声明无误
        Map<String, Object> resultMap = new HashMap<String, Object>();
        String username = paramMap.get("username");
        String password = paramMap.get("password");
        String email = paramMap.get("email");

        // 简单参数校验
        if (username == null || username.trim().isEmpty() || password == null || password.trim().isEmpty() || email == null || email.trim().isEmpty()) {
            resultMap.put("code", 400);
            resultMap.put("msg", "用户名、密码、邮箱不能为空！");
            resultMap.put("data", null);
            return resultMap;
        }

        // 调用业务层注册方法
        boolean registerSuccess = userService.userRegister(username, password, email);
        if (registerSuccess) {
            resultMap.put("code", 200);
            resultMap.put("msg", "注册成功！");
            resultMap.put("data", null);
        } else {
            resultMap.put("code", 500);
            resultMap.put("msg", "注册失败！用户名已存在");
            resultMap.put("data", null);
        }
        return resultMap;
    }

    /**
     * 用户登录接口
     * @param paramMap 接收前端传入的用户名、密码
     * @return JSON响应结果
     */
    @PostMapping("/login")
    public Map<String, Object> login(@RequestBody Map<String, String> paramMap) {
        // 正确创建HashMap，泛型类型声明无误
        Map<String, Object> resultMap = new HashMap<String, Object>();
        String username = paramMap.get("username");
        String password = paramMap.get("password");

        // 简单参数校验
        if (username == null || username.trim().isEmpty() || password == null || password.trim().isEmpty()) {
            resultMap.put("code", 400);
            resultMap.put("msg", "用户名、密码不能为空！");
            resultMap.put("data", null);
            return resultMap;
        }

        // 调用业务层登录方法
        String token = userService.userLogin(username, password);
        if (token != null) {
            resultMap.put("code", 200);
            resultMap.put("msg", "登录成功！");
            resultMap.put("data", token);
        } else {
            resultMap.put("code", 500);
            resultMap.put("msg", "登录失败！用户名或密码错误");
            resultMap.put("data", null);
        }
        return resultMap;
    }
}

