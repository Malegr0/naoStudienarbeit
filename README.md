# naoStudienarbeit

## Table of contents
* [About The Project](#about-the-project)
  * [Build With](#build-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Database Setup](#database-setup)
  * [Insert Data](#insert-data)

## About The Project
This project is about understanding german spoken language using the robot NAO and natural language processing. The result is going to be presented at the Berlin School
of Economics and Law. This repository represents the server-side of this project. The client-side can be found [HERE](https://github.com/Malegr0/naoClient). As a server we are using a Linux based system.

### Build With
This project was built using following frameworks:
  - [SpaCy](https://spacy.io/)
  - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  - [MariaDB Connector](https://mariadb.com/de/resources/blog/how-to-connect-python-programs-to-mariadb/)

For this project we are using the german trained pipeline for SpaCy. Other pipelines can be found [here](https://spacy.io/usage).
Note that you can't use our database if you are using another pipelines and/or languages.

## Getting Started
This project is written in Python 3.9

### Prerequisites
Pip and Pipenv is needed for the following installation.
MariaDB and their dependencies (libmariadb3 and libmariadb-dev) must be installed on the same device on which the code is executed.

### Installation
1. Clone the repo
```
git clone https://github.com/Malegr0/naoStudienarbeit.git
```
2. Open a terminal, navigate into the repository and install packages
```
pipenv install
```

### Database Setup
1. Open another terminal and login to MariaDB with your username and password.
```
mariadb -u YOUR_USERNAME -p
```
2. If u are logged in then create a database called nao.
```
create database nao;
```
3. Create a table called synonyms.
```
create table nao.synonyms (synonym varchar(255), id int);
```
4. Create a table called generic_terms.
```
create table nao.generic_terms (id int, generic_term varchar(255));
```
5. Create a table called matching_table.
```
create table nao.matching_table (caseID int, primary_keywords text, secondary_keywords text, answer text);
```
6. Create a table called weights.
```
create table nao.weights (keyword text, weight float);
```
7. Create a user to access the database. (You can change the credentials but keep in mind that you have to change it in the script as well.)
```
create user 'naouser'@'localhost' identified by 'Asube-2015!';
grant all privileges on nao.* 'naouser'@'localhost';
```

### Run the script and insert Data
1. Open a terminal and navigate to the project repository.
2. (Optional) To insert data run this command.
```
python3 main.py -i
```
3. To run the server use
```
python3 main.py -r
```
For further information use
```
python3 main.py -h
```
