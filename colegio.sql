-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-07-2025 a las 19:15:22
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `colegio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id` int(11) NOT NULL,
  `DNI` int(15) NOT NULL,
  `nombres` varchar(120) NOT NULL,
  `apellidos` varchar(120) NOT NULL,
  `sexo` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish2_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id`, `DNI`, `nombres`, `apellidos`, `sexo`) VALUES
(37, 27120960, 'Rafael', 'Drayer', 'Masculino'),
(50, 4859769, 'Juan Manuel', 'Reyes', 'Masculino'),
(51, 8974521, 'Diana Luisa', 'Montes', 'Femenino'),
(61, 9624558, 'Rodolfo', 'Solano', 'Masculino'),
(64, 1926771, 'Francisco luis', 'Rojas', 'Masculino'),
(66, 15982700, 'Valeria', 'Montes', 'Femenino'),
(67, 12647102, 'Ricardo jose', 'Mejías', 'Masculino'),
(68, 23790111, 'María', 'Fernández', 'Femenino'),
(69, 28203660, 'Manuel Alejandro', 'Reyes Mosqueda', 'Masculino'),
(70, 7634827, 'Trina', 'Bordones', 'Femenino'),
(71, 19786888, 'Xiomara', 'Guzmán', 'Femenino'),
(91, 8944752, 'Mary', 'Colina', 'Femenino'),
(92, 26741859, 'Norma', 'Bustillos', 'Masculino'),
(93, 25104385, 'Irama', 'Gómez', 'Masculino'),
(94, 12910632, 'Ronny', 'Reyes', 'Masculino'),
(95, 9829549, 'Milagro Coromoto', 'Moreno', 'Femenino'),
(96, 1528478, 'Celido', 'Silva', 'Masculino'),
(97, 2168512, 'Mariuska', 'Rivero', 'Femenino'),
(98, 1682069, 'Flor', 'Pérez', 'Femenino'),
(99, 18335240, 'Gimena', 'Cardozo', 'Femenino'),
(100, 20697420, 'Diego', 'Nuñez', 'Masculino'),
(101, 2568261, 'Perla', 'Moonroy', 'Femenino'),
(102, 1478396, 'Julio', 'Rengifo', 'Masculino'),
(103, 1560782, 'Guzstavo', 'Castillo', 'Masculino'),
(104, 1496751, 'Ramón', 'Rojas', 'Masculino'),
(105, 10205649, 'Silvana', 'Rodríguez', 'Femenino'),
(106, 8025909, 'Yanet', 'Mijares', 'Femenino'),
(107, 1746017, 'José Rafael', 'Durand', 'Masculino'),
(108, 21212211, 'iuytiuytiut', 'poipoioiip', 'Masculino');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
