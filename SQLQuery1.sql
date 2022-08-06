Create database Movies_2

Create table Director
(
Directorid int identity(1,1) not null,
Director_FirstName varchar(15),
Director_LastName varchar(15),
Constraint Director_PK primary key(DirectorID)

)

Create table Star
(
Starid int identity(1,1) not null,
Star_FirstName varchar(15),
Star_LastName varchar(15),
Constraint Star_PK primary key(StarID)

)

Create table Genre
(
Genreid int identity(1,1) not null,
Genre varchar(15),
Constraint Genre_PK primary key(GenreID)

)

Create table Movies(
MovieID int identity (1,1) not null,
Title varchar(35) not null,
DirectorID int not null,
StarID int not null,
GenreID int not null,
rating numeric(3,1) not null,
Constraint movies_pk primary key(MovieID)
);

Alter table Movies
add constraint Movies_FK1
foreign key(DirectorID) references Director(DirectorID)

Alter table Movies
add constraint Movies_FK2
foreign key(StarID) references Star(StarID)

Alter table Movies
add constraint Movies_FK3
foreign key(GenreID) references Genre(GenreID)