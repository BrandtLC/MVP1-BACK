
# Api Gerenciamento de Livraria

Esse é um breve código backend criado durante o desenvolvimento do primeiro MVP do curso de pós-gaduação em Engenharia de Software da PUC-Rio.

Consiste em uma API para o gerenciamento de uma biblioteca, possibilitando a criação e remoção de livros e usuários assim como gerenciar o processo de locação de livros.

Também é fornecido um arquivo `library.sql` com todo o script utilizado para a criação do banco, tabelas e entrada inicial de dados no banco de dados MySQL.


## Iniciando

Antes da primeira execução será necessário efetuar a instalação de todas as dependencias do projeto listadas no arquivo `requirements.txt`. É recomendada a utilização de um ambiente virtual para gerenciar essas dependencias.

Para instalar as dependencias é necessário rodar o seguinte comando em um terminal localizado na raiz do projeto.

```bash
  pip install -r requirements.txt
```

Para iniciar API basta rodar o aquivo principal do projeto
```bash
  python3 -m main.py
```