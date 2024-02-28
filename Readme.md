# Packages Required

  - pip install -r requirements.txt <b>or</b> pip install Flask pymongo dnspython python-dotenv Flask-PyMongo Flask-JWT-Extended flask_pymongo PyJWT mongoengine              
      flask_jwt_extended

# Running the app
 
  - python app.py

  - copy the local URL from the terminal (i.e http://127.0.0.1:5000)

  ![alt text](image.png)

# Replace app.config keys in app.py

  - replace the line no 6,7 with below

  - app.config['MONGO_URI'] = 'mongodb+srv://selva658:selva100_@cluster0.fowgx.mongodb.net/lybrate'

  - app.config['SECRET_KEY'] = 'EYMDyiQy4MtIQPcET-xV-yG1dNWGF1P0A9tiaYumN6EXtldIamagSfGgNQypmCq4'

# Use Postman for testing the Endpoint

  - [postman](https://web.postman.co/workspace/My-Workspace~89b7c15c-0c0b-4db3-8836-4454373cf629/request/create?requestId=7d39237e-5df3-4533-8f74-57e389f21211) 


#  Login and get the JWT Token

  - Utilize the POST method with the endpoint http://127.0.0.1:5000/login.

  - Within the <b>Body</b> section, select the <b>raw</b> format and choose <b>JSON</b>.

  - Input the username as test@123 and the password as 12345:

  - {"username":"test@123","password":"12345"}

  - Click on send,copy the response JWT Token


![alt text](image-1.png)

# GET TODO

  - Access the endpoint http://127.0.0.1:5000/todo using the GET method.

  - Within the <b>Headers</b> section, include the key as <b>Authorization</b> and the value as the <b>Copied JWT token</b>.
    - If <b>Token is invalid!</b>, please login in again with same cred.

  - Proceed by clicking on Send, which will result in a response displaying all the todos added in the database.


![alt text](image-2.png)

# GET specific item by ID

  - Access the endpoint http://127.0.0.1:5000/todo/<id> using the GET method.

  - Within the <b>Headers</b> section, include the key as <b>Authorization</b> and the value as the <b>Copied JWT token</b>.

    - If <b>Token is invalid!</b>, please login in again with same cred.

  - Proceed by clicking on Send, which will result in a response displaying specific item the todos added in the database.

![alt text](image-3.png)

# Create a new item

  - Access the endpoint http://127.0.0.1:5000/todo using the POST method.

  - Within the <b>Headers</b> section, include the key as <b>Authorization</b> and the value as the <b>Copied JWT token</b>.
    - If <b>Token is invalid!</b>, please login in again with same cred.

  - Within the <b>Body</b> section, select the <b>raw</b> format and choose <b>JSON</b>.

  - Input the name and description (id, create_at will generated by DB)


![alt text](image-4.png)

#  Update an existing item

  - Access the endpoint http://127.0.0.1:5000/todo/<id> using the PUT method.

  - Within the <b>Headers</b> section, include the key as <b>Authorization</b> and the value as the <b>Copied JWT token</b>.
    - If <b>Token is invalid!</b>, please login in again with same cred.

  - Within the <b>Body</b> section, select the <b>raw</b> format and choose <b>JSON</b>.

  - Input the name and description (id, create_at will generated by DB)

![alt text](image-5.png)


#  Delete an item

  - Access the endpoint http://127.0.0.1:5000/todo/<id> using the DELETE method.

  - Within the <b>Headers</b> section, include the key as <b>Authorization</b> and the value as the <b>Copied JWT token</b>.
    - If <b>Token is invalid!</b>, please login in again with same cred.

  ![alt text](image-6.png)




  

