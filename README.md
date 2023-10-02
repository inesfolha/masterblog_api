# MasterBlog API
<p id="top"></p>

## Table of Contents
1. [Introduction](#introduction)
2. [Description](#description)
    - [Methods](#functionality)
3. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Installation Steps](#installation-steps)
4. [Usage](#usage)
5. [Limitations](#limitations)



## Introduction

Welcome to MasterBlog API, similarly to [MasterBlog](https://github.com/inesfolha/masterblog), this is a simple web app to create, read, update and delete blog posts (CRUD). However, despite having the same functionality, it is built differently.

Contrasting with [MasterBlog](https://github.com/inesfolha/masterblog), where the flask app was directly running and loading the HTML templates using jinja to display the information, MasterBlog API relies on a frontend application that interacts with the API

This project was developed as a training exercise after my first deep dive into API development. 

MasterBlog API uses a simple JSON file as storage for all blog posts data and allows you to add new posts, update existing ones and deleting any unwanted post via our customized user interface. 

The frontend was provided as a template, so in this case it was not built from scratch but instead was adapted to the built API.   

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

### Installation Steps

1. Clone this repository or download the script file:

```bash
git clone https://github.com/inesfolha/masterblog_api.git
```

If you downloaded a ZIP archive, extract its contents to a directory of your choice.

2. Go to the script's directory:


3. To run the script, open your terminal and execute the following command:
```bash

```

4. Open a browser tab on:

```bash

```

5. Update the backend URL accordingly to where you are running it.
Reference-style: 
![Example][image]

[image]: instructions_step5.jpg "Step 5"

[Back to the Top](#top)

### Usage
 * [Watch Demo](link to video)


### Limitations

* There is no user authentication, so you can add, delete and update any post without any restrictions as well as place an unlimited amount of likes in each post.


* Since the data is stored in a simple json file, there may be some scalability issues. since JSON files are not well-suited for handling large amounts of data. As the app's data grows, reading and writing to a single JSON file can become slow and inefficient. 


* This project was built to have the API running in the codio environment and the frontend on localhost, so there may be some CORS limitations while running both files scrips on localhost. 


[Back to the Top](#top)

