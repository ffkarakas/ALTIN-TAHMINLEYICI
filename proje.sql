-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: localhost
-- Üretim Zamanı: 20 Ağu 2020, 10:22:36
-- Sunucu sürümü: 8.0.17
-- PHP Sürümü: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `proje`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `altin`
--

CREATE TABLE `altin` (
  `alis` decimal(10,2) NOT NULL,
  `satis` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `altin`
--

INSERT INTO `altin` (`alis`, `satis`) VALUES
('468.16', '466.79'),
('468.16', '466.79'),
('457.55', '457.76'),
('456.00', '455.00'),
('456.00', '455.00'),
('456.00', '456.00'),
('456.00', '456.00'),
('456.00', '456.00'),
('457.00', '457.00'),
('457.00', '457.00'),
('457.79', '457.62'),
('457.79', '457.62'),
('457.00', '457.00'),
('457.93', '457.89'),
('457.74', '457.77');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
