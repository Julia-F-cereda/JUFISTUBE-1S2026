CREATE DATABASE IF NOT EXISTS jufisTube;
USE jufisTube;

CREATE TABLE IF NOT EXISTS genero (
 nome_genero VARCHAR(30) NOT NULL PRIMARY KEY ,
 icone VARCHAR(100),
 cor VARCHAR(10)
);


CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 cantor VARCHAR(50),
 duracao TIME(6),
 nome VARCHAR(50),
 url_imagem VARCHAR(255),
 nome_genero VARCHAR(30),
 ativo bool default 0,
 CONSTRAINT FK_musica_genero foreign key (nome_genero) REFERENCES genero (nome_genero)
);

CREATE TABLE IF NOT EXISTS cadastro (
nome varchar(50)NOT NULL PRIMARY KEY,
senha varchar(100) NOT NULL
);

