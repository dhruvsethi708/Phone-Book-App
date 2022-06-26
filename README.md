# PHONE BOOK APPLICATION

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/dhruvsethi708/Phone-Book-App.git
$ cd Phone-Book-App
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r Requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd PhoneBook
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.
<br>
<br>

## CREATE
In order to add contacts, Go to the Add Contact button and fill the contact details. 

## READ
After Creating a new contact, all contacts saved are displayed.

## UPDATE
If you want to update contact details, you can update it through a update button. 

## DELETE
If you want to delete some contact, you can delete it through a delete button.


## DEMO VIDEO

https://user-images.githubusercontent.com/74965209/175818405-fe926800-86df-44a7-a868-a3922a429802.mp4


