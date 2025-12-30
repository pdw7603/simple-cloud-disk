package com.example.clouddisk.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.clouddisk.entity.FileMetadata;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

/**
 *  * 文件元数据 Mapper 接口（数据库操作）
 *   */
@Mapper // 标记为 MyBatis Mapper 接口
public interface FileMetadataMapper extends BaseMapper<FileMetadata> {

    /**
 *      * 根据用户ID查询文件列表
 *           * @param userId 用户ID
 *                * @return 文件元数据列表
 *                     */
    List<FileMetadata> selectByUserId(@Param("userId") Long userId);

    /**
 *      * 根据文件ID查询文件信息
 *           * @param fileId 文件ID
 *                * @return 文件元数据
 *                     */
    FileMetadata selectByFileId(@Param("fileId") Long fileId);
}
