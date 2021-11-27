-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema proyecto_sentiments2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema proyecto_sentiments2
-- -----------------------------------------------------
DROP DATABASE IF EXISTS proyecto_sentiments2;
CREATE SCHEMA IF NOT EXISTS `proyecto_sentiments2` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `proyecto_sentiments2` ;

-- -----------------------------------------------------
-- Table `proyecto_sentiments2`.`AUTHOR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_sentiments2`.`AUTHOR` (
  `idAutor` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idAutor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_sentiments2`.`AUTHORS_SEVERAL GENRES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_sentiments2`.`AUTHORS_SEVERAL GENRES` (
  `idAUTHORS_SEVERAL GENRES` INT NOT NULL AUTO_INCREMENT,
  `AUTHOR_idAutor` INT NOT NULL,
  `GENRE_idGenre` INT NOT NULL,
  PRIMARY KEY (`idAUTHORS_SEVERAL GENRES`, `AUTHOR_idAutor`, `GENRE_idGenre`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_sentiments2`.`GENRE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_sentiments2`.`GENRE` (
  `idGenre` INT NOT NULL AUTO_INCREMENT,
  `Genre` VARCHAR(45) NULL,
  PRIMARY KEY (`idGenre`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `proyecto_sentiments2`.`QUOTES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proyecto_sentiments2`.`QUOTES` (
  `idFrases célebres` INT NOT NULL AUTO_INCREMENT,
  `Frases` VARCHAR(200) NULL,
  `AUTHOR_idAutor` INT NOT NULL,
  `GENRE_idGenre` INT NOT NULL,
  PRIMARY KEY (`idFrases célebres`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
