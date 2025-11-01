FIRST LAUNCH:
On first launch you'll have to create admin:
> python create_admin.py 
enter admin name and password. That'll save admin info to Database,

After that you can login to the site:
>/login
No buttons, just append /login to your current site url,
> /logout for logout duh.

When logged in, you can add/edit/delete bunch of stuff:
> projects
> status
> about

To change bootom links, you'll have to change source code in index.html.
To change or delete William Dafoe picture (I wouldn't dare), check
images directory and change file, keeping the same name. Or, if you feeling
like advanced user, change file, it's name and source proper link in index.html 

About, Status, Picture are buttons that pop-up using JS script.


FOR HEROKU USERS:
For those like me, using SQLite database deploying site to Heroku, good luck.
You'll encounter some trobules because of database. It'll force you to migrate to
Postgresql (check Chatgpt or docs for that). Also, to initialise About, Status, 
Project tables, you'll have to run:
> heroku run python About_Status_Project_create_table.py and then it should work.

