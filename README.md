Introduction: 
The goal of this project is to provide minimalistic django project for customers to see the catalogue and order from the catalogue.
Tech Stack used: 
django 4.1.5 ,
python 3.10.9 
and sqlite database.

Main Features

User registration and logging in 

Paginated list of products

Customer able to create orders

Number of products in stock should decrease after an order is made

Customers may see their history of orders.

Separated requirements files

SQLite by default if no env variable is set

Usage
Follow the steps below to start the project.


Getting Started
First clone the repository from Github and switch to the new directory:

$ git clone https://github.com/ssanuj/qudo_challenge.git

$ cd qudo_challenge

Activate the virtualenv for your project.
python -m venv env
source env/Scripts/activate

Install project dependencies:

$ pip install -r requirements.txt

Then make migrations:

$ python manage.py makemigrations

$ python manage.py migrate
You can now run the development server:

$ python manage.py runserver

You can create a superuser to have access to the django admin.

$ python manage.py createsuperuser

add the username and passowrd at the prompt.


Copy and paste the following url:

$  http://127.0.0.1:8000/products/

This will prompt you to sign in or signup if you don't have an account.


There are 2 models for the project 'Product' and 'Order'. Product containing the fields name, price and available_stock_quantity.
Order contains the fields: name of the user which has ordered(derived from the request.user), the price, creation date and the product foreign key.

Following views are available in the app.

product view: which list all the products in the catalogue with its price and quantity available.
orders: Which enables the user to order any product from the catalogue only if there is enough stock.
order_history: list the past orders made by the user.

views for signin, signup and logout

Todo: Deployment instructions for any majorproviders. Didn't have time to complete this. 

