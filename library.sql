DROP DATABASE IF EXISTS mvp1;

CREATE DATABASE IF NOT EXISTS mvp1;

use mvp1;

CREATE TABLE clientes (
	id integer not null auto_increment,
    nome varchar(100) not null,
    sobrenome varchar(100) not null,
    telefone varchar(11),
    cpf char(11) unique,
    PRIMARY KEY (id)
);

CREATE TABLE livros (
	id integer not null auto_increment,
    titulo varchar(100) not null,
    editora varchar(100),
    autor varchar(100),
    ano integer,
    locado_por integer,
    locado_em date,
    PRIMARY KEY (id),
    FOREIGN KEY (locado_por) REFERENCES clientes(id)
);

INSERT INTO livros (titulo, editora, autor, ano)
	VALUES
    ('Harry Potter e a Pedra Filosofal', 'Rocco', 'J.K. Rowling', 1997),
    ('1984', 'Companhia das Letras','George Orwell', 1949),
    ('O Hobbit', 'HarperCollins', 'J.R.R. Tolkien', 1937),
    ('Frankenstein', 'Darksider', 'Mary Shalley', 1818),
    ('O Código Da Vinci', 'Sextante', 'Dan Brown', 2000),
    ('Drácula', 'Darksider', 'Bram Stoker', 1897),
    ('It: A coisa', 'Suma', 'Stephen King', 1986),
    ('A Batalha do Apocalipse', 'Verus', 'Eduardo Spohr', 2007),
    ('Filhos do Éden: Herdeiros de Atlântida', 'Verus', 'Eduardo Spohr', 2011),
    ('O Senhor dos Anéis: A Sociedade do Anel', 'HarperCollins', 'J.R.R. Tolkien', 1954);
    
INSERT INTO clientes (nome, sobrenome, telefone, cpf)
	VALUES
			