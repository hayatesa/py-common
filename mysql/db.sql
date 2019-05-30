/*
 Navicat Premium Data Transfer

 Source Server         : 119.29.94.246
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : 119.29.94.246:3306
 Source Schema         : biller_cat

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 30/04/2019 16:57:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for biller
-- ----------------------------
DROP TABLE IF EXISTS `biller`;
CREATE TABLE `biller`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_access_time` datetime(0) DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
  `create_time` datetime(0) DEFAULT NULL,
  `update_time` datetime(0) DEFAULT NULL,
  `create_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `update_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of biller
-- ----------------------------
INSERT INTO `biller` VALUES ('17ae7j05b899bh45s44lgi46w6o7g2', 'kimi', 'pbkdf2:sha256:50000$Pbk6FrQE$eae4e093dc4749376e355f91f8215980a5a62414380d28c5ab72aabfe2adbb1e', '2019-03-13 16:37:07', 0, '2019-02-26 18:02:03', NULL, NULL, NULL);
INSERT INTO `biller` VALUES ('7j05b17ae899bhi46w6o7g45s44lg2', 'leo', 'pbkdf2:sha256:50000$nxBeeLWs$48477b9a2e6181456951da0638b9f871b37d4208cefe74f741b899aff56166ab', '2019-03-02 19:54:19', 0, '2019-02-26 18:02:03', NULL, NULL, NULL);
INSERT INTO `biller` VALUES ('7j05b9bh4517ag2s44lgi46w6o7', 'haha', 'pbkdf2:sha256:50000$5JO2xdRx$898ff2170b8d7d9173f1474f8c195c4b58ab84f921d9d31d6cd9d57c87ca63b5', '2019-03-02 19:54:23', 1, '2019-02-26 21:59:10', NULL, NULL, NULL);
INSERT INTO `biller` VALUES ('e7j05b899bh45s44lgi46w6o717ag2', '管理员', 'pbkdf2:sha256:50000$lzy6Yx6O$89ffcb5f52efe8904f7d29ecf04d8660684e7e0eb98ff9c2fea03eafa1cf9fa9', '2019-03-02 19:54:26', 0, '2019-02-26 21:59:10', NULL, NULL, NULL);

-- ----------------------------
-- Table structure for biller_auth_github
-- ----------------------------
DROP TABLE IF EXISTS `biller_auth_github`;
CREATE TABLE `biller_auth_github`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `biller_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'FK',
  `github_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_access_time` datetime(0) DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
  `create_time` datetime(0) DEFAULT NULL,
  `update_time` datetime(0) DEFAULT NULL,
  `create_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `update_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `FK_GITHUB_BILLER`(`biller_id`) USING BTREE,
  CONSTRAINT `FK_GITHUB_BILLER` FOREIGN KEY (`biller_id`) REFERENCES `biller` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for biller_auth_qq
-- ----------------------------
DROP TABLE IF EXISTS `biller_auth_qq`;
CREATE TABLE `biller_auth_qq`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `biller_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'FK',
  `qq_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_access_time` datetime(0) DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
  `create_time` datetime(0) DEFAULT NULL,
  `update_time` datetime(0) DEFAULT NULL,
  `create_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `update_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `FK_QQ_BILLER`(`biller_id`) USING BTREE,
  CONSTRAINT `FK_QQ_BILLER` FOREIGN KEY (`biller_id`) REFERENCES `biller` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for biller_auth_wechat
-- ----------------------------
DROP TABLE IF EXISTS `biller_auth_wechat`;
CREATE TABLE `biller_auth_wechat`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `biller_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'FK',
  `wechat_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_access_time` datetime(0) DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
  `create_time` datetime(0) DEFAULT NULL,
  `update_time` datetime(0) DEFAULT NULL,
  `create_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `update_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `FK_WECHAT_BILLER`(`biller_id`) USING BTREE,
  CONSTRAINT `FK_WECHAT_BILLER` FOREIGN KEY (`biller_id`) REFERENCES `biller` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for biller_info
-- ----------------------------
DROP TABLE IF EXISTS `biller_info`;
CREATE TABLE `biller_info`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `biller_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'FK',
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '头像URL',
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
  `create_time` datetime(0) DEFAULT NULL,
  `update_time` datetime(0) DEFAULT NULL,
  `create_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `update_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `FK_INFO_BILLER`(`biller_id`) USING BTREE,
  CONSTRAINT `FK_INFO_BILLER` FOREIGN KEY (`biller_id`) REFERENCES `biller` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for sys_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_log`;
CREATE TABLE `sys_log`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
  `create_time` datetime(0) DEFAULT NULL,
  `create_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for sys_permission
-- ----------------------------
DROP TABLE IF EXISTS `sys_permission`;
CREATE TABLE `sys_permission`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `permission` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
  `create_time` datetime(0) NOT NULL,
  `update_time` datetime(0) DEFAULT NULL,
  `create_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `update_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for sys_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_role`;
CREATE TABLE `sys_role`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
  `create_time` datetime(0) NOT NULL,
  `update_time` datetime(0) DEFAULT NULL,
  `create_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `update_by` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for sys_role_permission
-- ----------------------------
DROP TABLE IF EXISTS `sys_role_permission`;
CREATE TABLE `sys_role_permission`  (
  `role_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `permission_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`permission_id`, `role_id`) USING BTREE,
  INDEX `FK_RP_ROLE`(`role_id`) USING BTREE,
  CONSTRAINT `FK_RP_PERMISSION` FOREIGN KEY (`permission_id`) REFERENCES `sys_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_RP_ROLE` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `avatar` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `last_access_time` datetime(0) DEFAULT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
  `create_time` datetime(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES ('17ae7j05b899bh45s44lgi46w6o7g2', 'kimi', 'pbkdf2:sha256:50000$Pbk6FrQE$eae4e093dc4749376e355f91f8215980a5a62414380d28c5ab72aabfe2adbb1e', '溶酶菌', '/img/default-avatar-80x80.gif', '2019-03-13 16:37:07', 0, '2019-02-26 18:02:03');
INSERT INTO `sys_user` VALUES ('7j05b17ae899bhi46w6o7g45s44lg2', 'leo', 'pbkdf2:sha256:50000$nxBeeLWs$48477b9a2e6181456951da0638b9f871b37d4208cefe74f741b899aff56166ab', '溶酶菌', '/img/default-avatar-80x80.gif', '2019-03-02 19:54:19', 0, '2019-02-26 18:02:03');
INSERT INTO `sys_user` VALUES ('7j05b9bh4517ag2s44lgi46w6o7', 'haha', 'pbkdf2:sha256:50000$5JO2xdRx$898ff2170b8d7d9173f1474f8c195c4b58ab84f921d9d31d6cd9d57c87ca63b5', '溶酶菌', '/img/default-avatar-80x80.gif', '2019-03-02 19:54:23', 1, '2019-02-26 21:59:10');
INSERT INTO `sys_user` VALUES ('e7j05b899bh45s44lgi46w6o717ag2', '管理员', 'pbkdf2:sha256:50000$lzy6Yx6O$89ffcb5f52efe8904f7d29ecf04d8660684e7e0eb98ff9c2fea03eafa1cf9fa9', '溶酶菌', '/img/default-avatar-80x80.gif', '2019-03-02 19:54:26', 0, '2019-02-26 21:59:10');

-- ----------------------------
-- Table structure for sys_user_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_role`;
CREATE TABLE `sys_user_role`  (
  `user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`user_id`, `role_id`) USING BTREE,
  INDEX `FK_UR_ROLE`(`role_id`) USING BTREE,
  CONSTRAINT `FK_UR_ROLE` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_UR_USER` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
