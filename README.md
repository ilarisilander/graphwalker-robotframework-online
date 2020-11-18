# GraphWalker RobotFramework RESTful
Build models with GraphWalker and run the tests with RobotFramework - now in RESTful online mode!

# Table of contents
<!--ts-->
   * [Table of contents](#table-of-contents)
   * [Documentation](#documentation)
   * [Installation](#installation)
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

# Usage

### Model
After creating the model in GraphWalker Studio, you download it as a **json** file and it is then ready to be loaded into graphwalker-cli.

### Keywords
* #### Naming
  The keywords in RobotFramework must have the same name as the vertecies and edges in the GraphWalker model.
  Ex. if your model has a vertex (node) with the name **v_Home_Page**, then you have a keyword with the name in the robot file.
  ```robot
  *** Keywords ***
  v_Home_Page
      Log To Console  Hello World!
  ```
* ### Structure
  A good way of storing the vertecies and edges is to create one keyword file for each type.
  ```
  |--robot
        |--keywords
                |--edge_keywords.robot
                |--vertex_keywords.robot
        |--results
        |--scripts
        |--test_example.robot
  ```

### GraphWalker CLI RESTful
