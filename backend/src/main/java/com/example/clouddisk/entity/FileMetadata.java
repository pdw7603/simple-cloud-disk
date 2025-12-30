package com.example.clouddisk.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.util.Date;

/**
 *  * 文件元数据实体类（对应 file_metadata 表）
 *   */
@Data // Lombok 注解，自动生成 getter/setter/toString 等方法
@TableName("file_metadata") // 关联数据库表名
public class FileMetadata {
    @TableId(type = IdType.AUTO) // 主键自增
    private Long id; // 文件ID
    private String fileName; // 文件名
    private String filePath; // HDFS 文件完整路径
    private Long fileSize; // 文件大小（字节）
    private Long userId; // 所属用户ID
    private Date uploadTime; // 上传时间
}
