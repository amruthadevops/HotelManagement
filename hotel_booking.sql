-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
-- Host: localhost    Database: hotel
-- ------------------------------------------------------
-- Server version 8.0.31

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

-- Drop the table if it exists
DROP TABLE IF EXISTS `booking`;

-- Create the table with proper data types
CREATE TABLE `booking` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `customer_name` VARCHAR(100) NOT NULL,
  `room_type` VARCHAR(50) NOT NULL,
  `num_of_guests` INT NOT NULL,
  `check_in` DATE NOT NULL,
  `check_out` DATE NOT NULL,
  `num_of_days` INT NOT NULL,
  `amount` DECIMAL(10,2) NOT NULL,
  `status` ENUM('confirmed', 'not confirmed', 'cancelled') DEFAULT 'not confirmed'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Insert sample data
INSERT INTO `booking` (`customer_name`, `room_type`, `num_of_guests`, `check_in`, `check_out`, `num_of_days`, `amount`, `status`) 
VALUES 
  ('JK', 'AC Double Room', 2, '2022-12-29', '2022-12-30', 1, 2000.00, 'not confirmed'),
  ('JK', 'AC Single Room', 1, '2022-12-30', '2023-01-02', 3, 4500.00, 'not confirmed');

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-29  6:31:28
