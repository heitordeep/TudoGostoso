# TudoGostoso
Developed in Scrapy with Mongodb.

**Vegan and vegetarian recipes**

# Before you start:
I recommend to use pyenv to run the application and to use version of Python 3.7 , but it's your preference :D

1) Installation requirements:
  ```shell
   $ make requirements 
  ```
2) Run containers:
  ```shell
   $ make up 
  ```
# All ready?

Run the command:
  ```shell
   $ make run
  ```
The data will be stored in mongodb container.

# How to access the container:

Now, run the command to get docker container id:
  ```shell
   $ make ps-a
  ``` 
  and 
  
  ```shell
   $ make exec id=number
  ```
  
 ## Database name:
 - DB: **scrapy_tudo_gostoso**
 - Collection name: **tudo_gostoso**
