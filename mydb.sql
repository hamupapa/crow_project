-- データベースの作成
create database mydb;

-- テーブルの作成
create table idtbl (
    id int,
    name varchar(20)
);

-- データの挿入
insert into idtbl values(1, 'Yamada Taro'), (2, 'Sato Jiro'), (3, 'Suzuki Saburo');
