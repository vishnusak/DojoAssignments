-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema myposts
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema myposts
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `myposts` DEFAULT CHARACTER SET utf8 ;
USE `myposts` ;

-- -----------------------------------------------------
-- Table `myposts`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `myposts`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `post` TEXT NOT NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
