# TudoGostoso
Scraping with Scrapy and Mongodb.

**Vegan and vegetarian recipes**

# Before you start:
I recommend using pyenv to run the application and use Python version 3.7, but the preference is yours :D


1) Installation requirements:
  ```shell
   $ make requirements 
  ```
2) Run containers:
  ```shell
   $ make up 
  ```
3) You need to create the .env file:

    URL=**localhost**<br>
    DATABASE=**scrapy_tudo_gostoso**
# All ready?

Run the command:
  ```shell
   $ make run
  ```
The data will be stored in the mongodb container.


# How to access the container:

Now, run the command to get the docker container id:
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
