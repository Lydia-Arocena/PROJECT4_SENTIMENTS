-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema proyecto_sentiments
-- -----------------------------------------------------
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`AUTHOR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`AUTHOR` (
  `idAutor` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idAutor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`GENRE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`GENRE` (
  `idGenre` INT NOT NULL AUTO_INCREMENT,
  `Genre` VARCHAR(45) NULL,
  PRIMARY KEY (`idGenre`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`QUOTES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`QUOTES` (
  `idFrases célebres` INT NOT NULL AUTO_INCREMENT,
  `Frases` VARCHAR(45) NULL,
  `AUTHOR_idAutor` INT NOT NULL,
  `GENRE_idGenre` INT NOT NULL,
  PRIMARY KEY (`idFrases célebres`),
  INDEX `fk_QUOTES_AUTHOR_idx` (`AUTHOR_idAutor` ASC) VISIBLE,
  INDEX `fk_QUOTES_GENRE1_idx` (`GENRE_idGenre` ASC) VISIBLE,
  CONSTRAINT `fk_QUOTES_AUTHOR`
    FOREIGN KEY (`AUTHOR_idAutor`)
    REFERENCES `mydb`.`AUTHOR` (`idAutor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_QUOTES_GENRE1`
    FOREIGN KEY (`GENRE_idGenre`)
    REFERENCES `mydb`.`GENRE` (`idGenre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`AUTHORS_SEVERAL GENRES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`AUTHORS_SEVERAL GENRES` (
  `idAUTHORS_SEVERAL GENRES` INT NOT NULL AUTO_INCREMENT,
  `AUTHOR_idAutor` INT NOT NULL,
  `GENRE_idGenre` INT NOT NULL,
  PRIMARY KEY (`idAUTHORS_SEVERAL GENRES`, `AUTHOR_idAutor`, `GENRE_idGenre`),
  INDEX `fk_AUTHORS_SEVERAL GENRES_AUTHOR1_idx` (`AUTHOR_idAutor` ASC) VISIBLE,
  INDEX `fk_AUTHORS_SEVERAL GENRES_GENRE1_idx` (`GENRE_idGenre` ASC) VISIBLE,
  CONSTRAINT `fk_AUTHORS_SEVERAL GENRES_AUTHOR1`
    FOREIGN KEY (`AUTHOR_idAutor`)
    REFERENCES `mydb`.`AUTHOR` (`idAutor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_AUTHORS_SEVERAL GENRES_GENRE1`
    FOREIGN KEY (`GENRE_idGenre`)
    REFERENCES `mydb`.`GENRE` (`idGenre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
