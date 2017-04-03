---
title: Intro to SQL
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to SQL
Week 5 | Lesson 5.02

## Connecting to a Local Database
A database can be local or remote, it can span a single machine or it can be distributed with replicated data over several machines. The latter configuration is called _sharding_.

Let's start by connecting to a local _sqlite_ database.

### SQLite

**[SQLite](https://sqlite.org/)** is a database software package built on the Structured Query Language [(SQL)](https://en.wikipedia.org/wiki/SQL).  It is similar to other SQL databases, such as [PostgreSQL](http://www.postgresql.org/), [MySQL](https://www.mysql.com/), Oracle, and Microsoft SQL Server, except that it is *file-based*, rather than *server-based*.  This makes it easy to setup and use for small projects, but less suitable for production environments.  Once you are familiar with sqlite, the same ideas, and similar syntax, can be applied to other SQL databases.

SQLite v3 is bundled with most Python distributions (including our Anaconda distribution).  You might also find it useful to install [SQLite Manager](https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/?src), a Firefox add-on for viewing SQLite database files via a simple GUI.

#### Interacting with SQLite
There are multiple ways of interacting with an SQLite database, including:

1. SQLite Command Line Utility
2. python `sqlite3` package
3. `pandas` SQL Interface
4. High-level ORMs (e.g. sqlalchemy, django ORM, etc.)

Let's start with method 1. All of these methods provide some form of wrapper, or set of convenience functions, for interacting with SQLite.  Behind the scenes, the Structured Query Language (SQL) itself defines the interface to the database software.  This underlying SQL syntax will be visible to a greater or lesser degree depending upon the method that is chosen.

#### Common SQL Command Patterns
The SQL command set has a rich syntax with numerous options, but most of the commonly used commands follow a few simple patterns.  A basic familiarity of these patterns is helpful when working in SQL:

    CREATE TABLE ...
    ALTER TABLE ... ADD COLUMN ...
    INSERT INTO ... VALUES ...
    UPDATE ... SET ... WHERE ...
    SELECT ... FROM ... WHERE ...
    SELECT ... FROM ... JOIN ... ON ...
    DELETE FROM ... WHERE ...

### 1. SQLite Command Line Utility

The first method we'll explore is connecting to SQLite via the built-in [command line utility](https://www.sqlite.org/sqlite.html).  

> Note: the commands in this section should be executed within your normal terminal shell.

To start a new session of the interpreter, simply open your terminal and type `sqlite3`, followed by the name of the database file.  If the file does not yet exist, sqlite will create it.

    $ sqlite3 test1.sqlite

    SQLite version 3.7.12 2012-04-03 19:43:07
    Enter ".help" for instructions
    Enter SQL statements terminated with a ";"
    sqlite>

Notice that your terminal prompt changes to `sqlite>`, indicating that you are now entering commands into the sqlite command line utility.  Take a quick look at the help command:

    sqlite> .help
Display the current databases - you should see the new file `test1.sqlite`:

    sqlite> .databases

#### Creating tables and adding columns
Create an table called `table1` with a single column `field1` containing an INTEGER PRIMARY KEY:

    sqlite> CREATE TABLE table1 (field1 INTEGER PRIMARY KEY);

Add a few more columns to `table1`:

    sqlite> ALTER TABLE table1 ADD COLUMN field2 VARCHAR(16);
    sqlite> ALTER TABLE table1 ADD COLUMN field3 REAL;
    sqlite> ALTER TABLE table1 ADD COLUMN field4 TEXT;

Notice the different field types in the ALTER TABLE commands.  SQLite supports several different [field types](https://www.sqlite.org/datatype3.html), including INTEGERS, variable length VARCHAR character fields (with a max length), TEXT fields, and 'REALS', which are used to store floating point numbers.

Verify that the table was created:

    sqlite> .tables

You can check the `schema` of the table using `.schema`, which shows the commands that would be needed to create the database tables from scratch.  

    sqlite> .schema

Notice that in this case, our `table1` could have been created with a single command, rather than adding each column separately.


#### Adding data
Let's add some data:

    sqlite> INSERT INTO table1 VALUES (1, 'Henry James', 42, '75 Mission Street, San Francisco, CA');
    sqlite> INSERT INTO table1 VALUES (2, 'Carol James', 40, '75 Mission Street, San Francisco, CA');
    sqlite> INSERT INTO table1 VALUES (3, 'Jesse James', 12, '75 Mission Street, San Francisco, CA');

Notice that the first column has unique values - this is a requirement for the PRIMARY KEY column.  If we try to add a record using an existing PK value we'll get an error:

    sqlite> INSERT INTO table1 VALUES (3, 'Julie James', 10, '75 Mission Street, San Francisco, CA');
    Error: PRIMARY KEY must be unique

Fortunately, SQLite has some built in functionality to auto-increment the PK value - just set the value of the PK field to NULL when doing the INSERT and it will automatically be set to a valid value.

    sqlite> INSERT INTO table1 VALUES (NULL, 'Julie James', 10, '75 Mission Street, San Francisco, CA');

Notice that the value in `field1` for the Julie James record has been automatically set to 4.

#### Updating records
Suppose we need to update an existing record with new data - e.g. maybe Julie James is only 9.  For this we use the UPDATE command with the WHERE option:

    sqlite> UPDATE table1 SET field3=9 WHERE field1=4;

#### Removing Records
To remove records use the DELETE command:

    sqlite> DELETE FROM table1 WHERE field2 like '%Jesse%';

Use SQLite-Manager to verify that the Jesse James record has been removed.  To exit the sqlite interpreter type `.exit`.

    sqlite>  .exit

#### Selecting Certain Records
To select only a certain number of records, use the LIMIT option:

    sqlite> SELECT * FROM table1 LIMIT 2;
    
To select only records that meet a certain condition, use the WHERE option:

    sqlite> SELECT * FROM table1 WHERE field1 IS 3;

To select the count of records meeting a certain condition, use the WHERE option:

    sqlite> SELECT count(*) FROM table1 WHERE field1 >= 2;
    
To order the returned results, use the ORDER BY option:

    sqlite> SELECT * FROM table1 ORDER BY field3;
    sqlite> SELECT * FROM table1 ORDER BY field3 ASC;
    sqlite> SELECT * FROM table1 ORDER BY field3 DESC;


### Comparing SQLite with MySQL and PostgreSQL
|Task|MySQL|PostgreSQL|SQLite|
|---|---|---|---|
|Connect to a database|mysql &lt;dbname&gt;| psql &lt;dbname&gt;|sqlite3 &lt;filename&gt;|
|Client help|help contents|\?|.help|
|SQL help|help contents|\h|n/a|
|List databases|SHOW DATABASES;|\l|.databases|
|Change database|USE &lt;dbname&gt;|\c <dbname&gt;|n/a|
|List tables|SHOW TABLES;|\dt|.tables|
|Show table|info DESCRIBE &lt;tablename&gt;|\d &lt;tablename&gt;|.schema &lt;tablename&gt;|
|Load data|LOAD DATA INFILE &lt;file&gt; |\i &lt;file&gt;|.import &lt;file&gt; &lt;table&gt;|
|Export data|SELECT ... INTO OUTFILE &lt;file&gt;|\o &lt;file&gt;|.dump &lt;table&gt;|
|Exit the client|quit (or exit)| \q|.exit|

## Independent Practice

Now that you are able to connect to a local or remote database try some of the following:

- create a new table in the database
- add data
- remove data
- alter tables
- list tables
- list schemas
- create a new database
- drop a table
- drop a database
- read the help

<a name="conclusion"></a>
## Conclusion
Relational databases are the most common. They organize data into tables. Other database types exist, including graph, hash, documents and time-series specific databases.
The simplest local database is _sqlite_ and we learned how to add and remove data from it.

### ADDITIONAL RESOURCES

- [Practice with SQL Zoo](http://www.sqlzoo.net/wiki/SQL_Tutorial)
- [Database page on Wikipedia](https://en.wikipedia.org/wiki/Database)
- [Database tutorials](http://www.tutorialspoint.com/database_tutorials.htm)
- [Postgres Cheat Sheet](https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546)
