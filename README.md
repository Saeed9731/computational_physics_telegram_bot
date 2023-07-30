

# What is this project?
This is a boilerplate to start a telebot project.

# How to use?

<strong>If you want to get notified about the future changes Follow my github account.</strong>

First clone the project.

```bash
git clone https://github.com/Saeed9731/computational_physics_telegram_bot.git
```

Then make sure Docker is running.
* If you are on windows click on the Docker Desktop icon and wait for about a minute.

Then in the project directory run this command:

```bash
docker-compose up --build
```

It will create two containers:
All the required packages will be installed.

### Install a new package.
* Attention:
If you want to install a package for telebot project you should run this command:

```bash
docker-compose exec bot pip install <package-name>
``` 

Don't forget to add the new package to requirements.txt for further use:
```bash
docker-compose exec bot pip freeze > requirements.txt
```
"# computational_physics_telegram_bot" 
