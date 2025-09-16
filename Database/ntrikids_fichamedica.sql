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
-- Table structure for table `fichamedica`
--

DROP TABLE IF EXISTS `fichamedica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fichamedica` (
  `idFichaMedica` int NOT NULL AUTO_INCREMENT,
  `ActividadFisica` tinytext,
  `AlergiasID` int NOT NULL,
  `PesoAcutal` float NOT NULL,
  `PesoDeseado` float NOT NULL,
  `PesoIdeal` float NOT NULL,
  `IMC` float NOT NULL,
  `Altura` float NOT NULL,
  `Constipacion` tinyint NOT NULL,
  `Gastritis` tinyint NOT NULL,
  `Diabetes` tinyint NOT NULL,
  `Hipertencion` tinyint NOT NULL,
  `Colesterol` float NOT NULL,
  `Trigliceridos` float NOT NULL,
  `Uricemia` float NOT NULL,
  `Glucosa` float NOT NULL,
  `LDL` float NOT NULL,
  `HDL` float NOT NULL,
  `AnamnesiAlimenticiaID` int NOT NULL,
  `ControlID` int NOT NULL,
  PRIMARY KEY (`idFichaMedica`),
  UNIQUE KEY `idFichaMedica_UNIQUE` (`idFichaMedica`),
  KEY `AAFichaMedica_idx` (`AnamnesiAlimenticiaID`),
  KEY `ControlFichaMedica_idx` (`ControlID`),
  CONSTRAINT `AAFichaMedica` FOREIGN KEY (`AnamnesiAlimenticiaID`) REFERENCES `anamnesisalimentaria` (`idAnamnesisAlimentaria`),
  CONSTRAINT `ControlFichaMedica` FOREIGN KEY (`ControlID`) REFERENCES `control` (`idControl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fichamedica`
--

LOCK TABLES `fichamedica` WRITE;
/*!40000 ALTER TABLE `fichamedica` DISABLE KEYS */;
/*!40000 ALTER TABLE `fichamedica` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-16 11:02:48
