-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: SmartGate
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `LiveView_log`
--

DROP TABLE IF EXISTS `LiveView_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LiveView_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` datetime(6) NOT NULL,
  `granted` tinyint(1) NOT NULL,
  `snapshot` varchar(100) NOT NULL,
  `person_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `LiveView_log_person_id_cd41b672_fk_LiveView_person_id` (`person_id`),
  CONSTRAINT `LiveView_log_person_id_cd41b672_fk_LiveView_person_id` FOREIGN KEY (`person_id`) REFERENCES `LiveView_person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=159 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LiveView_log`
--

LOCK TABLES `LiveView_log` WRITE;
/*!40000 ALTER TABLE `LiveView_log` DISABLE KEYS */;
INSERT INTO `LiveView_log` VALUES (55,'2021-07-27 10:49:29.844624',1,'snapshots/dslFwGZRWfybsyIss10X.jpg',6),(56,'2021-07-27 10:49:32.366076',1,'snapshots/7fEdg7FISvJR6p0iCNU6.jpg',6),(57,'2021-07-27 10:49:36.383263',1,'snapshots/38Q8MzuT539gtwuxl1BN.jpg',4),(58,'2021-07-27 10:49:38.612007',1,'snapshots/HRFrG9Uk8glCAKp6CvSr.jpg',4),(59,'2021-07-27 10:49:40.818123',1,'snapshots/bTnKw3sw6AVxskLlygoF.jpg',6),(60,'2021-07-27 10:49:42.958776',1,'snapshots/5XBmOThC3wOf4yygu9H9.jpg',4),(61,'2021-07-27 10:49:45.087549',1,'snapshots/HNP4vNrKdQxohFn1tRUV.jpg',4),(62,'2021-07-27 10:49:47.356005',1,'snapshots/7EjYE30qEYFtmeCJ1G6t.jpg',4),(63,'2021-07-27 10:49:49.570062',1,'snapshots/cTJPQpN2nfK0bhNCm8pW.jpg',6),(64,'2021-07-27 10:49:51.852679',1,'snapshots/nG5lAeU4kOJLvufgtOVM.jpg',4),(65,'2021-07-27 10:49:55.712884',0,'snapshots/FaT4mSq7Kkhd7Cv9b2dy.jpg',NULL),(66,'2021-07-27 10:49:59.268662',1,'snapshots/pic4L2KpucYuQHA1Ef1F.jpg',4),(67,'2021-07-27 10:50:01.464339',1,'snapshots/yWznmS7oN5OdY1yMKWBj.jpg',6),(68,'2021-07-27 10:50:03.198835',1,'snapshots/mCfakK6vo2ATgq73SoJX.jpg',4),(69,'2021-07-27 10:50:05.553379',1,'snapshots/IG0arA24UDWw7bqZzx5L.jpg',4),(70,'2021-07-27 10:50:07.787278',1,'snapshots/vpd5eM4cBiYL36NEcOQq.jpg',4),(71,'2021-07-27 10:50:09.757095',1,'snapshots/Qk48F4ru5EPo2KT4CtPp.jpg',4),(72,'2021-07-27 10:50:11.963294',1,'snapshots/OMdosK9b65GgeZVO4ObR.jpg',4),(73,'2021-07-27 10:50:14.158540',1,'snapshots/nHJIaNQvaunTr4rbYR6q.jpg',6),(74,'2021-07-27 10:50:16.915892',1,'snapshots/e3tkLxhRNMhYWVuQmWYy.jpg',6),(75,'2021-07-27 10:50:19.468759',1,'snapshots/m8hzqJy9uV1d4ouEAFRR.jpg',6),(76,'2021-07-27 10:50:22.717504',1,'snapshots/EU1QeuUKVialbR1z58ds.jpg',4),(77,'2021-07-27 10:50:24.883028',1,'snapshots/HCbS13dbHSy8UMixfLOn.jpg',4),(78,'2021-07-27 10:50:27.091132',1,'snapshots/Bd1NtGfWy1y1qFTCTvQG.jpg',4),(79,'2021-07-27 10:50:29.538659',1,'snapshots/4N6maUMJDwUH0fi8eCUt.jpg',4),(80,'2021-07-27 10:50:31.727537',1,'snapshots/IVEhwYD5AS3bHNk8GBoD.jpg',4),(81,'2021-07-27 10:50:33.690926',1,'snapshots/CfTs95nP0RW4iZghdzjX.jpg',4),(82,'2021-07-27 10:50:34.175717',0,'snapshots/4opw7wPD7J9vHOn4w714.jpg',NULL),(83,'2021-07-27 10:50:36.111607',1,'snapshots/4vhmCvRNYXXIW0i0RR33.jpg',4),(84,'2021-07-27 10:50:38.400023',1,'snapshots/FY4paKPYy5NxKphv9m14.jpg',4),(85,'2021-07-27 10:50:40.532296',1,'snapshots/Foz3AYxCRbLM3PMUuTE7.jpg',4),(86,'2021-07-27 10:50:42.754982',1,'snapshots/7lEYRf2rl2MOxyRnwwke.jpg',6),(87,'2021-07-27 10:50:45.003028',1,'snapshots/Q46uJ7996vmMneS1gi4H.jpg',4),(88,'2021-07-27 10:50:47.028538',1,'snapshots/BvoE1e09MBopNXcTtS7M.jpg',4),(89,'2021-07-27 10:50:49.270118',1,'snapshots/hvOpAhhEt0w4dnxZtM4u.jpg',4),(90,'2021-07-27 10:50:51.572890',1,'snapshots/2dy1XaoE1ug0OyYGTRfD.jpg',4),(91,'2021-07-27 10:50:53.558107',1,'snapshots/KF2W3BbC6FXoDsYMkdY1.jpg',6),(92,'2021-07-27 10:50:55.598610',1,'snapshots/euXgzL0pbhPtq3lqGM0N.jpg',6),(93,'2021-07-27 10:50:57.675259',1,'snapshots/o1UgNRLvUq4Jej2vJDuF.jpg',4),(94,'2021-07-27 10:50:59.747050',1,'snapshots/DEgy1RuD0hLcuskRBMjT.jpg',4),(95,'2021-07-27 10:51:01.810074',1,'snapshots/Kn6dtX0E5hJCj2lW4A9L.jpg',4),(96,'2021-07-27 10:51:03.860196',1,'snapshots/V5XX12lQWN5rutyiUJJm.jpg',6),(97,'2021-07-27 10:51:05.997893',1,'snapshots/pwDgQL29W2OAeeLypJoU.jpg',6),(98,'2021-07-27 10:51:08.151595',1,'snapshots/smSoLmHq3Jy02taspAlu.jpg',6),(99,'2021-07-27 10:51:10.265890',1,'snapshots/6GBVZgY5jmjnyWSICvD5.jpg',4),(100,'2021-07-27 10:51:30.065288',1,'snapshots/cJpx28HLPwoE4msMrcgm.jpg',4),(101,'2021-07-27 10:51:30.372792',0,'snapshots/PmGNXbNqgEtzet8AcotL.jpg',NULL),(102,'2021-07-27 10:51:32.506459',1,'snapshots/UEnpK9fQmuqHWGCAKYw0.jpg',4),(103,'2021-07-27 10:51:34.970502',1,'snapshots/KgxN5UXxrCbOnKMq3CdU.jpg',4),(104,'2021-07-27 10:51:36.986692',1,'snapshots/kvP73yl2EJtLw0jERSQm.jpg',4),(105,'2021-07-27 10:51:39.477509',1,'snapshots/dkiMEHriWfzznZIXHbEy.jpg',6),(106,'2021-07-27 10:51:41.608869',1,'snapshots/dTlEIcj4EFX6Sk3lGDnh.jpg',4),(107,'2021-07-27 10:51:43.658294',1,'snapshots/u43zuwYXjxe0aw3xxgoG.jpg',4),(108,'2021-07-27 10:51:45.727452',1,'snapshots/q5hwI0ea2Ko0u5ZJokfO.jpg',4),(109,'2021-07-27 10:51:47.767169',1,'snapshots/SHwGDprfAJ0VMU7oAF0Q.jpg',4),(110,'2021-07-27 10:54:09.222551',1,'snapshots/HNRgz9mFrNpiLe3QAHQN.jpg',4),(111,'2021-07-27 10:54:11.170569',1,'snapshots/8GHbmqbcCVIGRfoJkmgO.jpg',4),(112,'2021-07-27 10:54:13.133343',1,'snapshots/sgbUgnd1v5lpuHAYqpCa.jpg',4),(113,'2021-07-27 10:54:15.334860',1,'snapshots/Z4fbuq1itvRR9u68Bdzl.jpg',4),(114,'2021-07-27 10:54:17.275508',1,'snapshots/PFA9butJMRzE9FczO9lA.jpg',6),(115,'2021-07-27 10:54:19.312699',1,'snapshots/ulvkNlzX1ElKTqAGUUAH.jpg',4),(116,'2021-07-27 10:54:21.353894',1,'snapshots/vBixuoLWB5bQ1Z5CWGfc.jpg',6),(117,'2021-07-27 10:54:23.440143',1,'snapshots/jS4kCAsah5EoJE6M4EMh.jpg',4),(118,'2021-07-27 10:54:25.502963',1,'snapshots/c50bDUZpjGzuNRJO0Qip.jpg',4),(119,'2021-07-27 10:54:27.646265',1,'snapshots/FicydCt7QPk9Fiy75VF9.jpg',4),(120,'2021-07-27 10:54:29.795230',1,'snapshots/HJzS9sBlP5RLWsX2CaG0.jpg',4),(121,'2021-07-27 10:54:31.905755',1,'snapshots/5NDBAjro56lPk8jSAbef.jpg',4),(122,'2021-07-27 10:54:34.136436',1,'snapshots/V7BaXrDkSEb93Rq3RjvM.jpg',6),(123,'2021-07-27 10:54:36.259944',1,'snapshots/H3ZVMyc2GKXDu5cwlV6w.jpg',4),(124,'2021-07-27 10:54:38.313377',1,'snapshots/tAMHqSa6u9PuQW7hOVSg.jpg',6),(125,'2021-07-27 10:54:40.389237',1,'snapshots/qeebOqpHHWzVFEK1O3EY.jpg',6),(126,'2021-07-27 10:54:42.679147',1,'snapshots/xms9KDYBWAttjCXPJ0Ao.jpg',4),(127,'2021-07-27 10:54:44.712042',1,'snapshots/oHYCvInskDZhPpofoKBx.jpg',4),(128,'2021-07-27 10:54:46.700936',1,'snapshots/bzE0ogCl1uXgaleCQkaa.jpg',4),(129,'2021-07-27 10:54:48.811356',1,'snapshots/8rPCCfBq6O6hQeR488US.jpg',4),(130,'2021-07-27 10:54:51.070046',1,'snapshots/rVpyIdtvTqnVDxRALVhA.jpg',4),(131,'2021-07-27 10:54:52.933962',1,'snapshots/HWx1GNC2GU0n8d3aG21N.jpg',6),(132,'2021-07-27 10:54:55.107555',1,'snapshots/ywdBU8SGpohLO5MoRjQZ.jpg',4),(133,'2021-07-27 10:54:57.153504',1,'snapshots/DvkceXePMgCx5gbxs9pc.jpg',4),(134,'2021-07-27 10:54:59.184949',1,'snapshots/9vAdSQGwoBNLrx5UZocw.jpg',4),(135,'2021-07-27 10:55:01.211800',1,'snapshots/bV7sX4v7nTDlhLaTyGdB.jpg',4),(136,'2021-07-27 10:55:05.400262',1,'snapshots/63jIQeunneZP5gVHzuXu.jpg',4),(137,'2021-07-27 10:55:07.463046',1,'snapshots/B649XtrK8ufJQzsCA9ts.jpg',4),(138,'2021-07-27 10:55:09.487650',1,'snapshots/MGAqloOdVxB3sc5vkpun.jpg',4),(139,'2022-03-21 23:01:38.479140',1,'snapshots/G7GoNDtje8Fb853rurv3.jpg',4),(140,'2022-03-21 23:01:40.311021',1,'snapshots/8z7KSaz08Lw72KxV2R3Y.jpg',4),(141,'2022-03-21 23:01:42.431738',1,'snapshots/Gz0YrZvT2lwozPbySqhu.jpg',4),(142,'2022-03-21 23:02:02.899535',1,'snapshots/Hqst0QMl1GjUiVXVt9ER.jpg',6),(143,'2022-03-21 23:02:05.199555',1,'snapshots/HQUeRu3VxeWs2mklly7r.jpg',4),(144,'2022-03-21 23:02:11.623317',1,'snapshots/hg7htJvzYh3PkYaVFr30.jpg',6),(145,'2022-03-21 23:02:13.627836',1,'snapshots/Nyh2ozn5rDbJsh4tVTxs.jpg',4),(146,'2022-03-21 23:02:46.579030',1,'snapshots/DtvR44BRxTu8DPD6jcap.jpg',4),(147,'2022-03-21 23:03:08.380977',1,'snapshots/AW8GgEM4dzY8mXxiwZ2M.jpg',4),(148,'2022-03-21 23:03:16.078908',1,'snapshots/6QoSOtkdwLp3KjN3cPlp.jpg',4),(149,'2022-03-21 23:03:18.101036',1,'snapshots/Elf9dSduofo0PwkXComB.jpg',4),(150,'2022-03-21 23:03:20.254827',1,'snapshots/h99rnSWLA5ErPiEoxC5z.jpg',4),(151,'2022-03-21 23:03:22.268134',1,'snapshots/DljzjzpNXg12qSSGaEHv.jpg',4),(152,'2022-03-21 23:03:46.632046',1,'snapshots/WIx7y1DrbGOTkN01Nkk5.jpg',4),(153,'2022-03-21 23:03:48.906549',1,'snapshots/arWg6WRoXrntP0mIddzY.jpg',4),(154,'2022-03-21 23:03:50.799254',1,'snapshots/tD7mdODzlAqxRJdKDz3H.jpg',4),(155,'2022-03-21 23:03:54.763129',1,'snapshots/6Zhl3RID76EqyCqvAPEq.jpg',4),(156,'2022-03-21 23:03:56.895878',1,'snapshots/dFly62GrGfIOGbMOXmB8.jpg',6),(157,'2022-03-21 23:04:06.456614',1,'snapshots/JE12YcAWuytjZqTk3Hps.jpg',6),(158,'2022-03-21 23:04:12.325047',1,'snapshots/cWfURtFkPcgRhNuaJwg9.jpg',4);
/*!40000 ALTER TABLE `LiveView_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LiveView_person`
--

DROP TABLE IF EXISTS `LiveView_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LiveView_person` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `authorized` tinyint(1) NOT NULL,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LiveView_person`
--

