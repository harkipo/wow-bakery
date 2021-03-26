# wow-bakery
Bakery management system backend

# Instructions:

1) Clone the repository
2) run 'python manage.py migrate'
3) create superuser - run 'python manage.py createsuperuser'
4) run 'python manage.py runserver'

Note: Postman collection has been added in repository for instructions on API endpoints

# functionalities:

Authentication:
  - User Registeration
  - User Login

Bakery Inventory(Admin user only):
  - Add,Update,Delete Ingredients
  - Add,Update,Delete bakery Items
  - Map and unmap ingredients to bakery items 
  - View Bakery Items( all users )
  - View Hot selling Items( all users )

Order Management(Admin Only):
  - Add , update , Delete Offer rules
  - Create order from cart items 
  - return order details for bill generation
