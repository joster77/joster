create database clientesdb;
use clientesdb;
create table usuarios(
id int auto_increment primary key not null,
nombres varchar(50),
apellidos varchar(50),
sexo varchar(20)
);

insert into usuarios values (null,"José","Terrones","Masculino");

select *  from usuarios