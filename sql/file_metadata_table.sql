use cloud_disk;
CREATE TABLE `file_metadata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `file_name` varchar(255) NOT NULL,
  `file_path` varchar(512) NOT NULL,
  `file_size` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `upload_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
  -- 先注释外键约束，等创建user表后再添加
  -- FOREIGN KEY (`user_id`) REFERENCES `user`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
