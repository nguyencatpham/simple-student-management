CREATE DATABASE `student_management` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- student_management.Classes definition

CREATE TABLE `Classes` (
  `class_name` varchar(100) NOT NULL,
  `class_size` int NOT NULL,
  `total` int NOT NULL,
  `class_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- student_management.Lessons definition

CREATE TABLE `Lessons` (
  `lesson_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int DEFAULT NULL,
  `score15` double DEFAULT NULL,
  `score45` double DEFAULT NULL,
  PRIMARY KEY (`lesson_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- student_management.Regulations definition

CREATE TABLE `Regulations` (
  `regulation_id` int NOT NULL AUTO_INCREMENT,
  `age_min` int NOT NULL DEFAULT '0',
  `age_max` int NOT NULL DEFAULT '0',
  `score_max` varchar(100) NOT NULL DEFAULT '0',
  PRIMARY KEY (`regulation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- student_management.Students definition

CREATE TABLE `Students` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `class_id` int DEFAULT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `birthday` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `sex` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `Students_FK` (`class_id`),
  CONSTRAINT `Students_FK` FOREIGN KEY (`class_id`) REFERENCES `Students` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;