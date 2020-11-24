# GraphWalker RobotFramework RESTful
Build models with GraphWalker and run the tests with RobotFramework - now in RESTful online mode!

# Table of contents
<!--ts-->
   * [Table of contents](#table-of-contents)
   * [Documentation](#documentation)
   * [Installation](#installation)
   * [Webdriver](#webdriver)
      * [Version](#version)
      * [Download](#download)
   * [Usage](#usage)
      * [Model](#model)
      * [Keywords](#keywords)
      * [GraphWalker CLI RESTful](#graphwalker-cli-restful)
<!--te-->

# Documentation
[GraphWalker](https://github.com/GraphWalker/graphwalker-project/wiki) | 
[RobotFramework](https://robotframework.org/#documentation)

# Installation
```bash
git clone https://github.com/ilarisilander/graphwalker-robotframework-online.git
cd graphwalker-robotframework-online
pip install -r requirements.txt
```

# Webdriver
There are several different webdrivers, but in this project, we use chromedriver.

* ### Version
  Before you download the chromedriver, you need to find out what version of chrome your computer is running.
  Open your chrome web browser, and type the following in the URL field:
  ```
  chrome://version
  ```
  
* ### Download
  Download chromedriver from https://chromedriver.chromium.org/ and choose the same version as your chrome web browser has.

# Usage

### Model
After creating the model in GraphWalker Studio, you download it as a **json** file and it is then ready to be loaded into graphwalker-cli.

### Keywords
* #### Naming
  The keywords in RobotFramework must have the same name as the vertices and edges in the GraphWalker model.
  Ex. if your model has a vertex (node) with the name **v_Home_Page**, then you need to have a keyword with the same name in the keyword file.
  ```robot
  *** Keywords ***
  v_Home_Page
      Log To Console  Hello World!
  ```
* ### Structure
  A good way of storing the vertices and edges is to create one keyword file for each type.
  ```
  |--robot
        |--keywords
        |         |--edge_keywords.robot
        |         |--vertex_keywords.robot
        |
        |--results
        |--scripts
        |--test_example.robot
  ```

### GraphWalker CLI RESTful
Your current directory should be where your graphwalker-cli-x.x.x.jar is located. To start the REST server locally, type the following in the terminal:
```bash
java -jar graphwalker-cli-4.3.0.jar -d all online -s RESTFUL -m <full-path-to-json-model> "random(length(10))"
```
The last part, **random(length(10))**, is the generator and stop condition. It tells the graphwalker-cli how the path is generated and for how long.

Please visit [GraphWalker - Generators & Stop Conditions](https://github.com/GraphWalker/graphwalker-project/wiki/Generators-and-stop-conditions) for more information.

### RobotFramework
When starting the RobotFramework test, your GraphWalker API should be running.
Your current directory should be where your **test_example.robot** is located, which should be in the **robot** directory.
```bash
robot -d results test_example.robot
```
