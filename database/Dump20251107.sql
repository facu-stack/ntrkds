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
-- Table structure for table `acceso`
--

DROP TABLE IF EXISTS `acceso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acceso` (
  `ID_usuario` int NOT NULL AUTO_INCREMENT,
  `ID_Acceso` int NOT NULL,
  `Usuario` varchar(45) NOT NULL,
  `Contraseña` varchar(45) NOT NULL,
  PRIMARY KEY (`ID_usuario`,`ID_Acceso`),
  UNIQUE KEY `ID_usuario_UNIQUE` (`ID_usuario`),
  CONSTRAINT `Especialista` FOREIGN KEY (`ID_usuario`) REFERENCES `especialista` (`idUsuario`),
  CONSTRAINT `Tutor` FOREIGN KEY (`ID_usuario`) REFERENCES `datos_tutor` (`ID_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acceso`
--

LOCK TABLES `acceso` WRITE;
/*!40000 ALTER TABLE `acceso` DISABLE KEYS */;
/*!40000 ALTER TABLE `acceso` ENABLE KEYS */;
UNLOCK TABLES;

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
  `FechaActualizacion` date NOT NULL,
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

--
-- Table structure for table `clinica`
--

DROP TABLE IF EXISTS `clinica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clinica` (
  `idClinica` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `LocalidadID` int NOT NULL,
  PRIMARY KEY (`idClinica`),
  UNIQUE KEY `idClinica_UNIQUE` (`idClinica`),
  KEY `LocalidadClinica_idx` (`LocalidadID`),
  CONSTRAINT `LocalidadClinica` FOREIGN KEY (`LocalidadID`) REFERENCES `localidad` (`idLocalidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clinica`
--

LOCK TABLES `clinica` WRITE;
/*!40000 ALTER TABLE `clinica` DISABLE KEYS */;
/*!40000 ALTER TABLE `clinica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `control`
--

DROP TABLE IF EXISTS `control`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `control` (
  `idControl` int NOT NULL AUTO_INCREMENT,
  `FechaActual` date NOT NULL,
  `DiagnosticoClinico` longtext NOT NULL,
  `PesoControl` float NOT NULL,
  `MasaMuscular` float NOT NULL,
  `MasaGrasa` float NOT NULL,
  `UltimoControl` date NOT NULL,
  `fmID` int NOT NULL,
  PRIMARY KEY (`idControl`),
  UNIQUE KEY `idControl_UNIQUE` (`idControl`),
  KEY `fmFK_idx` (`fmID`),
  CONSTRAINT `fmFK` FOREIGN KEY (`fmID`) REFERENCES `fichamedica` (`idFichaMedica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `control`
--

LOCK TABLES `control` WRITE;
/*!40000 ALTER TABLE `control` DISABLE KEYS */;
/*!40000 ALTER TABLE `control` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `datos_tutor`
--

DROP TABLE IF EXISTS `datos_tutor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `datos_tutor` (
  `ID_usuario` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL,
  `Direccion` varchar(45) NOT NULL,
  `Localidad` int NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `DNI` varchar(45) NOT NULL,
  PRIMARY KEY (`ID_usuario`),
  UNIQUE KEY `ID_usuario_UNIQUE` (`ID_usuario`),
  KEY `localidadFK_idx` (`Localidad`),
  CONSTRAINT `tutorLocalidad` FOREIGN KEY (`Localidad`) REFERENCES `localidad` (`idLocalidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `datos_tutor`
--

LOCK TABLES `datos_tutor` WRITE;
/*!40000 ALTER TABLE `datos_tutor` DISABLE KEYS */;
/*!40000 ALTER TABLE `datos_tutor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especialista`
--

DROP TABLE IF EXISTS `especialista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especialista` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Especialidad` varchar(45) NOT NULL,
  `ClinicaID` int NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `idUsuario_UNIQUE` (`idUsuario`),
  KEY `ClinicaEspecialista_idx` (`ClinicaID`),
  CONSTRAINT `ClinicaEspecialista` FOREIGN KEY (`ClinicaID`) REFERENCES `clinica` (`idClinica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especialista`
--

LOCK TABLES `especialista` WRITE;
/*!40000 ALTER TABLE `especialista` DISABLE KEYS */;
/*!40000 ALTER TABLE `especialista` ENABLE KEYS */;
UNLOCK TABLES;

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
  `aaID` int NOT NULL,
  PRIMARY KEY (`idFichaMedica`),
  UNIQUE KEY `idFichaMedica_UNIQUE` (`idFichaMedica`),
  KEY `aaFK_idx` (`aaID`),
  CONSTRAINT `aaFK` FOREIGN KEY (`aaID`) REFERENCES `anamnesisalimentaria` (`idAnamnesisAlimentaria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fichamedica`
--

LOCK TABLES `fichamedica` WRITE;
/*!40000 ALTER TABLE `fichamedica` DISABLE KEYS */;
/*!40000 ALTER TABLE `fichamedica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `localidad`
--

DROP TABLE IF EXISTS `localidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `localidad` (
  `idLocalidad` int NOT NULL AUTO_INCREMENT,
  `CP` varchar(12) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `ProvinciaID` int NOT NULL,
  PRIMARY KEY (`idLocalidad`),
  UNIQUE KEY `idLocalidad_UNIQUE` (`idLocalidad`),
  KEY `ProvinciaLocalidad_idx` (`ProvinciaID`),
  CONSTRAINT `ProvinciaLocalidad` FOREIGN KEY (`ProvinciaID`) REFERENCES `provincia` (`idProvincia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `localidad`
--

LOCK TABLES `localidad` WRITE;
/*!40000 ALTER TABLE `localidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `localidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paciente_tutor`
--

DROP TABLE IF EXISTS `paciente_tutor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paciente_tutor` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `paciente_id` int NOT NULL,
  `tutor_id` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `paciente_id` (`paciente_id`),
  KEY `tutor_id` (`tutor_id`),
  CONSTRAINT `paciente_tutor_ibfk_1` FOREIGN KEY (`paciente_id`) REFERENCES `pacientes` (`ID_usuario`),
  CONSTRAINT `paciente_tutor_ibfk_2` FOREIGN KEY (`tutor_id`) REFERENCES `datos_tutor` (`ID_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente_tutor`
--

LOCK TABLES `paciente_tutor` WRITE;
/*!40000 ALTER TABLE `paciente_tutor` DISABLE KEYS */;
/*!40000 ALTER TABLE `paciente_tutor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pacientes`
--

DROP TABLE IF EXISTS `pacientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pacientes` (
  `ID_usuario` int NOT NULL,
  `Domicilio` varchar(45) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL,
  `FechaNacimiento` date NOT NULL,
  `DNI` int NOT NULL,
  `Localidad` int NOT NULL,
  `FichaMedica` varchar(45) NOT NULL,
  PRIMARY KEY (`ID_usuario`),
  UNIQUE KEY `ID_usuario_UNIQUE` (`ID_usuario`),
  KEY `LocalidadFK_idx` (`Localidad`),
  CONSTRAINT `LocalidadFK` FOREIGN KEY (`Localidad`) REFERENCES `localidad` (`idLocalidad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pacientes`
--

LOCK TABLES `pacientes` WRITE;
/*!40000 ALTER TABLE `pacientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `pacientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provincia`
--

DROP TABLE IF EXISTS `provincia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provincia` (
  `idProvincia` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`idProvincia`),
  UNIQUE KEY `idProvincia_UNIQUE` (`idProvincia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provincia`
--

LOCK TABLES `provincia` WRITE;
/*!40000 ALTER TABLE `provincia` DISABLE KEYS */;
/*!40000 ALTER TABLE `provincia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `turnos`
--

DROP TABLE IF EXISTS `turnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turnos` (
  `ID_Turnos` int NOT NULL AUTO_INCREMENT,
  `Fecha` date DEFAULT NULL,
  `Hora` time DEFAULT NULL,
  `Motivo` varchar(45) DEFAULT NULL,
  `Paciente_ID` int NOT NULL,
  `Especialista_ID` int NOT NULL,
  PRIMARY KEY (`ID_Turnos`,`Paciente_ID`,`Especialista_ID`),
  UNIQUE KEY `ID_Turnos_UNIQUE` (`ID_Turnos`),
  KEY `PacientesTurnos_idx` (`Paciente_ID`),
  KEY `EspecialistaTurnos_idx` (`Especialista_ID`),
  CONSTRAINT `EspecialistaTurnos` FOREIGN KEY (`Especialista_ID`) REFERENCES `especialista` (`idUsuario`),
  CONSTRAINT `PacientesTurnos` FOREIGN KEY (`Paciente_ID`) REFERENCES `pacientes` (`ID_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turnos`
--

LOCK TABLES `turnos` WRITE;
/*!40000 ALTER TABLE `turnos` DISABLE KEYS */;
/*!40000 ALTER TABLE `turnos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-07 19:17:28