LOCK TABLES `LiveView_person` WRITE;
/*!40000 ALTER TABLE `LiveView_person` DISABLE KEYS */;
INSERT INTO `LiveView_person` VALUES (1,'Erik1',1,'persons/20200402_183945_6XGbUB5.jpg'),(2,'Kamil1',1,'persons/20200426_120202_zH6hzYK.jpg'),(3,'Timo',0,'persons/timp.png'),(4,'Roman',1,'persons/roman.png'),(5,'Juro',1,'persons/15577343662228817545145394188845.jpg'),(6,'Roman2',1,'persons/15570001650862745937424864594180.jpg'),(7,'RomanIR',1,'persons/1234567890.png'),(8,'Erik2',1,'persons/20200427_121640.jpg'),(9,'Mamina',1,'persons/20200427_115032.jpg'),(10,'Lucka',1,'persons/20200427_114938.jpg'),(11,'Adam',1,'persons/20200427_114923.jpg'),(12,'Mamina2',1,'persons/20200427_114906.jpg'),(13,'Mamina3',1,'persons/20200427_114827.jpg'),(14,'Vanes',1,'persons/20200427_114429_EptKEzj.jpg'),(15,'Kamil2',1,'persons/20200426_120206.jpg'),(16,'Erik',1,'persons/20200427_114252.jpg'),(17,'Simka',1,'persons/20200427_153840.jpg'),(18,'Matik',1,'persons/20200427_115928.jpg'),(19,'Basa',1,'persons/20200427_115525.jpg'),(21,'Matik2',1,'persons/20210708_083019.jpg');
/*!40000 ALTER TABLE `LiveView_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LiveView_setting`
--

DROP TABLE IF EXISTS `LiveView_setting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LiveView_setting` (
  `id` int NOT NULL AUTO_INCREMENT,
  `device` varchar(255) NOT NULL,
  `crop` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LiveView_setting`
--

LOCK TABLES `LiveView_setting` WRITE;
/*!40000 ALTER TABLE `LiveView_setting` DISABLE KEYS */;
INSERT INTO `LiveView_setting` VALUES (1,'http://192.168.3.62:8080/video','0.35');
/*!40000 ALTER TABLE `LiveView_setting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LiveView_subscriber`
--

DROP TABLE IF EXISTS `LiveView_subscriber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LiveView_subscriber` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subscription` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `LiveView_subscriber_user_id_2c556643_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LiveView_subscriber`
--

LOCK TABLES `LiveView_subscriber` WRITE;
/*!40000 ALTER TABLE `LiveView_subscriber` DISABLE KEYS */;
INSERT INTO `LiveView_subscriber` VALUES (1,1,1),(2,0,2);
/*!40000 ALTER TABLE `LiveView_subscriber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add person',1,'add_person'),(2,'Can change person',1,'change_person'),(3,'Can delete person',1,'delete_person'),(4,'Can view person',1,'view_person'),(5,'Can add setting',2,'add_setting'),(6,'Can change setting',2,'change_setting'),(7,'Can delete setting',2,'delete_setting'),(8,'Can view setting',2,'view_setting'),(9,'Can add subscriber',3,'add_subscriber'),(10,'Can change subscriber',3,'change_subscriber'),(11,'Can delete subscriber',3,'delete_subscriber'),(12,'Can view subscriber',3,'view_subscriber'),(13,'Can add log',4,'add_log'),(14,'Can change log',4,'change_log'),(15,'Can delete log',4,'delete_log'),(16,'Can view log',4,'view_log'),(17,'Can add log entry',5,'add_logentry'),(18,'Can change log entry',5,'change_logentry'),(19,'Can delete log entry',5,'delete_logentry'),(20,'Can view log entry',5,'view_logentry'),(21,'Can add permission',6,'add_permission'),(22,'Can change permission',6,'change_permission'),(23,'Can delete permission',6,'delete_permission'),(24,'Can view permission',6,'view_permission'),(25,'Can add group',7,'add_group'),(26,'Can change group',7,'change_group'),(27,'Can delete group',7,'delete_group'),(28,'Can view group',7,'view_group'),(29,'Can add user',8,'add_user'),(30,'Can change user',8,'change_user'),(31,'Can delete user',8,'delete_user'),(32,'Can view user',8,'view_user'),(33,'Can add content type',9,'add_contenttype'),(34,'Can change content type',9,'change_contenttype'),(35,'Can delete content type',9,'delete_contenttype'),(36,'Can view content type',9,'view_contenttype'),(37,'Can add session',10,'add_session'),(38,'Can change session',10,'change_session'),(39,'Can delete session',10,'delete_session'),(40,'Can view session',10,'view_session'),(41,'Can add group',11,'add_group'),(42,'Can change group',11,'change_group'),(43,'Can delete group',11,'delete_group'),(44,'Can view group',11,'view_group'),(45,'Can add push information',12,'add_pushinformation'),(46,'Can change push information',12,'change_pushinformation'),(47,'Can delete push information',12,'delete_pushinformation'),(48,'Can view push information',12,'view_pushinformation'),(49,'Can add subscription info',13,'add_subscriptioninfo'),(50,'Can change subscription info',13,'change_subscriptioninfo'),(51,'Can delete subscription info',13,'delete_subscriptioninfo'),(52,'Can view subscription info',13,'view_subscriptioninfo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$8m3tAT9R01Lh$jeeB8tVE3ane2YfDdI5hZTEUpMEVWzefAJw6zKf/KUw=','2022-03-21 23:00:20.151041',1,'roman','','','roman.mariancik@gmail.com',1,1,'2020-07-27 21:39:11.000000'),(2,'pbkdf2_sha256$180000$rumHUZpQ08Rp$d5vp+lOV11PZCJJMPiOh7q3PzCmSazVlgG25qwqmCa0=','2021-07-27 10:08:06.990579',1,'admin','','','roman.mariancik@gmail.com',1,1,'2020-07-27 21:39:30.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-07-27 21:42:33.525920','1','device and crop',1,'[{\"added\": {}}]',2,1),(2,'2020-07-27 21:46:11.517280','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Device\"]}}]',2,1),(3,'2020-07-27 21:47:55.164835','1','Erik1',1,'[{\"added\": {}}]',1,1),(4,'2020-07-27 21:48:37.933915','2','Kamil1',1,'[{\"added\": {}}]',1,1),(5,'2020-07-27 21:49:30.121420','3','Timo',1,'[{\"added\": {}}]',1,1),(6,'2020-07-27 21:49:38.866062','4','Roman',1,'[{\"added\": {}}]',1,1),(7,'2020-07-27 21:49:46.745322','5','Juro',1,'[{\"added\": {}}]',1,1),(8,'2020-07-27 21:49:56.833692','6','Roman2',1,'[{\"added\": {}}]',1,1),(9,'2020-07-27 21:50:07.072184','7','RomanIR',1,'[{\"added\": {}}]',1,1),(10,'2020-07-27 21:50:17.141701','8','Erik2',1,'[{\"added\": {}}]',1,1),(11,'2020-07-27 21:50:31.001609','9','Mamina',1,'[{\"added\": {}}]',1,1),(12,'2020-07-27 21:50:41.656905','10','Lucka',1,'[{\"added\": {}}]',1,1),(13,'2020-07-27 21:50:57.254699','11','Adam',1,'[{\"added\": {}}]',1,1),(14,'2020-07-27 21:51:06.338452','12','Mamina2',1,'[{\"added\": {}}]',1,1),(15,'2020-07-27 21:51:14.964934','13','Mamina3',1,'[{\"added\": {}}]',1,1),(16,'2020-07-27 21:51:23.114845','14','Vanes',1,'[{\"added\": {}}]',1,1),(17,'2020-07-27 21:51:33.968718','15','Kamil2',1,'[{\"added\": {}}]',1,1),(18,'2020-07-27 21:51:42.920926','16','Erik',1,'[{\"added\": {}}]',1,1),(19,'2020-07-27 21:51:57.144888','17','Simka',1,'[{\"added\": {}}]',1,1),(20,'2020-07-27 21:52:10.480776','18','Mata',1,'[{\"added\": {}}]',1,1),(21,'2020-07-27 21:52:17.652473','19','Basa',1,'[{\"added\": {}}]',1,1),(22,'2020-07-27 21:52:32.544396','20','Lucka2',1,'[{\"added\": {}}]',1,1),(23,'2020-07-27 22:12:08.346388','1','roman',2,'[{\"added\": {\"name\": \"subscriber\", \"object\": \"will receive ring notifications, if checked.\"}}]',8,2),(24,'2020-07-27 22:12:13.774995','2','admin',2,'[{\"added\": {\"name\": \"subscriber\", \"object\": \"will receive ring notifications, if checked.\"}}]',8,2),(25,'2020-07-31 14:53:36.149997','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,2),(26,'2020-07-31 14:54:10.195762','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,2),(27,'2020-08-02 10:13:30.062919','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,2),(28,'2020-08-02 10:13:55.093167','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,2),(29,'2020-08-02 10:14:20.777489','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,2),(30,'2020-09-25 05:41:25.879538','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Device\", \"Crop\"]}}]',2,1),(31,'2020-10-10 12:13:29.174647','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Device\"]}}]',2,2),(32,'2020-10-10 12:14:43.371030','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,2),(33,'2020-10-25 09:43:20.504424','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Device\"]}}]',2,1),(34,'2021-02-13 18:21:25.886212','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Device\", \"Crop\"]}}]',2,1),(35,'2021-02-13 18:22:32.983259','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,1),(36,'2021-02-13 18:23:50.824608','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Device\", \"Crop\"]}}]',2,1),(37,'2021-02-13 18:24:53.964450','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,1),(38,'2021-02-13 18:51:46.776782','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,1),(39,'2021-02-13 18:52:20.833723','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,1),(40,'2021-02-13 19:04:44.075521','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Device\"]}}]',2,1),(41,'2021-02-27 13:48:11.843124','1','device and crop',2,'[]',2,1),(42,'2021-02-27 13:50:13.058923','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Device\"]}}]',2,1),(43,'2021-04-26 09:41:56.195334','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Device\", \"Crop\"]}}]',2,1),(44,'2021-04-27 09:05:20.133878','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Device\"]}}]',2,1),(45,'2021-07-27 10:09:34.287849','1','device and crop',2,'[]',2,2),(46,'2021-07-27 10:10:34.348529','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,2),(47,'2021-07-27 10:13:23.536706','20','Lucka2',3,'',1,2),(48,'2021-07-27 10:14:58.569777','21','Matik2',1,'[{\"added\": {}}]',1,2),(49,'2021-07-27 10:15:03.752067','18','Matik',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',1,2),(50,'2021-07-27 10:16:03.586212','1','device and crop',2,'[]',2,2),(51,'2021-07-27 10:17:15.474750','54','Roman',3,'',4,2),(52,'2021-07-27 10:17:15.683462','53','Roman',3,'',4,2),(53,'2021-07-27 10:17:15.686150','52','Roman',3,'',4,2),(54,'2021-07-27 10:17:15.689514','51','Roman',3,'',4,2),(55,'2021-07-27 10:17:15.692924','50','Roman',3,'',4,2),(56,'2021-07-27 10:17:15.900247','49','Roman',3,'',4,2),(57,'2021-07-27 10:17:15.903032','48','Roman',3,'',4,2),(58,'2021-07-27 10:17:15.906673','47','Roman2',3,'',4,2),(59,'2021-07-27 10:17:15.910133','46','Roman',3,'',4,2),(60,'2021-07-27 10:17:15.913363','45','unknown',3,'',4,2),(61,'2021-07-27 10:17:16.120415','44','Roman',3,'',4,2),(62,'2021-07-27 10:17:16.123614','43','Roman',3,'',4,2),(63,'2021-07-27 10:17:16.126132','42','unknown',3,'',4,2),(64,'2021-07-27 10:17:16.128771','41','Roman',3,'',4,2),(65,'2021-07-27 10:17:16.337962','40','Roman2',3,'',4,2),(66,'2021-07-27 10:17:16.340813','39','Roman',3,'',4,2),(67,'2021-07-27 10:17:16.343273','38','Roman',3,'',4,2),(68,'2021-07-27 10:17:16.345354','37','Roman',3,'',4,2),(69,'2021-07-27 10:17:16.348829','36','unknown',3,'',4,2),(70,'2021-07-27 10:17:16.351485','35','unknown',3,'',4,2),(71,'2021-07-27 10:17:16.560035','34','RomanIR',3,'',4,2),(72,'2021-07-27 10:17:16.563609','33','Roman',3,'',4,2),(73,'2021-07-27 10:17:16.566190','32','Roman',3,'',4,2),(74,'2021-07-27 10:17:16.568531','31','Roman2',3,'',4,2),(75,'2021-07-27 10:17:16.778908','30','Roman',3,'',4,2),(76,'2021-07-27 10:17:16.783453','29','Roman2',3,'',4,2),(77,'2021-07-27 10:17:16.785500','28','Roman2',3,'',4,2),(78,'2021-07-27 10:17:16.787596','27','Roman2',3,'',4,2),(79,'2021-07-27 10:17:16.997434','26','Roman2',3,'',4,2),(80,'2021-07-27 10:17:17.009224','25','Roman2',3,'',4,2),(81,'2021-07-27 10:17:17.219127','24','Roman2',3,'',4,2),(82,'2021-07-27 10:17:17.223593','23','Roman2',3,'',4,2),(83,'2021-07-27 10:17:17.226016','22','Roman2',3,'',4,2),(84,'2021-07-27 10:17:17.228019','21','Roman2',3,'',4,2),(85,'2021-07-27 10:17:17.230361','20','Roman2',3,'',4,2),(86,'2021-07-27 10:17:17.233292','19','Roman2',3,'',4,2),(87,'2021-07-27 10:17:17.236036','18','Roman2',3,'',4,2),(88,'2021-07-27 10:17:17.240513','17','Roman2',3,'',4,2),(89,'2021-07-27 10:17:17.243535','16','Roman2',3,'',4,2),(90,'2021-07-27 10:17:17.457820','15','Roman2',3,'',4,2),(91,'2021-07-27 10:17:17.460931','14','Roman',3,'',4,2),(92,'2021-07-27 10:17:17.463714','13','Roman2',3,'',4,2),(93,'2021-07-27 10:17:17.466340','12','Roman',3,'',4,2),(94,'2021-07-27 10:17:17.469660','11','Roman',3,'',4,2),(95,'2021-07-27 10:17:17.680379','10','Roman',3,'',4,2),(96,'2021-07-27 10:17:17.685449','9','Roman',3,'',4,2),(97,'2021-07-27 10:17:17.688621','8','Roman',3,'',4,2),(98,'2021-07-27 10:17:17.902088','7','Roman',3,'',4,2),(99,'2021-07-27 10:17:17.907368','6','Roman',3,'',4,2),(100,'2021-07-27 10:17:17.910615','5','unknown',3,'',4,2),(101,'2021-07-27 10:17:17.913428','4','Roman',3,'',4,2),(102,'2021-07-27 10:17:17.917532','3','Roman',3,'',4,2),(103,'2021-07-27 10:17:17.920106','2','RomanIR',3,'',4,2),(104,'2021-07-27 10:17:18.134744','1','Timo',3,'',4,2),(105,'2021-07-27 10:50:49.273810','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,2),(106,'2022-03-21 23:01:55.304836','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,1),(107,'2022-03-21 23:03:00.340406','1','device and crop',2,'[{\"changed\": {\"fields\": [\"Crop\"]}}]',2,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (5,'admin','logentry'),(7,'auth','group'),(6,'auth','permission'),(8,'auth','user'),(9,'contenttypes','contenttype'),(4,'FaceRecognition','log'),(1,'FaceRecognition','person'),(2,'FaceRecognition','setting'),(3,'FaceRecognition','subscriber'),(10,'sessions','session'),(11,'webpush','group'),(12,'webpush','pushinformation'),(13,'webpush','subscriptioninfo');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-07-27 21:32:35.747894'),(2,'auth','0001_initial','2020-07-27 21:32:35.912661'),(3,'FaceRecognition','0001_initial','2020-07-27 21:32:36.459731'),(4,'admin','0001_initial','2020-07-27 21:32:36.585877'),(5,'admin','0002_logentry_remove_auto_add','2020-07-27 21:32:36.699365'),(6,'admin','0003_logentry_add_action_flag_choices','2020-07-27 21:32:36.713052'),(7,'contenttypes','0002_remove_content_type_name','2020-07-27 21:32:36.846885'),(8,'auth','0002_alter_permission_name_max_length','2020-07-27 21:32:36.909189'),(9,'auth','0003_alter_user_email_max_length','2020-07-27 21:32:36.965401'),(10,'auth','0004_alter_user_username_opts','2020-07-27 21:32:36.978370'),(11,'auth','0005_alter_user_last_login_null','2020-07-27 21:32:37.036253'),(12,'auth','0006_require_contenttypes_0002','2020-07-27 21:32:37.040091'),(13,'auth','0007_alter_validators_add_error_messages','2020-07-27 21:32:37.060209'),(14,'auth','0008_alter_user_username_max_length','2020-07-27 21:32:37.149649'),(15,'auth','0009_alter_user_last_name_max_length','2020-07-27 21:32:37.222455'),(16,'auth','0010_alter_group_name_max_length','2020-07-27 21:32:37.263458'),(17,'auth','0011_update_proxy_permissions','2020-07-27 21:32:37.285006'),(18,'sessions','0001_initial','2020-07-27 21:32:37.324296'),(19,'webpush','0001_initial','2020-07-27 21:32:37.485254'),(20,'webpush','0002_auto_20190603_0005','2020-07-27 21:32:37.545922'),(21,'FaceRecognition','0002_auto_20200727_2344','2020-07-27 21:44:28.867525');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('01rqi0e5u3tpyxdoqhh9ib13f4n9iwu6','MTE0ZGIxMzYwYmNlOGY0MWJmYzFlODI0ZWRjOWI1NzFjMGIzZWQ3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmN2M4YjliYzczZDcwMmVjZDZiMDE5ZDg4MGJhNjFkYTQ5OTU0ZGZkIn0=','2021-02-27 18:20:54.718206'),('3aehbogdxcthyuv0557snnvrkrmn9t6i','MTE0ZGIxMzYwYmNlOGY0MWJmYzFlODI0ZWRjOWI1NzFjMGIzZWQ3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmN2M4YjliYzczZDcwMmVjZDZiMDE5ZDg4MGJhNjFkYTQ5OTU0ZGZkIn0=','2020-11-08 09:42:42.471236'),('3wp7n4y3emlm3rcnrou8pgzyrn2xokrj','MTE0ZGIxMzYwYmNlOGY0MWJmYzFlODI0ZWRjOWI1NzFjMGIzZWQ3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmN2M4YjliYzczZDcwMmVjZDZiMDE5ZDg4MGJhNjFkYTQ5OTU0ZGZkIn0=','2021-09-04 09:35:40.736153'),('6rp8rg51ye8lly0qurw77hngj8asl087','MTE0ZGIxMzYwYmNlOGY0MWJmYzFlODI0ZWRjOWI1NzFjMGIzZWQ3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmN2M4YjliYzczZDcwMmVjZDZiMDE5ZDg4MGJhNjFkYTQ5OTU0ZGZkIn0=','2020-08-10 21:39:40.605428'),('db94yehiau2pqw4nhmb1dya4sguwf7wp','MTE0ZGIxMzYwYmNlOGY0MWJmYzFlODI0ZWRjOWI1NzFjMGIzZWQ3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmN2M4YjliYzczZDcwMmVjZDZiMDE5ZDg4MGJhNjFkYTQ5OTU0ZGZkIn0=','2021-02-27 18:09:22.277647'),('dcv5rnk7j9kxmf367stnoisu2z0aupnb','MTE0ZGIxMzYwYmNlOGY0MWJmYzFlODI0ZWRjOWI1NzFjMGIzZWQ3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmN2M4YjliYzczZDcwMmVjZDZiMDE5ZDg4MGJhNjFkYTQ5OTU0ZGZkIn0=','2021-05-10 09:29:52.774278'),('eao9fgrf0o1txvqvtl1wpsfj5havrq4z','MTE0ZGIxMzYwYmNlOGY0MWJmYzFlODI0ZWRjOWI1NzFjMGIzZWQ3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmN2M4YjliYzczZDcwMmVjZDZiMDE5ZDg4MGJhNjFkYTQ5OTU0ZGZkIn0=','2022-04-04 23:00:20.159370'),('hddiweyzzjj12zrsopf017oubsz0bncy','MTE0ZGIxMzYwYmNlOGY0MWJmYzFlODI0ZWRjOWI1NzFjMGIzZWQ3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmN2M4YjliYzczZDcwMmVjZDZiMDE5ZDg4MGJhNjFkYTQ5OTU0ZGZkIn0=','2021-02-27 18:50:50.838848'),('htyqxtlcqo7sd8a5lv1t0rbq8enrczbd','MTE0ZGIxMzYwYmNlOGY0MWJmYzFlODI0ZWRjOWI1NzFjMGIzZWQ3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmN2M4YjliYzczZDcwMmVjZDZiMDE5ZDg4MGJhNjFkYTQ5OTU0ZGZkIn0=','2020-09-29 11:19:27.028998'),('kajp3w3a3kvdbaltge5rjsx7udxo842y','YzUzMDI5ODRlMjhhM2M2MGIyZjBiOThkNGJhMWUxNGNjNWE5YTQwNTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTQ1NmM0ZjZjNGU0M2RiNTMxY2QwZGNlNDFhOTY1ZDAzMGM1NmUyIn0=','2021-08-10 10:08:06.994748'),('w4k5v95q155ze4li8e36l7q1y06sz591','YzUzMDI5ODRlMjhhM2M2MGIyZjBiOThkNGJhMWUxNGNjNWE5YTQwNTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTQ1NmM0ZjZjNGU0M2RiNTMxY2QwZGNlNDFhOTY1ZDAzMGM1NmUyIn0=','2020-08-10 22:03:02.161121'),('wbwg4dqrf2641fexyuqv7jvidi2cu0t4','YzUzMDI5ODRlMjhhM2M2MGIyZjBiOThkNGJhMWUxNGNjNWE5YTQwNTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTQ1NmM0ZjZjNGU0M2RiNTMxY2QwZGNlNDFhOTY1ZDAzMGM1NmUyIn0=','2020-10-24 12:13:10.900651'),('yv2fi8fg1oh2v126jq4lwp7h08uyjv9l','MTE0ZGIxMzYwYmNlOGY0MWJmYzFlODI0ZWRjOWI1NzFjMGIzZWQ3ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmN2M4YjliYzczZDcwMmVjZDZiMDE5ZDg4MGJhNjFkYTQ5OTU0ZGZkIn0=','2020-10-09 05:40:56.591546');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webpush_group`
--

DROP TABLE IF EXISTS `webpush_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `webpush_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webpush_group`
--

LOCK TABLES `webpush_group` WRITE;
/*!40000 ALTER TABLE `webpush_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `webpush_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webpush_pushinformation`
--

DROP TABLE IF EXISTS `webpush_pushinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `webpush_pushinformation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int DEFAULT NULL,
  `subscription_id` int NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `webpush_pushinformat_subscription_id_7989aa34_fk_webpush_s` (`subscription_id`),
  KEY `webpush_pushinformation_user_id_5e083b7f_fk_auth_user_id` (`user_id`),
  KEY `webpush_pushinformation_group_id_262dcc9a_fk_webpush_group_id` (`group_id`),
  CONSTRAINT `webpush_pushinformat_subscription_id_7989aa34_fk_webpush_s` FOREIGN KEY (`subscription_id`) REFERENCES `webpush_subscriptioninfo` (`id`),
  CONSTRAINT `webpush_pushinformation_group_id_262dcc9a_fk_webpush_group_id` FOREIGN KEY (`group_id`) REFERENCES `webpush_group` (`id`),
  CONSTRAINT `webpush_pushinformation_user_id_5e083b7f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webpush_pushinformation`
--

LOCK TABLES `webpush_pushinformation` WRITE;
/*!40000 ALTER TABLE `webpush_pushinformation` DISABLE KEYS */;
/*!40000 ALTER TABLE `webpush_pushinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webpush_subscriptioninfo`
--

DROP TABLE IF EXISTS `webpush_subscriptioninfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `webpush_subscriptioninfo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `browser` varchar(100) NOT NULL,
  `endpoint` varchar(500) NOT NULL,
  `auth` varchar(100) NOT NULL,
  `p256dh` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webpush_subscriptioninfo`
--

LOCK TABLES `webpush_subscriptioninfo` WRITE;
/*!40000 ALTER TABLE `webpush_subscriptioninfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `webpush_subscriptioninfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-31 22:43:20
