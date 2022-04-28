-- 創建 Database
CREATE DATABASE IF NOT EXISTS awan_project;

-- 使用資料庫
USE awan_project;

-- 創建 user table
CREATE TABLE IF NOT EXISTS user(
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(20) NOT NULL,
    name VARCHAR(20) NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL,
    time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- 創建 symptoms table
CREATE TABLE IF NOT EXISTS symptoms(
    id INT NOT NULL AUTO_INCREMENT,
    symptom_name VARCHAR(255),
    PRIMARY KEY (id)
);

-- 創建 departments table
CREATE TABLE IF NOT EXISTS departments(
    id INT NOT NULL AUTO_INCREMENT,
    symptoms_id INT NOT NULL,
    department VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (symptoms_id) REFERENCES symptoms (id)
);