-- schema.sql

drop database if exists dbfbreack;

create database dbfbreack;

use dbfbreack;

grant select, insert, update, delete on dbfbreack.* to 'root'@'localhost' identified by 'zengyong';

create table users (
    `id` varchar(50) not null,
    `name` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `created_at` real not null,
    unique key `idx_name` (`name`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table products (
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `cpmc` varchar(50) not null,
    `cplb` varchar(20) not null,
    `xwdm` varchar(20) not null,
    `zqzh` varchar(20) not null,
    `zjzh` varchar(20) not null,
    `qzmm` bool not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table files (
    `id` varchar(50) not null,
    `wjlb` varchar(20) not null,
    `wjlj` varchar(50) not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;
