drop table if exists keys;
create table keys (
  id integer primary key autoincrement,
  text text not null
);
drop table if exists surveys;
create table surveys (
  id integer primary key autoincrement,
  survey_id integer not null
);

