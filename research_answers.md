# Research Answers

## 1. How HTTP Applications Preserve State

HTTP is stateless, which means that each request is treated separately and the website does not automatically remember what happened before. I see this in practice when working with WordPress websites. For example, after I log in to the WordPress dashboard, I can move between pages, plugins, and settings without entering my login details every time. The website remembers that I am logged in by using an authentication cookie in the browser. This cookie contains information that helps the server identify the user during later requests.

Sessions are another way of preserving state. The server can store information linked to a unique session ID, while the browser sends that ID back with each request. A WooCommerce shopping cart is a good example. A customer can add a product to the cart, visit other pages, and return later without the cart becoming empty. The website uses session-related information to connect the new request to the same visitor.

In Django, sessions and authentication work in a similar way. Django can store session data on the server and place only the session ID in the browser cookie. This allows the application to remember a logged-in user without storing sensitive account details directly in the browser.

## 2. Performing Django Database Migrations with MariaDB

My sticky notes project currently uses SQLite, which stores the database in a file inside the project. A server-based database such as MariaDB requires a few additional setup steps. First, MariaDB must be installed, and a new database and user account must be created. The user must also be given permission to access and make changes to the database. Django uses its MySQL database backend when connecting to MariaDB, so a compatible Python database driver must also be installed.

The `DATABASES` section in `settings.py` would then be changed from SQLite to the MySQL backend. It would contain the database name, username, password, host, and port used by the MariaDB server. This is similar to the database connection details we work with in a WordPress `wp-config.php` file, although Django stores them in a different format. Once the connection details are correct, I would run `python manage.py makemigrations` to create migration files for any model changes. I would then run `python manage.py migrate` to apply those migrations to MariaDB and create or update the required tables.

Before running migrations on a live website, I would first back up the existing database and test the changes in a development or staging environment. This is an important safety step and is similar to the precautions we take at Studiobotics when working on client websites. We avoid making major changes directly on a live site without a backup because a failed migration could affect client data or cause the website to stop working correctly.
