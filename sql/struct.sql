/*
Navicat MySQL Data Transfer
Source Server         : localhost_3306
Source Server Version : 50536
Source Host           : localhost:3306
Source Database       : xinzhi
Target Server Type    : MYSQL
Target Server Version : 50536
File Encoding         : 65001
Date: 2019-04-11 11:38:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for member
-- ----------------------------s
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member` (
  `id` int(30) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `nickname` varchar(50) DEFAULT NULL,
  `bio` TEXT DEFAULT NULL,
  `birth` varchar(20) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `preference` TEXT DEFAULT NULL,
  `main_topic` varchar(255) DEFAULT NULL,
  `topics` varchar(255) DEFAULT NULL,
  `state` int(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `member` ADD PRIMARY KEY (`id`)
alter table `member` modify id int auto_increment

-- ----------------------------
-- Table structure for group
-- ----------------------------
DROP TABLE IF EXISTS `groups`;
CREATE TABLE `groups` (
  `id` int(30) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `desc` TEXT DEFAULT NULL,
  `photo` varchar(300) DEFAULT NULL,
  `members` int(10) DEFAULT NULL,
  `create_time` varchar(100) DEFAULT NULL,
  `who` int(30) DEFAULT NULL,
  `rating` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `main_topic` varchar(255) DEFAULT NULL,
  `topics` varchar(255) DEFAULT NULL,
  `verify` int(1) DEFAULT 0,
  `state` int(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
alter table `groups` modify id int auto_increment

-- ----------------------------
-- Table structure for group-member
-- ----------------------------
DROP TABLE IF EXISTS `group_member`;
CREATE TABLE `group_member` (
  `member_id` int(30) NOT NULL,
  `group_id` int(30) NOT NULL,
  `join_time` varchar(100) NOT NULL,
  `verify` int(1) DEFAULT 0,
  `rating` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`member_id`, `group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `group_member` ADD column `id` int(30) default null

-- ----------------------------
-- Table structure for activity
-- ----------------------------
DROP TABLE IF EXISTS `activity`;
CREATE TABLE `activity` (
  `id` int(30) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `desc` TEXT DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `create_time` varchar(100) DEFAULT NULL,
  `event_time` varchar(100) DEFAULT NULL,
  `update_time` varchar(100) DEFAULT NULL,
  `images` TEXT DEFAULT NULL,
  `group_id` int(30) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `main_topic` varchar(100) DEFAULT NULL,
  `topics` varchar(100) DEFAULT NULL,
  `verify` int(1) DEFAULT 0,
  `state` int(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
alter table `activity` modify id int auto_increment

DROP TABLE IF EXISTS `member_activity`;
CREATE TABLE `member_activity` (
  `member_id` int(30) NOT NULL,
  `activity_id` int(30) NOT NULL,
  `join_time` varchar(100) NOT NULL,
  PRIMARY KEY (`member_id`, `activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `member_activity` ADD column `id` int(30) default null
-- ----------------------------
-- Table structure for topics
-- ----------------------------
DROP TABLE IF EXISTS `topics`;
CREATE TABLE `topics` (
  `id` int(30) NOT NULL,
  `name` varchar(100) NOT NULL,
  `desc` TEXT DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
alter table `topics` modify id int auto_increment

--alter table activity add constraint FK_ID foreign key(group_id) REFERENCES groups(id)

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `users` (`username`, `password`) VALUES('root', 'b9be11166d72e9e3ae7fd407165e4bd2');