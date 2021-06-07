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
Note that you can't use our database if you are using another pipeline.

## Getting Started
This project is written in python 3.

### Prerequisites
Pip is needed for the following installation.
MariaDB must be installed on the same device on which the code is executed.

### Installation
1. Clone the repo
```
git clone https://github.com/Malegr0/naoStudienarbeit.git
```
2. Install packages
```
pip install -U spacy
python -m spacy download de_core_news_sm
pip install flask
pip3 install mariadb
```

### Database Setup
1. Open the terminal and login to MariaDB with your username and password.
```
sudo mariadb --user YOUR_USERNAME -p
```
2. If u are logged in then create a database called nao.
```
create database nao;
```
3. Create a table called synonyms.
```
create table nao.synonyms(word varchar(255), synonym varchar(255);
```
4. Create a table called answers.
```
Needs to be completed.
```

### Insert Data
1. Open another terminal.
2. Navigate to FOLDER in the cloned repository.
3. Run FILE.py to fill both tables with our data.
```
python FILE.py
```
