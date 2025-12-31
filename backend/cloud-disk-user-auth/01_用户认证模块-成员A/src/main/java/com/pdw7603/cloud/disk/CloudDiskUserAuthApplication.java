package com.pdw7603.cloud.disk;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 *  * SpringBoot启动类（用户认证模块）
 *   * 作者：616yangshicheng
 *    */
@SpringBootApplication
public class CloudDiskUserAuthApplication {
    public static void main(String[] args) {
        // 启动SpringBoot服务
        SpringApplication.run(CloudDiskUserAuthApplication.class, args);
        System.out.println("用户认证模块服务启动成功！端口：8080");
    }
}
