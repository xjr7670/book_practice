CREATE TABLE `t_board` (
  `board_id` int(11) NOT NULL auto_increment COMMENT '论坛版块ID',
  `board_name` varchar(150) NOT NULL default '' COMMENT '论坛版块名',
  `board_desc` varchar(255) default NULL COMMENT '论坛版块描述',
  `topic_num` int(11) NOT NULL default '0' COMMENT '帖子数目',
  PRIMARY KEY  (`board_id`),
  KEY `AK_Board_NAME` (`board_name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
CREATE TABLE `t_post` (
  `post_id` int(11) NOT NULL auto_increment COMMENT '帖子ID',
  `board_id` int(11) NOT NULL default '0' COMMENT '论坛ID',
  `topic_id` int(11) NOT NULL default '0' COMMENT '话题ID',
  `user_id` int(11) NOT NULL default '0' COMMENT '发表者ID',
  `post_type` tinyint(4) NOT NULL default '2' COMMENT '帖子类型 1:主帖子 2:回复帖子',
  `post_title` varchar(50) NOT NULL COMMENT '帖子标题',
  `post_text` text NOT NULL COMMENT '帖子内容',
  `create_time` date NOT NULL COMMENT '创建时间',
  PRIMARY KEY  (`post_id`),
  KEY `IDX_POST_TOPIC_ID` (`topic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COMMENT='帖子';
