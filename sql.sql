create database Greenpeace;
use Greenpeace;

create table Usuario(
	nome varchar(30) not null,
    tempo timestamp,
    derretimento int not null,
    elevacao int not null
    
);
select * from Usuario;