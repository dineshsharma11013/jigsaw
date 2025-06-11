-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2024 at 10:24 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jigsaw`
--

-- --------------------------------------------------------

--
-- Table structure for table `blogs`
--

CREATE TABLE `blogs` (
  `id` int(11) NOT NULL,
  `img` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `msg` text NOT NULL,
  `url` text NOT NULL,
  `tags` varchar(255) NOT NULL,
  `rem_addr` varchar(100) NOT NULL,
  `status` enum('1','2') NOT NULL DEFAULT '1' COMMENT '1-active, 2-disable',
  `created_at` varchar(100) NOT NULL,
  `updated_at` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blogs`
--

INSERT INTO `blogs` (`id`, `img`, `title`, `msg`, `url`, `tags`, `rem_addr`, `status`, `created_at`, `updated_at`) VALUES
(1, 'sdf', '', 'test2', '', 'test2@gmail.com', '127.0.0.1', '1', '', ''),
(4, '2df59869-a085-49be-8456-88301b56a36f.png', '', 'test2', '', 'test2@gmail.com', '127.0.0.1', '1', '2024-07-17 11:46:14.826780', ''),
(5, '', 'hello world', 'test2', 'hello-world', 'test2@gmail.com', '127.0.0.1', '1', '2024-07-17 12:12:16.289928', ''),
(6, '', 'hello world', 'test221', 'hello-world', 'test2@gmail.com', '127.0.0.1', '1', '2024-07-17 13:04:01.675978', '2024-07-17 13:34:49.843755');

-- --------------------------------------------------------

--
-- Table structure for table `enquiry_mdl`
--

CREATE TABLE `enquiry_mdl` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `phone` varchar(150) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `message` text NOT NULL,
  `rem_addr` varchar(100) NOT NULL,
  `created_at` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `enquiry_mdl`
--

INSERT INTO `enquiry_mdl` (`id`, `name`, `email`, `phone`, `subject`, `message`, `rem_addr`, `created_at`) VALUES
(1, 'test', 'test@gmail.com', '234234', 'test', '', '', ''),
(2, 'test2', 'test2@gmail.com', '324234', 'test2', 'hello world', '127.0.0.1', '2024-07-11 18:53:57.715120');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blogs`
--
ALTER TABLE `blogs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `enquiry_mdl`
--
ALTER TABLE `enquiry_mdl`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blogs`
--
ALTER TABLE `blogs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `enquiry_mdl`
--
ALTER TABLE `enquiry_mdl`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
