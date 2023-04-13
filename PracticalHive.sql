set hive.support.concurrency=true;
set hive.enforce.bucketing=true;
set hive.exec.dynamic.partition.mode=nonstrict;
set hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager;
set hive.compactor.initiator.on=true;
set hive.compactor.worker.threads=10;

create table fctpersonaccount(
    personaccountkey bigint, personkey bigint, accountkey bigint, balance decimal(18,9)) clustered by (personkey, accountkey) into 1 buckets stored as orc tblproperties('transactional'='true', 'orc.compress'='ZLIB', 'orc.create.index'='true');

create table report002( accountnumber int, last_balance decimal(18,9)) clustered by (accountnumber, last_balance) into 1 buckets stored as orc tblproperties('transactional'='true', 'orc.comporess'='ZLIB', 'orc.create.index'='true');

insert into table report002 select dimaccount.accountnumber, sum(fctpersonaccount.balance) as last_balance from organisedb.fctpersonaccount join organisedb.dimaccount on fctpersonaccount.accountkey = dimaccount.accountkey
    group by dimaccount.accountnumber;

insert into table organisedb.fctpersonaccount select distinct personaccountkey, personkey, accountkey, balance from transformdb.fctpersonaccount where personaccountkey=1 order by personaccountkey, personkey, accountkey;


load data local inpath '/mnt/f/book_data/PracticalHive/ESM-Ch-5-and-8-ExampleData/datawarehouse/00rawdata/rawfirstname.csv' overwrite into table retrievedb.rawfirstname;


 create table retrievedb.rawlastname ( lastnameid string, lastname string ) row format delimited fields terminated
 by ',';

 load data local inpath '/mnt/f/book_data/PracticalHive/ESM-Ch-5-and-8-ExampleData/datawarehouse/00rawdata/rawlastname.csv' overwrite into table retrievedb.rawlastname;

  load data local inpath '/mnt/f/book_data/PracticalHive/ESM-Ch-5-and-8-ExampleData/datawarehouse/00rawdata/rawperson.csv' overwrite into table retrievedb.rawperson;

  load data local inpath '/mnt/f/book_data/PracticalHive/ESM-Ch-5-and-8-ExampleData/datawarehouse/00rawdata/rawdatetime.csv' overwrite into table retrievedb.rawdatetime;

  load data local inpath '/mnt/f/book_data/PracticalHive/ESM-Ch-5-and-8-ExampleData/datawarehouse/00rawdata/rawaddress.csv' overwrite into table rawaddress;

load data local inpath '/mnt/f/book_data/PracticalHive/ESM-Ch-5-and-8-ExampleData/datawarehouse/00rawdata/rawaddresshistory.csv' overwrite into table rawaddresshistory;  

load data local inpath '/mnt/f/book_data/PracticalHive/ESM-Ch-5-and-8-ExampleData/datawarehouse/00rawdata/rawaccount.csv' overwrite into table rawaccount;

 create table assessdb.firstname003(firstnameid string, firstname string, sex string) clustered by (firstnameid) into 1 buckets stored as orc tblproperties('transactional'='true', 'orc.compress'='ZLIB', 'orc.create.index'='true');

insert into table assessdb.firstname003 select cast(firstnameid as int), substring(firstname, 2, length(firstname)-2), substring(sex, 2, length(sex)-2) from assessdb.firstname002;


 create table assessdb.lastname001(
lastnameid string,
lastname string
)
clustered by (lastnameid) into 1 buckets stored as orc tblproperties('transactional'='true', 'orc.comporess'='ZLIB', 'orc.create.index'='true');

create table if not exists assessdb.lastname ( lastnameid string, lastname string) clustered by (lastnameid) into 1 buckets stored as orc tblproperties('transactional'='true', 'orc.compress'='ZLIB', 'orc.create.index'='true');

 create table assessdb.person001 ( persid string, firstnameid string, lastnameid string ) clustered by (persid) into 1 buckets stored as orc tblproperties('transactional'='true', 'orc.compress'='ZLIB', 'orc.create.index'='true');

insert into table assessdb.personfull select person.persid, person.firstnameid, firstname.firstname, person.lastnameid, lastname.lastname, firstname.sex from assessdb.firstname join assessdb.person on firstname.firstnameid = person.firstnameid join assessdb.lastname on lastname.lastnameid = person.lastnameid;

insert into table assessdb.datetime003
select 
    cast(id as int), substring(datetimes, 2, length(datetimes)-2),
    substring(monthname, 2, length(monthname)-2), cast(yearnumber as int),
    cast(monthnumber as int), cast(daynumber as int), cast(hournumber as int),
    cast(minutenumber as int), substring(ampm, 2, length(ampm)-2)
from assessdb.datetime002;