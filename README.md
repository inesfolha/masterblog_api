# MasterBlog API
<p id="top"></p>

## Table of Contents
1. [Introduction](#introduction)
2. [Description](#description)
    - [Methods](#functionality)
3. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Installation Steps](#installation-steps)
4. [How does it work?](#how-does-it-work)
5. [Limitations](#limitations)
6. [Contributions](#contributions)



## Introduction

Welcome to MasterBlog API, similarly to [MasterBlog](https://github.com/inesfolha/masterblog), this is a simple web app to create, read, update and delete blog posts (CRUD). However, despite having the same functionality, it is built differently.

Contrasting with [MasterBlog](https://github.com/inesfolha/masterblog), where the flask app was directly running and loading the HTML templates using jinja to display the information, MasterBlog API relies on a frontend application that interacts with the API

Since the frontend is not fully developed to yet support all the API functionalities, you can also use the full API with Postman or a similar software. 

MasterBlog API uses a simple JSON file as storage for all blog posts data and allows you to add new posts, update existing ones and deleting any unwanted post via our customized user interface.

The API was built using the Flask framework. 

[Back to the Top](#top)

## Description


#### Functionality

| route                    | method |                                          use                                          |
|--------------------------|:------:|:-------------------------------------------------------------------------------------:|
| /api/posts               |  GET   | Loads the posts and sorts them based on a specified field and direction(if specified) |
| /api/posts               |  POST  |                        Handles the addition of a new blog post                        |
| /api/posts/<int:post_id> | DELETE |                      Deletes a post with the specified post ID.                       |
| /api/posts/<int:post_id> |  PUT   |                      Updates a post with the specified post ID.                       |
| /api/posts/search        |  GET   |                   Searches for posts based on title and/or content.                   |

[Back to the Top](#top)
## Installation

### Prerequisites

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
- Flask installed.
- To make the backend work, you may need to install a package called flask-cors.

- If you want to use the all the API functions, you can use [Postman](https://www.postman.com/)

### Installation Steps

1. Clone this repository or download the script file:

```bash
git clone https://github.com/inesfolha/masterblog_api.git
```

If you downloaded a ZIP archive, extract its contents to a directory of your choice.

2. Go to the script's directory.

3. Run the backend and the frontend scripts. 

4. Open the frontend URL on a browser.

5. Update the backend URL in the frontend page accordingly to where you are running the backend.
 
![Example][image]

[image]: https://github.com/inesfolha/masterblog_api/blob/main/frontend/static/instructions_step5.jpg?raw=true "Step 5"

[Back to the Top](#top)

### How does it work?
 * [Watch Demo](https://www.youtube.com/watch?v=mOzXPNffNbs)


### Limitations

* There is no user authentication, so you can add, delete and update any post without any restrictions as well as place an unlimited amount of likes in each post.


* Since the data is stored in a simple json file, there may be some scalability issues. since JSON files are not well-suited for handling large amounts of data. As the app's data grows, reading and writing to a single JSON file can become slow and inefficient. 


* This project was built to have the API running in the codio environment and the frontend on localhost, so there may be some CORS limitations while running both files scrips on localhost. 


* Despite the API having working functions such us search, sort and update, the user interface currently still does not support it, I am looking for updating the user interface in the future, or if you would like to develop it yourself, you are welcome to do so.   


[Back to the Top](#top)

## Contributions

Contributions to this project are welcome. If you'd like to contribute, please fork the repository, make your changes, and create a pull request.

[Back to the Top](#top)

