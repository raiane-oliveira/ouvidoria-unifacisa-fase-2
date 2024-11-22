create schema ouvidoria;

use ouvidoria;

create table manifestacao(
codigo int auto_increment,
conteudo varchar(150),
tipo varchar (30),
autor varchar (30),
createdAt datetime default
 current_timestamp,
 primary key (codigo)
);