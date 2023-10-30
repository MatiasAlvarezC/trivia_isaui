-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: trivia
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `preguntas_respuestas`
--

DROP TABLE IF EXISTS `preguntas_respuestas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `preguntas_respuestas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pregunta` varchar(255) NOT NULL,
  `opcion_1` varchar(255) NOT NULL,
  `opcion_2` varchar(255) NOT NULL,
  `opcion_3` varchar(255) NOT NULL,
  `opcion_4` varchar(255) NOT NULL,
  `respuesta_correcta` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preguntas_respuestas`
--

LOCK TABLES `preguntas_respuestas` WRITE;
/*!40000 ALTER TABLE `preguntas_respuestas` DISABLE KEYS */;
INSERT INTO `preguntas_respuestas` VALUES (1,'¿En qué año se fundó el instituto?','1983','1973','1960','1990',1),(2,'¿Cuál fue el nombre del establecimiento educativo cuando se fundó?','Santa Victoria','Colón','San Francisco de Asís','Santísima Trinidad',3),(3,'¿En qué año se convierte a colegio Nacional?','1985','1963','1993','2001',1),(4,'¿Cuántos directores tuvo el Instituto hasta la fecha?','1','23','10','4',4),(5,'¿Cuántas carreras se dictan actualmente en el ISAUI ?','2','6','4','10',2),(6,'¿Qué significa workshop?','Muestra de fin de año','Espacio de encuentro','Exposición de Carreras','Conferencias',1),(7,'¿Qué carrera fue la pionera con los viajes en las materias de prácticas?','Trekking','Enfermeria','Desarrollo de Software','Técnico y Guía Superior en Turismo',4),(8,'¿Cómo era el edificio  educativo en sus comienzos?','Ambiente al aire libre','Una casa que se convertia en colegio','El edificio actual','Solo planta baja',2),(9,'¿ISAUI es un Instituto público?','Siempre lo fue','Es privado','En sus comienzos fue público','Desde el 2010 es privado',1),(10,'¿A partir de que año la cooperadora empezó a construir las aulas?','1986','1980','2000','2010',1),(11,'¿De donde provenia el dinero?','Estado','Bono contribución de los padres','Profesores','Instituto',2),(12,'¿Quién era el presidente de la cooperadora en ese entonces?','Sr Roomberg','Sr Alvarez','Sr Diaz','Sr Gatica',4),(13,'¿Quién es el presidente de la cooperadora actualmente?','Sofia Vergara','Claudia Estebanez','Daniela Maschio','Alejandra Nomina',3),(14,'¿En que presidencia se logró la nacionalización?','Alfonsín','Sarmiento','Menem','Peron',1);
/*!40000 ALTER TABLE `preguntas_respuestas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_de_usuario` varchar(255) NOT NULL,
  `instagram` varchar(255) DEFAULT NULL,
  `puntaje` int NOT NULL,
  `tiempo` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1085 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1084,'Matias','alvarezmati_',1400,38);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-30 17:13:29
