# Grability ShoppingCart

This is a Django/Andgular Project that implements an shoppingcart

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django and their dependencies.



```bash
pip install -r requirements.txt

```

Use npm for install Angular and their dependecies, you must execute it in angualr path: 

```bash
cd sources/angular/
npm install

```

## Build Frontend

You have to compile the angular  project to prove to Django the static files:

```
cd sources/angular
ng build --prod
cd ../../
python manage.py collectstatic
```
## Usage

In order to execute the proyect you have to execute the Django server from base path

```
python manage.py runserver

```
###  NOTE

If everything goes well the following are the urls:

**API**: http://localhost:8000/api/

**DJANGO ADMIN**: http://localhost:8000/admin

**HOMEPAGE**: http://localhost:8000/


## Testing user

**superuser:** superuser  
**password:** Zaq12wsx#

## Database Description

### The Database has four entities: 

**User**: Describe a User that is going to have a ShoppingCart

**Product**: Describe the stock of products and its cost and taxes

**ShoopingCart**: Describe the entity that is going to store the product that the user is adding, to buy, has the following states:

```
DRAFT = An order that still is pending for checkout
PENDING = An order that already has checkout, but it's pending for payment
PAID =  An order already paid, but is pending to start 
IN_PROGRESS = The Order is being prepared, to be send to the client
COMPLETED = The client is prepared and the client has recieved the products
CANCELED = The order has been canceld by the client

```

**ProductShoppingCart**: Describes the cuantity of every product that the client has added to their current shopping cart


![Entity Relation Database](./Model_ER.png?raw=true)