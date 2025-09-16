-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: ntrikids
-- ------------------------------------------------------
-- Server version	9.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `anamnesisalimentaria`
--

DROP TABLE IF EXISTS `anamnesisalimentaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anamnesisalimentaria` (
  `idAnamnesisAlimentaria` int NOT NULL AUTO_INCREMENT,
  `Leche` tinyint DEFAULT NULL,
  `Yogurt` tinyint DEFAULT NULL,
  `Quesos` tinyint DEFAULT NULL,
  `Carnes` tinyint DEFAULT NULL,
  `Huevos` tinyint DEFAULT NULL,
  `Hortalizas` tinyint DEFAULT NULL,
  `Frutas` tinyint DEFAULT NULL,
  `Panificados` tinyint DEFAULT NULL,
  `Pastas` tinyint DEFAULT NULL,
  `Azucar` tinyint DEFAULT NULL,
  `Edulcorantes` tinyint DEFAULT NULL,
  `Mermeladas` tinyint DEFAULT NULL,
  `DulceDeLeche` tinyint DEFAULT NULL,
  `Fritos` tinyint DEFAULT NULL,
  `Manteca` tinyint DEFAULT NULL,
  `Margarina` tinyint DEFAULT NULL,
  `Crema` tinyint DEFAULT NULL,
  `Mayonesa` tinyint DEFAULT NULL,
  `Caldos` tinyint DEFAULT NULL,
  `Bebidas` tinyint DEFAULT NULL,
  `Favoritos` longtext,
  `Aclaraciones` longtext,
  PRIMARY KEY (`idAnamnesisAlimentaria`),
  UNIQUE KEY `idAnamnesisAlimentaria_UNIQUE` (`idAnamnesisAlimentaria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anamnesisalimentaria`
--

LOCK TABLES `anamnesisalimentaria` WRITE;
/*!40000 ALTER TABLE `anamnesisalimentaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `anamnesisalimentaria` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-16 11:02:47
