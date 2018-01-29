drop table if exists images;
create table images (
    id integer primary key autoincrement,
    url text not null,
    time_taken timestamp not null
);