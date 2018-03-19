drop table if exists images;
create table images (
    id integer primary key autoincrement,
    image_path text not null,
    time_taken timestamp not null
);

drop table if exists settings;
create table settings (
    time_set timestamp primary key not null,
    danger integer not null,
    environment integer not null,
    state integer not null,
);