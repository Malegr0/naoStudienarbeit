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
of Economics and Law. This repository represents the server-side of this project. The client-side can be found HERE. As server we are using a Raspberry Pi 4 but any linux
based system will be ok.

### Build With
This project was built using following frameworks:
  - [SpaCy](https://spacy.io/)
  - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  - [MariaDB Connector](https://mariadb.com/de/resources/blog/how-to-connect-python-programs-to-mariadb/)

For this project we are using the german trained pipeline for SpaCy. Other pipelines can be found [here](https://spacy.io/usage).
Note that you can't use our database if you are using another pipelines and/or languages.

## Getting Started
This project is written in python 3.9

### Prerequisites
Pip is needed for the following installation.
MariaDB and their dependencies (libmariadb3 and libmariadb-dev) must be installed on the same device on which the code is executed.

### Installation
1. Clone the repo
```
git clone https://github.com/Malegr0/naoStudienarbeit.git
```
2. Install packages
```
pip3 install -U spacy==3.0.6
python -m spacy download de_core_news_sm
pip3 install flask
pip3 install mariadb
```

### Database Setup
1. Open the terminal and login to MariaDB with your username and password.
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
create table nao.matching_table (caseID int, keywords text, answer text);
```
6. Create a user to access the database. (You can change the credentials but keep in mind that you have to change it in the script as well.)
```
create user 'naouser'@'localhost' identified by 'Asube-2015!';
grant all privileges on nao.* 'naouser'@'localhost';
```

### Insert Data
1. Open another terminal.
2. Navigate to the folder data_inserter in the cloned repository.
3. Run main.py to fill each tables with our data.
```
python main.py
```
