-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: Lumo
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.24.04.1

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('67c85f0ec8ad');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amenities`
--

DROP TABLE IF EXISTS `amenities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amenities` (
  `name` varchar(32) NOT NULL,
  `amount` int NOT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amenities`
--

LOCK TABLES `amenities` WRITE;
/*!40000 ALTER TABLE `amenities` DISABLE KEYS */;
INSERT INTO `amenities` VALUES ('Swimming Pool',1,'124a8cd6-6516-4f35-8819-b457ba336e75','2025-01-05 19:49:14','2025-01-05 19:49:14'),('Backup Generator',1,'1d97d186-8020-46a3-81e9-a139b82b5729','2025-01-05 19:56:55','2025-01-05 20:03:35'),('Parking Space',1,'3131c735-fb0e-495e-bb73-e08d110a1319','2025-01-05 19:50:18','2025-01-05 19:50:18'),('Garden',1,'6180b61c-c0cd-46db-90db-b341f095d38e','2025-01-05 19:52:02','2025-01-05 19:52:02'),('Gym',1,'8062f6ae-5608-4f52-a2f6-223be73655ea','2025-01-05 19:49:54','2025-01-05 19:49:54'),('Air Conditioning',1,'9aba2d3f-5927-4967-8f91-579ae391d324','2025-01-05 19:51:10','2025-01-05 19:51:10'),('Wi-Fi',1,'a6b79c2a-8f49-4b70-9cb3-11bf7cf1dff5','2025-01-05 19:50:38','2025-01-05 19:50:38'),('Balcony',1,'cb4a8495-8867-4b94-bf72-1cbe1374e2d1','2025-01-05 19:51:42','2025-01-05 19:51:42'),('Furnished',1,'d0d7ef22-8742-4e18-9205-e9b16992bffa','2025-01-05 19:51:26','2025-01-05 19:51:26'),('Playground',1,'eb04e3f3-7c52-444b-bd4a-2b53695b9ec2','2025-01-05 19:52:36','2025-01-05 19:52:36'),('Security System',1,'f389f874-c6af-49e9-8499-191d34ca6217','2025-01-05 19:52:21','2025-01-05 19:52:21');
/*!40000 ALTER TABLE `amenities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `areas`
--

DROP TABLE IF EXISTS `areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `areas` (
  `name` varchar(60) NOT NULL,
  `region_id` varchar(64) DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `region_id` (`region_id`),
  CONSTRAINT `areas_ibfk_1` FOREIGN KEY (`region_id`) REFERENCES `regions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `areas`
--

LOCK TABLES `areas` WRITE;
/*!40000 ALTER TABLE `areas` DISABLE KEYS */;
INSERT INTO `areas` VALUES ('Ndungu Kebbe','33bc6cf7-bd30-41a0-8102-84fd3b8c5c27','02077ab8-cae9-4e01-b262-f526df39dd8c','2025-01-09 11:37:34','2025-01-09 11:37:34'),('Sanyang Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','16f4ac3f-dcab-47f1-a117-d1c002322bff','2025-01-09 11:34:07','2025-01-09 11:34:07'),('Yundum Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','1f3d0aad-0a13-4ae5-a244-746ef6831e40','2025-01-05 14:01:25','2025-01-05 14:01:25'),('Brikama Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','2cf55223-de65-4f79-89d8-265268efa606','2025-01-05 12:14:58','2025-01-05 12:14:58'),('Kotu Area','9febe65c-4694-4d93-b63a-e77ee1085b43','373132ab-05c0-4223-9f6f-97615c2e111c','2025-01-09 11:50:55','2025-01-09 11:50:55'),('Kanifing','9febe65c-4694-4d93-b63a-e77ee1085b43','5303bb3b-385e-49da-9c54-9b72b894d406','2025-01-09 11:24:47','2025-01-09 11:24:47'),('Banjul Area','2fa2eb1d-0b46-4937-9aaf-a6f941dccabf','541c2349-53e2-4617-81e3-1f3add2763c5','2025-01-09 11:23:05','2025-01-09 11:23:05'),('Somita Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','547a594e-f296-4911-8ec6-610a587a6fad','2025-01-09 11:38:52','2025-01-09 11:38:52'),('Turntable Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','56c24f84-5f68-43a5-8015-ab0c914f9df1','2025-01-09 11:49:29','2025-01-09 11:49:29'),('Gunjur Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','588ec62c-d897-465a-b145-e1bb33f96fa3','2025-01-09 11:00:12','2025-01-09 11:00:12'),('Amdallai','33bc6cf7-bd30-41a0-8102-84fd3b8c5c27','79a6908c-0256-4f97-b5db-54d89b841e03','2025-01-09 11:38:06','2025-01-09 11:38:06'),('Kafuta Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','8103d285-5d82-48ee-b125-006f1b66bd1e','2025-01-09 11:36:08','2025-01-09 11:36:08'),('Albadarr','33bc6cf7-bd30-41a0-8102-84fd3b8c5c27','8bd7d404-60c0-4be8-aae9-625ef2a2efb7','2025-01-09 11:37:12','2025-01-09 11:37:12'),('Bakau Area','9febe65c-4694-4d93-b63a-e77ee1085b43','a82ad975-6bda-41a2-8531-f45bbc5fc606','2025-01-09 10:30:54','2025-01-09 10:30:54'),('Faraba Banta Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','b59100f5-b21f-44a0-b740-135a1957e37e','2025-01-09 11:35:47','2025-01-09 11:35:47'),('Brufut Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','bed5efff-c8ca-4895-b98f-1f48686fdb19','2025-01-09 11:34:35','2025-01-09 11:34:35'),('Kerewan Area','33bc6cf7-bd30-41a0-8102-84fd3b8c5c27','dc3c0818-373b-4d15-afd5-0e15a7a4d6df','2025-01-09 11:38:19','2025-01-09 11:38:19'),('Kartong Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','dd71e515-2fd3-45ae-8b07-c1880e369037','2025-01-09 11:33:50','2025-01-09 11:33:50'),('Sukuta Area','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','e3b833a5-3986-409f-af55-fc48971984cd','2025-01-09 11:34:48','2025-01-09 11:34:48'),('Serrekunda','9febe65c-4694-4d93-b63a-e77ee1085b43','eb28404d-e05f-4608-99db-0019465d0048','2025-01-09 11:35:16','2025-01-09 11:35:16'),('Essau Area','33bc6cf7-bd30-41a0-8102-84fd3b8c5c27','f33e9243-5b02-4b6f-8945-c35fd87ce4e6','2025-01-09 11:36:31','2025-01-09 11:36:31');
/*!40000 ALTER TABLE `areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blocked_tokens`
--

DROP TABLE IF EXISTS `blocked_tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blocked_tokens` (
  `jti` varchar(60) NOT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blocked_tokens`
--

LOCK TABLES `blocked_tokens` WRITE;
/*!40000 ALTER TABLE `blocked_tokens` DISABLE KEYS */;
INSERT INTO `blocked_tokens` VALUES ('8f742456-d6bd-4647-8e5d-744e4d120a8e','0378d13d-34c1-403f-9fd7-6820e9affbd4','2025-01-04 22:36:54','2025-01-04 22:36:54'),('37476ad9-b74b-472e-b11a-173b0766f393','3e6cec64-30ee-4c73-9aad-68021c5bb756','2025-01-10 21:23:01','2025-01-10 21:23:01'),('8f742456-d6bd-4647-8e5d-744e4d120a8e','51d0e12f-e645-41c6-9838-f9ed1c8c2a24','2025-01-04 21:46:40','2025-01-04 21:46:40'),('72c3663a-0e99-4142-a004-2f3cc651d2c7','5a65e1b9-32bf-460c-9626-ffd467ab9ef8','2025-01-10 16:21:27','2025-01-10 16:21:27'),('78b6230a-991b-4970-97f5-0086566b2802','8da831b2-91fe-4fdc-a979-3371f9508f59','2025-01-10 21:32:15','2025-01-10 21:32:15'),('edd120bd-50a0-4764-ba2f-9fecc34541f0','98060bc8-7772-4d16-890c-ebaba87354d7','2025-01-05 01:18:27','2025-01-05 01:18:27'),('7b6cbeee-2d80-4132-ba31-eaf0413b0218','9e56bb1e-851a-42d6-9ef2-e6061f9226e6','2025-01-10 21:29:32','2025-01-10 21:29:32'),('e962f0f1-be0e-4a35-9a83-e24d97a748f0','bdc381e3-5966-4100-b393-f58e58914a9d','2025-01-05 00:27:48','2025-01-05 00:27:48'),('65d258cc-0045-4e0b-8515-45d57d7ee677','bfc19bc8-88a6-4758-b894-81d310fbd4cd','2025-01-10 21:19:18','2025-01-10 21:19:18'),('980a8721-fd9f-4000-984a-d9ec71b10dfe','ca360160-fbb8-498f-aa86-06776d50bd8a','2025-01-04 22:58:07','2025-01-04 22:58:07'),('8b7ecc4d-ceae-4b71-8f5b-d19699a2c5e3','cfbb0aba-e036-4286-86a4-b17ed1c7950c','2025-01-05 01:03:06','2025-01-05 01:03:06'),('98516d9e-9583-47fa-8d2c-7e3677e65e82','fa101750-5362-417f-8cbc-9139dc2b77e6','2025-01-10 21:23:31','2025-01-10 21:23:31');
/*!40000 ALTER TABLE `blocked_tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `name` varchar(60) NOT NULL,
  `area_id` varchar(64) DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `area_id` (`area_id`),
  CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES ('Sifo','588ec62c-d897-465a-b145-e1bb33f96fa3','0f533559-2e1a-4c9e-9767-faef2a6ea4c3','2025-01-09 11:40:06','2025-01-09 11:40:06'),('Kasa Kunda','2cf55223-de65-4f79-89d8-265268efa606','10af9820-a610-423f-bce4-5977b167d189','2025-01-09 11:42:37','2025-01-09 11:42:37'),('Kotu','373132ab-05c0-4223-9f6f-97615c2e111c','1351eb04-faaf-461c-ba95-ad26538f8bc0','2025-01-09 11:51:25','2025-01-09 11:51:25'),('Sanyang','16f4ac3f-dcab-47f1-a117-d1c002322bff','15073e03-64fd-440f-bf6e-3a6dcfac8fab','2025-01-09 11:46:01','2025-01-09 11:46:01'),('Gunjurr Kunkujang','588ec62c-d897-465a-b145-e1bb33f96fa3','1a682c6a-74a2-4379-95d8-95f2c836e09b','2025-01-09 11:43:12','2025-01-09 11:43:12'),('Tujereng','bed5efff-c8ca-4895-b98f-1f48686fdb19','2207832f-ec22-44c9-a365-2f434e083b03','2025-01-09 11:47:39','2025-01-09 11:47:39'),('Jambanjelly','16f4ac3f-dcab-47f1-a117-d1c002322bff','23d93613-8e5d-43a4-b65b-472ff1db231f','2025-01-09 11:45:47','2025-01-09 11:45:47'),('Hawa Ba','16f4ac3f-dcab-47f1-a117-d1c002322bff','2432bea1-a49c-4079-8909-8bc5117ed694','2025-01-09 11:46:14','2025-01-09 11:46:14'),('Kanifing Estate','5303bb3b-385e-49da-9c54-9b72b894d406','2461319a-3ef2-4c6b-b262-970687dcf36d','2025-01-09 11:25:22','2025-01-09 11:25:22'),('Kololi','373132ab-05c0-4223-9f6f-97615c2e111c','25f3b09d-35b7-4113-8674-e022ce5422e9','2025-01-09 11:51:18','2025-01-09 11:51:18'),('Yundum','1f3d0aad-0a13-4ae5-a244-746ef6831e40','28fbada9-323d-4ec7-b8c8-868ac160044c','2025-01-09 10:28:52','2025-01-09 10:28:52'),('Kanifing South','5303bb3b-385e-49da-9c54-9b72b894d406','2e407c1d-3969-4fec-b6ec-8d9b1d83c485','2025-01-09 11:25:02','2025-01-09 11:25:02'),('Old Yundum','1f3d0aad-0a13-4ae5-a244-746ef6831e40','3731fd29-d6dc-47e0-831d-4a18d7b1ffda','2025-01-09 11:48:18','2025-01-09 11:48:18'),('Senegambia','373132ab-05c0-4223-9f6f-97615c2e111c','3c8f09e7-d304-4888-a141-e71a2e2d0962','2025-01-09 17:58:02','2025-01-09 17:58:02'),('Busura','2cf55223-de65-4f79-89d8-265268efa606','4b16c3fe-42ab-473d-ac68-9b5186459526','2025-01-09 11:41:23','2025-01-09 11:41:23'),('Dimbaya','2cf55223-de65-4f79-89d8-265268efa606','4bedcae3-b48b-4273-9f4c-14d46972c78d','2025-01-09 11:41:58','2025-01-09 11:41:58'),('Yaranbamba','1f3d0aad-0a13-4ae5-a244-746ef6831e40','51da2d9a-e399-4083-9513-1513581dd0ff','2025-01-05 14:12:02','2025-01-05 14:12:02'),('Tintinto','bed5efff-c8ca-4895-b98f-1f48686fdb19','555a7c88-065a-465d-8344-0fe686d6bda6','2025-01-09 11:47:14','2025-01-09 11:47:14'),('Sukuta','e3b833a5-3986-409f-af55-fc48971984cd','5de545ba-d4a4-4e4f-996d-e008de34d24f','2025-01-09 11:48:35','2025-01-09 11:48:35'),('Sambouya Amanson','588ec62c-d897-465a-b145-e1bb33f96fa3','60b1399a-b652-4160-8126-b753c4d5790d','2025-01-09 11:43:42','2025-01-09 11:43:42'),('Kerr Serign','373132ab-05c0-4223-9f6f-97615c2e111c','642a6a69-27df-4567-ad65-e7fbd8c0a48f','2025-01-09 11:51:06','2025-01-09 11:51:06'),('Jabang','e3b833a5-3986-409f-af55-fc48971984cd','6683e976-3008-4ccf-91cf-070ef0b8467b','2025-01-09 11:48:45','2025-01-09 11:48:45'),('Bato Kunku','bed5efff-c8ca-4895-b98f-1f48686fdb19','6dfd60d7-d156-4a56-9f26-fa57bea9ed5c','2025-01-09 11:47:53','2025-01-09 11:47:53'),('Bakau','a82ad975-6bda-41a2-8531-f45bbc5fc606','7a717c88-5263-4e50-8814-639f5d1d55e1','2025-01-09 10:31:20','2025-01-09 10:31:20'),('Busumbala','1f3d0aad-0a13-4ae5-a244-746ef6831e40','814a0146-d87f-446c-b885-54f87a84e924','2025-01-05 22:32:15','2025-01-05 22:32:15'),('Brikama','2cf55223-de65-4f79-89d8-265268efa606','8225f301-dbe6-4775-9c29-17a2c69e1801','2025-01-09 11:40:43','2025-01-09 11:40:43'),('Brufut','bed5efff-c8ca-4895-b98f-1f48686fdb19','8b3c64d4-93c3-4e17-a30c-4d6a3a0ff2ce','2025-01-09 14:31:30','2025-01-09 14:31:30'),('Tranquil','56c24f84-5f68-43a5-8015-ab0c914f9df1','9b79340d-fb10-4f9e-854f-8e411e673e48','2025-01-09 11:50:15','2025-01-09 11:50:15'),('Madina Salaam','588ec62c-d897-465a-b145-e1bb33f96fa3','a1b86683-c805-4f66-a170-e77fe1e7aeb1','2025-01-09 11:45:13','2025-01-09 11:45:13'),('Jalambang','2cf55223-de65-4f79-89d8-265268efa606','ab506b80-6a5d-4348-958d-eb3fc77da3ab','2025-01-09 11:46:49','2025-01-09 11:46:49'),('Berending','588ec62c-d897-465a-b145-e1bb33f96fa3','ac2e4239-0c28-4683-bd98-6b073c2fd33c','2025-01-09 11:45:00','2025-01-09 11:45:00'),('Brusubi','56c24f84-5f68-43a5-8015-ab0c914f9df1','d3062765-ad22-4e4a-afd5-61ece7edaab9','2025-01-09 11:49:43','2025-01-09 11:49:43'),('Mandaur','2cf55223-de65-4f79-89d8-265268efa606','d79382b9-4a4b-4249-9440-9cc35144e91b','2025-01-09 11:41:03','2025-01-09 11:41:03'),('Darsilami','2cf55223-de65-4f79-89d8-265268efa606','dd2004ac-417d-46fd-8748-9f03d47611d7','2025-01-09 11:41:42','2025-01-09 11:41:42'),('Banjul','541c2349-53e2-4617-81e3-1f3add2763c5','ecdf4456-a2da-4945-b6c0-92348082266a','2025-01-09 11:23:42','2025-01-09 11:23:42'),('Gunjur','588ec62c-d897-465a-b145-e1bb33f96fa3','ef29b9d6-9745-4ce2-99f1-e289c3d047c4','2025-01-09 11:00:49','2025-01-09 11:00:49'),('Marakissa','2cf55223-de65-4f79-89d8-265268efa606','f02dd300-536d-47ff-96a3-d39b3a2943c7','2025-01-09 11:40:27','2025-01-09 11:40:27'),('Penjem','2cf55223-de65-4f79-89d8-265268efa606','fd32f2aa-d1da-45df-a003-8171b7b0a1ad','2025-01-09 11:41:12','2025-01-09 11:41:12'),('Kiti','2cf55223-de65-4f79-89d8-265268efa606','fd375db6-8451-48f1-872d-59e1de7d6132','2025-01-05 19:32:15','2025-01-05 19:32:15');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `image_url` varchar(255) NOT NULL,
  `property_id` varchar(64) DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `property_id` (`property_id`),
  CONSTRAINT `images_ibfk_1` FOREIGN KEY (`property_id`) REFERENCES `properties` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES ('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Prim-Apartments-Sanyang-The-GambiaWhatsApp-Image-2024-07-10-at-16.17.08.jpeg','e293d506-d10e-4e2c-beda-12d6560f5497','038b8c92-8217-49df-956f-e375a87dffd8','2025-01-05 22:47:31','2025-01-05 22:47:31'),('https://gamrealty.com/wp-content/uploads/2023/12/IMG_20231211_142416.jpg','cc50dcdf-f13b-4661-a7c6-e7a37a446abd','0cf1fdcc-0229-4f1d-af46-92ea6ef7fd95','2025-01-09 14:51:48','2025-01-09 14:51:48'),('https://gamrealty.com/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-06-at-10.55.56-1.jpeg','22c98a86-d341-462a-b0f2-a805c2700418','0ef1f625-2868-469f-a88c-9d9835487f4b','2025-01-08 02:42:40','2025-01-08 02:42:40'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-15-at-18.13.24-1.jpeg','8a76efe0-c38f-4c99-9771-d548f3c132ec','11005d57-0b1c-4ab4-a65e-feb491cac61f','2025-01-09 14:36:55','2025-01-09 14:36:55'),('https://gamrealty.com/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-06-at-10.55.56-4.jpeg','22c98a86-d341-462a-b0f2-a805c2700418','18647f1b-6020-4873-ba74-638dae43db11','2025-01-08 02:42:40','2025-01-08 02:42:40'),('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Premium-Rental-Villa-Seaview-Buruft-Heights-GambiaWhatsApp-Image-2024-06-28-at-11.13.00-3.jpg','ddaf56c8-70be-480e-a060-c13f451480bf','20429add-9ff4-4b3a-a000-0ed7b187db55','2025-01-09 14:43:21','2025-01-09 14:43:21'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-20-at-17.33.53-5.jpeg','9021ae0e-92eb-4a50-864b-45d6741252b4','2449892f-fe49-45d5-b1cf-e5f6146b3789','2025-01-09 14:00:53','2025-01-09 14:00:53'),('https://gamrealty.com/wp-content/uploads/2024/01/Gamrealty-Kololi-Sands-Long-term-apartment-rentalKS-1108-balcony-standard-scale-2_00x-scaled.jpg','65f51966-edb7-4237-bf00-b6d934d31a1e','26605e81-bcd9-44ac-8850-e1f4843d7836','2025-01-09 14:48:07','2025-01-09 14:48:07'),('https://gamrealty.com/wp-content/uploads/2024/04/WhatsApp-Image-2024-04-02-at-15.38.30.jpeg','4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','2b965bc2-60b7-4c48-a01b-b0c17837f8df','2025-01-09 13:48:35','2025-01-09 13:48:35'),('https://gamrealty.com/wp-content/uploads/2024/01/Gamrealty-Kololi-Sands-Long-term-apartment-rentalKS-1108-beachview-standard-scale-2_00x-scaled.jpg','65f51966-edb7-4237-bf00-b6d934d31a1e','2d62f456-7a1f-4636-bbaf-3bd003225468','2025-01-09 14:48:07','2025-01-09 14:48:07'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-19-at-10.40.34.jpeg','9021ae0e-92eb-4a50-864b-45d6741252b4','36ee8f12-f3ab-481d-8b39-d81c7c17346c','2025-01-09 14:00:53','2025-01-09 14:00:53'),('https://gamrealty.com/wp-content/uploads/2024/03/IMG_8700.jpg','4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','422270bc-be01-44a4-8146-fb93335b3077','2025-01-09 13:48:35','2025-01-09 13:48:35'),('https://gamrealty.com/wp-content/uploads/2024/01/Gamrealty-Kololi-Sands-Long-term-apartment-rentalKS-1108-standard-scale-2_00x-scaled.jpg','65f51966-edb7-4237-bf00-b6d934d31a1e','43844ba2-2070-4551-b3d6-6b805b6bfb39','2025-01-09 14:48:07','2025-01-09 14:48:07'),('https://gamrealty.com/wp-content/uploads/2023/12/IMG_20231211_141254.jpg','cc50dcdf-f13b-4661-a7c6-e7a37a446abd','489a672c-5c53-45ac-bf1a-d168b7d045e2','2025-01-09 14:51:48','2025-01-09 14:51:48'),('https://gamrealty.com/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-06-at-13.28.17.jpeg','22c98a86-d341-462a-b0f2-a805c2700418','4cc9a541-d48e-40bc-adac-474923dceff7','2025-01-08 02:42:40','2025-01-08 02:42:40'),('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Prim-Apartments-Sanyang-The-GambiaWhatsApp-Image-2024-07-10-at-16.17.07-1.jpeg','e293d506-d10e-4e2c-beda-12d6560f5497','4fd48bcd-d17f-4c1b-818c-a0180afa26ce','2025-01-05 22:47:31','2025-01-05 22:47:31'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-27-at-12.03.47-3.jpeg','32af3948-73ae-4abd-b878-a1e91c6c26b5','578bb5b1-b186-4c84-a5e7-4b7743eb8f5b','2025-01-09 14:54:09','2025-01-09 14:54:09'),('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Premium-Rental-Villa-Seaview-Buruft-Heights-GambiaWhatsApp-Image-2024-06-28-at-11.13.03-1.jpg','ddaf56c8-70be-480e-a060-c13f451480bf','5820ed2e-895b-4021-ba06-8a8106fce4ce','2025-01-09 14:43:21','2025-01-09 14:43:21'),('https://gamrealty.com/wp-content/uploads/2023/12/1200px-Averrhoa_carambola_ARS_k5735-7.jpg','cc50dcdf-f13b-4661-a7c6-e7a37a446abd','5d4c7c70-17db-4c9d-82d9-2622e5094097','2025-01-09 14:51:48','2025-01-09 14:51:48'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-27-at-12.03.47-3.jpeg','32af3948-73ae-4abd-b878-a1e91c6c26b5','650d0d40-66e0-4e2f-be07-832798f145aa','2025-01-09 14:54:09','2025-01-09 14:54:09'),('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Prim-Apartments-Sanyang-The-GambiaWhatsApp-Image-2024-07-10-at-16.17.09-1.jpeg','e293d506-d10e-4e2c-beda-12d6560f5497','66ba0900-6aa1-439e-b0ae-5d8d52e66cde','2025-01-05 22:47:31','2025-01-05 22:47:31'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-27-at-12.03.47-2.jpeg','32af3948-73ae-4abd-b878-a1e91c6c26b5','6b48ca0c-c99d-497d-96d8-4f666b430d4f','2025-01-09 14:54:09','2025-01-09 14:54:09'),('https://gambiapropertyshop.com/wp-content/uploads/2014/02/Land-for-Sale-Batukunku-1.jpg','32af3948-73ae-4abd-b878-a1e91c6c26b5','6bf886f3-b1fe-4a03-bddd-820ba0a220ba','2025-01-10 11:30:58','2025-01-10 11:30:58'),('https://gamrealty.com/wp-content/themes/realhomes-child/img/GR-Lets-talk-chat-icon.png','e293d506-d10e-4e2c-beda-12d6560f5497','6e2de1d8-a6fc-417c-9a2b-2b14e744be69','2025-01-05 22:47:31','2025-01-05 22:47:31'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-20-at-17.33.53.jpeg','9021ae0e-92eb-4a50-864b-45d6741252b4','85c1ec5e-cfc7-4b99-a8c0-d067a697cc94','2025-01-09 14:00:53','2025-01-09 14:00:53'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-20-at-17.33.51.jpeg','9021ae0e-92eb-4a50-864b-45d6741252b4','8bf9bb56-482c-41ed-9b37-3c18195af95d','2025-01-09 14:00:53','2025-01-09 14:00:53'),('https://gamrealty.com/wp-content/uploads/2024/01/Gamrealty-Kololi-Sands-Long-term-apartment-rentalKS-1108-room-view-ext-standard-scale-2_00x-scaled.jpg','65f51966-edb7-4237-bf00-b6d934d31a1e','8e0bd0c2-f11f-4e82-90b8-ab71b1c9dd6b','2025-01-09 14:48:07','2025-01-09 14:48:07'),('https://gamrealty.com/wp-content/uploads/2023/12/IMG_20231211_142430.jpg','cc50dcdf-f13b-4661-a7c6-e7a37a446abd','91ba62c0-59d7-4172-81c7-2ddb8e9706eb','2025-01-09 14:51:48','2025-01-09 14:51:48'),('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Premium-Rental-Villa-Seaview-Buruft-Heights-GambiaWhatsApp-Image-2024-06-28-at-11.13.03.jpg','ddaf56c8-70be-480e-a060-c13f451480bf','91be23fe-7452-4f89-aeba-4d649d121f42','2025-01-09 14:43:21','2025-01-09 14:43:21'),('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Premium-Rental-Villa-Seaview-Buruft-Heights-GambiaWhatsApp-Image-2024-06-28-at-11.13.02-1.jpg','ddaf56c8-70be-480e-a060-c13f451480bf','927b901f-ec58-4d0a-93a4-7a3099988e7a','2025-01-09 14:43:21','2025-01-09 14:43:21'),('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Premium-Rental-Villa-Seaview-Buruft-Heights-GambiaWhatsApp-Image-2024-06-28-at-11.13.02-2.jpg','ddaf56c8-70be-480e-a060-c13f451480bf','9de5f682-afac-459e-a422-4f6d6bd83e60','2025-01-09 14:43:21','2025-01-09 14:43:21'),('https://gamrealty.com/wp-content/uploads/2024/01/Gamrealty-Kololi-Sands-Long-term-apartment-rentalKS-window-view-standard-scale-2_00x-scaled.jpeg','65f51966-edb7-4237-bf00-b6d934d31a1e','a140cebf-cb18-4150-a149-4949a9e5bbd4','2025-01-09 14:48:07','2025-01-09 14:48:07'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-15-at-18.13.25-1.jpeg','8a76efe0-c38f-4c99-9771-d548f3c132ec','a55154b4-c5f4-4a97-b1b8-9f7b7bbcef6b','2025-01-09 14:36:55','2025-01-09 14:36:55'),('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Premium-Rental-Villa-Seaview-Buruft-Heights-GambiaWhatsApp-Image-2024-06-28-at-11.13.01-3.jpg','ddaf56c8-70be-480e-a060-c13f451480bf','a7263ed3-a148-4620-a45d-b9fb6cc96103','2025-01-09 14:43:21','2025-01-09 14:43:21'),('https://gamrealty.com/wp-content/uploads/2024/04/WhatsApp-Image-2024-04-02-at-15.38.34-1.jpeg','4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','b5058cec-9742-4f5c-9304-28c84162becf','2025-01-09 13:48:35','2025-01-09 13:48:35'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-15-at-18.13.24.jpeg','8a76efe0-c38f-4c99-9771-d548f3c132ec','b76d5435-df9e-4e70-bef4-3b8e93123671','2025-01-09 14:36:55','2025-01-09 14:36:55'),('https://gamrealty.com/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-06-at-10.55.57.jpeg','22c98a86-d341-462a-b0f2-a805c2700418','c167d4ee-b7cd-4691-8773-0eddcdde38fb','2025-01-08 02:42:40','2025-01-08 02:42:40'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-27-at-12.03.47-4.jpeg','32af3948-73ae-4abd-b878-a1e91c6c26b5','c36e7beb-5e3f-430f-8865-31b436e244a5','2025-01-09 14:54:09','2025-01-09 14:54:09'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-15-at-18.13.24-2.jpeg','8a76efe0-c38f-4c99-9771-d548f3c132ec','c67a42ac-78cb-4bde-a95b-6025cb68af96','2025-01-09 14:36:55','2025-01-09 14:36:55'),('https://gamrealty.com/wp-content/uploads/2023/12/1200px-Averrhoa_carambola_ARS_k5735-7.jpg','cc50dcdf-f13b-4661-a7c6-e7a37a446abd','c9ea20fb-ec2a-467a-a32c-1fe8b1e892c4','2025-01-09 14:51:48','2025-01-09 14:51:48'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-20-at-17.33.53-6.jpeg','9021ae0e-92eb-4a50-864b-45d6741252b4','cea1d057-94d1-4a58-aa9d-c0c68c8ab17c','2025-01-09 14:00:53','2025-01-09 14:00:53'),('https://gamrealty.com/wp-content/uploads/2024/04/WhatsApp-Image-2024-04-02-at-15.38.32-2.jpeg','4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','d32c049a-0534-44e2-b186-784cb4fe7d17','2025-01-09 13:48:35','2025-01-09 13:48:35'),('https://gamrealty.com/wp-content/uploads/2024/04/WhatsApp-Image-2024-04-02-at-15.38.30-2.jpeg','4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','d3af8030-bd69-4950-85c9-6694fc46b2e3','2025-01-09 13:48:35','2025-01-09 13:48:35'),('https://gamrealty.com/wp-content/uploads/2024/04/WhatsApp-Image-2024-04-02-at-15.38.30-1.jpeg','4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','dc1b59e9-6b67-4cc7-8a26-e4f56262c4b3','2025-01-09 13:48:35','2025-01-09 13:48:35'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-15-at-18.13.23-1.jpeg','8a76efe0-c38f-4c99-9771-d548f3c132ec','dd05836d-0842-42cd-8cf2-111bc1dec858','2025-01-09 14:36:55','2025-01-09 14:36:55'),('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Prim-Apartments-Sanyang-The-GambiaWhatsApp-Image-2024-07-10-at-16.17.11-2.jpeg','e293d506-d10e-4e2c-beda-12d6560f5497','e05451de-d17b-4384-bafe-a76885f898e8','2025-01-05 22:47:31','2025-01-05 22:47:31'),('https://gambiapropertyshop.com/wp-content/uploads/2014/02/Land-for-Sale-Batukunku-1.jpg',NULL,'e1b9644f-ee67-4b99-8247-77e425597ef6','2025-01-09 19:28:12','2025-01-09 19:28:12'),('https://gamrealty.com/wp-content/uploads/2024/07/Gamrealty-Prim-Apartments-Sanyang-The-GambiaWhatsApp-Image-2024-07-10-at-16.17.06.jpeg','e293d506-d10e-4e2c-beda-12d6560f5497','e1c74508-c2f7-42a4-9001-7cb7e298d9f3','2025-01-05 22:47:31','2025-01-05 22:47:31'),('https://gamrealty.com/wp-content/uploads/2024/04/WhatsApp-Image-2024-04-02-at-15.38.32-1.jpeg','4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','e4b7b5d6-a79c-46ff-83b7-374e8992302e','2025-01-09 13:48:35','2025-01-09 13:48:35'),('https://gamrealty.com/wp-content/uploads/2024/02/WhatsApp-Image-2024-02-02-at-12.38.44.jpeg','22c98a86-d341-462a-b0f2-a805c2700418','ef7bde95-11eb-4d25-a8f7-72e1a0b36e40','2025-01-08 02:42:40','2025-01-08 02:42:40'),('https://gamrealty.com/wp-content/uploads/2023/12/IMG_20231211_141257.jpg','cc50dcdf-f13b-4661-a7c6-e7a37a446abd','ef99fe4c-08e0-47d0-b258-b492c0fc312c','2025-01-09 14:51:48','2025-01-09 14:51:48'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-15-at-18.13.23-1.jpeg','8a76efe0-c38f-4c99-9771-d548f3c132ec','f02d849d-a701-40af-a8c7-4cb1dca1172b','2025-01-09 14:36:55','2025-01-09 14:36:55'),('https://gamrealty.com/wp-content/uploads/2024/11/WhatsApp-Image-2024-11-20-at-17.33.53-8.jpeg','9021ae0e-92eb-4a50-864b-45d6741252b4','f452b94f-7e47-47d1-b351-4df492f4c4cc','2025-01-09 14:00:53','2025-01-09 14:00:53'),('https://gamrealty.com/wp-content/uploads/2024/01/Gamrealty-Kololi-Sands-Long-term-apartment-rentalKS-1108-interior-standard-scale-2_00x-scaled.jpg','65f51966-edb7-4237-bf00-b6d934d31a1e','fe1e13ca-7f14-46b1-9771-9f5f5c5e890a','2025-01-09 14:48:07','2025-01-09 14:48:07');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `properties`
--

DROP TABLE IF EXISTS `properties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `properties` (
  `title` varchar(255) NOT NULL,
  `user_id` varchar(64) DEFAULT NULL,
  `price` int NOT NULL,
  `location` varchar(255) NOT NULL,
  `description` text,
  `property_type` enum('rent','sale') NOT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `city_id` varchar(64) DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `city_id` (`city_id`),
  FULLTEXT KEY `title` (`title`,`description`),
  CONSTRAINT `properties_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `properties_ibfk_2` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `properties`
--

LOCK TABLES `properties` WRITE;
/*!40000 ALTER TABLE `properties` DISABLE KEYS */;
INSERT INTO `properties` VALUES ('Three Bedroom Apartment','f9094884-6f2f-4f33-88e0-8a503cb640fc',3500,'Busumbala, Busumbala Area, West Coast Region','Modern three bedroom apartment with standard size room. Suitable for all families','rent',1,'814a0146-d87f-446c-b885-54f87a84e924','22c98a86-d341-462a-b0f2-a805c2700418','2025-01-08 02:42:40','2025-01-10 21:14:34'),('3000 m2 Plot of Land for Sale in Gunjur','f9094884-6f2f-4f33-88e0-8a503cb640fc',2400000,'Gunjur, Gunjur Area, West Coast Region','Gunjur is a growing town, conveniently located near Kartong and just a short distance from the pristine beaches along the riverbanks and the Senegalese border. This plot offers a tranquil environment and beautiful nature, perfect for those seeking peace and privacy with easy access to nearby amenities.','sale',1,'ef29b9d6-9745-4ce2-99f1-e289c3d047c4','32af3948-73ae-4abd-b878-a1e91c6c26b5','2025-01-09 14:54:09','2025-01-09 14:54:09'),('Newly Built Apartment Complex with 16 units','084aef31-75fc-4678-9dbb-2e4f7b415957',40000000,'Kotu, Kotu Area, Kanifing Municipal Council','Explore the potential of this modern apartment complex located in the heart of Kotu, The Gambia.\r\nWith 16 units, including 4 spacious two-bedroom apartments and 8 spacious studios, this property offers a versatile investment opportunity for those seeking to enter the leisure and rental business.','sale',1,'1351eb04-faaf-461c-ba95-ad26538f8bc0','4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','2025-01-09 13:48:35','2025-01-09 13:48:35'),('Unfurnished 2-bed Apartment with Prime Ocean View – Long Term Rent','f9094884-6f2f-4f33-88e0-8a503cb640fc',15000,'Kololi, Kotu Area, Kanifing Municipal Council','UNFURNISHED APARTMENT WITH PRIME OCEAN VIEW AND SUPER LARGE CORNER BALCONY OVERLOOKING THE ATLANTIC OCEAN','rent',1,'25f3b09d-35b7-4113-8674-e022ce5422e9','65f51966-edb7-4237-bf00-b6d934d31a1e','2025-01-09 14:48:07','2025-01-09 14:48:07'),('Fully Furnished 3 Bedroom Bungalow at Twin Trees Residences','f9094884-6f2f-4f33-88e0-8a503cb640fc',6120000,'Brufut, Brufut Area, West Coast Region','For Sale: Fully Furnished 3-bedroom Bungalow at Twin Trees Residences, Brufut\r\n','sale',1,'8b3c64d4-93c3-4e17-a30c-4d6a3a0ff2ce','8a76efe0-c38f-4c99-9771-d548f3c132ec','2025-01-09 14:36:55','2025-01-09 14:36:55'),('Large Quality Office Space for Rent','084aef31-75fc-4678-9dbb-2e4f7b415957',17500,'Bakau, Bakau Area, Kanifing Municipal Council','Gamrealty is pleased to offer this prime office space for rent, centrally located in a highly sought-after area, ideal for businesses looking to establish a professional presence in The Gambia. This office provides easy access to key commercial and residential zones, located between the Kanifing Industrial Zone, Banjul, Fajara, and the Senegambia area. It is also conveniently close to major landmarks, including the Independence Stadium, Twin Towers and The Diplomat (currently under construction), making it a strategic location for your business','rent',1,'7a717c88-5263-4e50-8814-639f5d1d55e1','9021ae0e-92eb-4a50-864b-45d6741252b4','2025-01-09 14:00:53','2025-01-09 14:00:53'),('10.000 m2 Green Oasis for Sale | Kending Saibel – Sanyang','f9094884-6f2f-4f33-88e0-8a503cb640fc',14040000,'Sanyang, Sanyang Area, West Coast Region','Discover Your Tropical Paradise in Kending Saibel\r\n10.000 m2 Plot of Land Sale | Keninding Saibali (between Tujereng and Sanyang)\r\n\r\nWelcome to a once-in-a-lifetime opportunity! This 10,000 m² (2.5 acres) plot of land in Kending Saibel, just 2.2 km from the pristine beach of Sanyang, is a green oasis like no other.','sale',1,'15073e03-64fd-440f-bf6e-3a6dcfac8fab','cc50dcdf-f13b-4661-a7c6-e7a37a446abd','2025-01-09 14:51:48','2025-01-09 14:51:48'),('Luxury Beachfront 3 Bedroom Villa with Pool','f9094884-6f2f-4f33-88e0-8a503cb640fc',240000,'Brufut, Brufut Area, West Coast Region','Luxury 3 Bedroom Villa with Pool in Brufut Heights, First Line with SeaviewExperience unparalleled luxury in Brufut Heights with this exquisite 2-storey villa, offering breathtaking ocean views and available for long-term rental at $40,000 per annum. Formerly tenanted by the US Embassy, this property is ideal for embassy staff, high-profile expatriates, and individuals seeking the pinnacle of comfort and security.','rent',1,'8b3c64d4-93c3-4e17-a30c-4d6a3a0ff2ce','ddaf56c8-70be-480e-a060-c13f451480bf','2025-01-09 14:43:21','2025-01-09 14:43:21'),('Two bedroom apartment','bf9dae03-2e21-4336-9c45-d7943255e05b',6000,'Busumbala, Busumbala Area, West Coast Region','Two bedroom apartment with two bathrooms, fully furnished kitchen.','rent',1,'814a0146-d87f-446c-b885-54f87a84e924','e293d506-d10e-4e2c-beda-12d6560f5497','2025-01-05 22:47:31','2025-01-05 22:58:04');
/*!40000 ALTER TABLE `properties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property_amenity`
--

DROP TABLE IF EXISTS `property_amenity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `property_amenity` (
  `property_id` varchar(60) NOT NULL,
  `amenity_id` varchar(60) NOT NULL,
  PRIMARY KEY (`property_id`,`amenity_id`),
  KEY `amenity_id` (`amenity_id`),
  CONSTRAINT `property_amenity_ibfk_1` FOREIGN KEY (`property_id`) REFERENCES `properties` (`id`),
  CONSTRAINT `property_amenity_ibfk_2` FOREIGN KEY (`amenity_id`) REFERENCES `amenities` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property_amenity`
--

LOCK TABLES `property_amenity` WRITE;
/*!40000 ALTER TABLE `property_amenity` DISABLE KEYS */;
INSERT INTO `property_amenity` VALUES ('65f51966-edb7-4237-bf00-b6d934d31a1e','124a8cd6-6516-4f35-8819-b457ba336e75'),('8a76efe0-c38f-4c99-9771-d548f3c132ec','124a8cd6-6516-4f35-8819-b457ba336e75'),('ddaf56c8-70be-480e-a060-c13f451480bf','124a8cd6-6516-4f35-8819-b457ba336e75'),('8a76efe0-c38f-4c99-9771-d548f3c132ec','1d97d186-8020-46a3-81e9-a139b82b5729'),('9021ae0e-92eb-4a50-864b-45d6741252b4','1d97d186-8020-46a3-81e9-a139b82b5729'),('cc50dcdf-f13b-4661-a7c6-e7a37a446abd','1d97d186-8020-46a3-81e9-a139b82b5729'),('22c98a86-d341-462a-b0f2-a805c2700418','3131c735-fb0e-495e-bb73-e08d110a1319'),('4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','3131c735-fb0e-495e-bb73-e08d110a1319'),('65f51966-edb7-4237-bf00-b6d934d31a1e','3131c735-fb0e-495e-bb73-e08d110a1319'),('8a76efe0-c38f-4c99-9771-d548f3c132ec','3131c735-fb0e-495e-bb73-e08d110a1319'),('9021ae0e-92eb-4a50-864b-45d6741252b4','3131c735-fb0e-495e-bb73-e08d110a1319'),('cc50dcdf-f13b-4661-a7c6-e7a37a446abd','3131c735-fb0e-495e-bb73-e08d110a1319'),('ddaf56c8-70be-480e-a060-c13f451480bf','3131c735-fb0e-495e-bb73-e08d110a1319'),('22c98a86-d341-462a-b0f2-a805c2700418','6180b61c-c0cd-46db-90db-b341f095d38e'),('8a76efe0-c38f-4c99-9771-d548f3c132ec','6180b61c-c0cd-46db-90db-b341f095d38e'),('cc50dcdf-f13b-4661-a7c6-e7a37a446abd','6180b61c-c0cd-46db-90db-b341f095d38e'),('ddaf56c8-70be-480e-a060-c13f451480bf','6180b61c-c0cd-46db-90db-b341f095d38e'),('e293d506-d10e-4e2c-beda-12d6560f5497','6180b61c-c0cd-46db-90db-b341f095d38e'),('e293d506-d10e-4e2c-beda-12d6560f5497','8062f6ae-5608-4f52-a2f6-223be73655ea'),('22c98a86-d341-462a-b0f2-a805c2700418','9aba2d3f-5927-4967-8f91-579ae391d324'),('4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','9aba2d3f-5927-4967-8f91-579ae391d324'),('65f51966-edb7-4237-bf00-b6d934d31a1e','9aba2d3f-5927-4967-8f91-579ae391d324'),('8a76efe0-c38f-4c99-9771-d548f3c132ec','9aba2d3f-5927-4967-8f91-579ae391d324'),('9021ae0e-92eb-4a50-864b-45d6741252b4','9aba2d3f-5927-4967-8f91-579ae391d324'),('ddaf56c8-70be-480e-a060-c13f451480bf','9aba2d3f-5927-4967-8f91-579ae391d324'),('e293d506-d10e-4e2c-beda-12d6560f5497','9aba2d3f-5927-4967-8f91-579ae391d324'),('8a76efe0-c38f-4c99-9771-d548f3c132ec','a6b79c2a-8f49-4b70-9cb3-11bf7cf1dff5'),('9021ae0e-92eb-4a50-864b-45d6741252b4','a6b79c2a-8f49-4b70-9cb3-11bf7cf1dff5'),('4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','cb4a8495-8867-4b94-bf72-1cbe1374e2d1'),('65f51966-edb7-4237-bf00-b6d934d31a1e','cb4a8495-8867-4b94-bf72-1cbe1374e2d1'),('ddaf56c8-70be-480e-a060-c13f451480bf','cb4a8495-8867-4b94-bf72-1cbe1374e2d1'),('4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','d0d7ef22-8742-4e18-9205-e9b16992bffa'),('8a76efe0-c38f-4c99-9771-d548f3c132ec','d0d7ef22-8742-4e18-9205-e9b16992bffa'),('ddaf56c8-70be-480e-a060-c13f451480bf','d0d7ef22-8742-4e18-9205-e9b16992bffa'),('22c98a86-d341-462a-b0f2-a805c2700418','eb04e3f3-7c52-444b-bd4a-2b53695b9ec2'),('4ebdae1d-c8ce-49c8-8dbe-a31945d4f150','eb04e3f3-7c52-444b-bd4a-2b53695b9ec2'),('65f51966-edb7-4237-bf00-b6d934d31a1e','eb04e3f3-7c52-444b-bd4a-2b53695b9ec2'),('8a76efe0-c38f-4c99-9771-d548f3c132ec','eb04e3f3-7c52-444b-bd4a-2b53695b9ec2'),('ddaf56c8-70be-480e-a060-c13f451480bf','eb04e3f3-7c52-444b-bd4a-2b53695b9ec2'),('65f51966-edb7-4237-bf00-b6d934d31a1e','f389f874-c6af-49e9-8499-191d34ca6217'),('8a76efe0-c38f-4c99-9771-d548f3c132ec','f389f874-c6af-49e9-8499-191d34ca6217'),('9021ae0e-92eb-4a50-864b-45d6741252b4','f389f874-c6af-49e9-8499-191d34ca6217');
/*!40000 ALTER TABLE `property_amenity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regions`
--

DROP TABLE IF EXISTS `regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regions` (
  `name` varchar(60) NOT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regions`
--

LOCK TABLES `regions` WRITE;
/*!40000 ALTER TABLE `regions` DISABLE KEYS */;
INSERT INTO `regions` VALUES ('Upper River Region','019aac95-f89b-464d-bb88-03ec48342153','2025-01-05 13:07:09','2025-01-05 13:07:09'),('Banjul City Council','2fa2eb1d-0b46-4937-9aaf-a6f941dccabf','2025-01-05 13:08:24','2025-01-05 13:08:24'),('North Bank Region','33bc6cf7-bd30-41a0-8102-84fd3b8c5c27','2025-01-05 13:08:04','2025-01-05 13:08:04'),('Lower River Region','68d85865-7a93-49bd-8fda-af2915654f76','2025-01-05 11:34:47','2025-01-05 11:34:47'),('Central River Region','70ffc274-4244-4ff3-a655-3aba3d6758aa','2025-01-05 12:16:03','2025-01-05 12:16:03'),('West Coast Region','8941d16a-0d65-4e89-b3cd-5b1364cdbc78','2025-01-05 12:07:14','2025-01-05 12:07:14'),('Kanifing Municipal Council','9febe65c-4694-4d93-b63a-e77ee1085b43','2025-01-05 13:06:50','2025-01-05 13:06:50');
/*!40000 ALTER TABLE `regions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `username` varchar(64) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `phone_number` varchar(16) NOT NULL,
  `whatsapp` varchar(16) DEFAULT NULL,
  `id` varchar(64) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('lamin','lamin@email.com','pbkdf2:sha256:1000000$fJuf1cwl$8c0e14ab1e40c468e9689da5357f40b7cd7279b627f8c7b1cc01a6b045751772','12345601','12345601','084aef31-75fc-4678-9dbb-2e4f7b415957','2025-01-04 21:13:04','2025-01-04 21:13:04'),('binta','binta@email.com','pbkdf2:sha256:1000000$eccRpXKU$cd0e85f23227095ce1980c3a0c2ae6a9736295cc3e149c9e8518c8e217cf4dea','12345606','12345606','2f98208d-c9a6-4911-8343-28f25a2ee1b8','2025-01-04 21:14:27','2025-01-04 21:14:27'),('musa','musa@email.com','pbkdf2:sha256:1000000$qJbMQ1Gz$2a733a57f4daa9ddc55d4a819ef4595825d2d166480383b5fe1f41f68b2878ff','12345603','12345603','3381aed9-8911-4116-bccf-79e022769ece','2025-01-04 21:13:47','2025-01-04 21:13:47'),('Momodou','omodou@email.com','pbkdf2:sha256:1000000$lSFa1BAs$cda85579dc2927e74027d764eb308fd3992929da21e3fa66f0946494dd41f516','12345609','12345609','450b9767-ba93-493f-82a9-bd54dfcf6294','2025-01-10 21:29:38','2025-01-10 21:31:34'),('amadou','amadou@email.com','pbkdf2:sha256:1000000$mCAnGb4Y$63a4b8a504c62a28df65dc39f8aa910d5dacd2abee18a555a5027c9daa821087','12345609','12345609','52cd7c1c-8bb1-4bd3-8577-2b5796f5e722','2025-01-05 01:19:32','2025-01-10 22:03:51'),('aisha','aisha@email.com','pbkdf2:sha256:1000000$tVvNdli0$df77dc7dd17658f1cc53f34e06c61e1dba737ebc761b7d1f37a4e62e34f7c7cb','12345604','12345604','5b7aa043-bd4a-4f1c-8f31-4cced3e0b267','2025-01-04 21:13:59','2025-01-04 21:13:59'),('sanna','sanna@email.com','pbkdf2:sha256:1000000$WsDrJEP1$275aeb116f187b830c95f16464913dab25f7ad468ec336354d9dd037f1a07384','12345605','12345605','af59e596-82f6-41eb-81e2-804841f6d841','2025-01-04 21:14:11','2025-01-04 21:14:11'),('admin','admin@email.com','pbkdf2:sha256:1000000$yZc0yfTn$4c2984d6f69d7e0e986a9555f82bd8637537f3782e324b2f10020821c98eb307','12345609','12345609','bf9dae03-2e21-4336-9c45-d7943255e05b','2025-01-05 00:48:04','2025-01-05 01:09:16'),('fatou','fatou@email.com','pbkdf2:sha256:1000000$6J0ObWe8$26df72c54b0969d906373f3091143c1a10ce046508f762d045594b713092c767','12345602','12345602','f22180a6-c0cc-4537-88d3-9dfcf39fafe5','2025-01-04 21:13:25','2025-01-04 21:13:25'),('omar','omar@email.com','pbkdf2:sha256:1000000$qTPvcbRh$47768709c24899ca9f43165de50253ff5738e9c87b227d132ad88ae979b12ef5','3588208','3588208','f9094884-6f2f-4f33-88e0-8a503cb640fc','2025-01-08 02:07:02','2025-01-08 02:07:02');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-12 13:17:02
