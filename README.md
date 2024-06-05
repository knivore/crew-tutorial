<div align="center">
<h1> CrewAI Tutorial</h1>
<h3>A quick guide to get started with CrewAI</h3>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#starting">Starting</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

This repository is a tutorial on how to get started with CrewAI. CrewAI is a framework built for orchestrating role-playing, autonomous AI Agents.
CrewAI focuses on empowering agents to work together seamlessly, tackling complex tasks with capabilities ranging from web search, data analysis to collaboration & delegating tasks among coworkers.

### Built With
[![CrewAI][CrewAI]][CrewAI-url] [![Python][Python.org]][Python-url] [![OpenAI][OpenAI]][OpenAI-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get started, follow these simple steps:

### Prerequisites

- Python 3.8 or higher
- Basic understanding of Python
- OpenAI API Key (Sign up & obtain [here](https://platform.openai.com/api-keys))

Setting up OpenAI's API Key.

- Create a .env file and populate:

``` 
OPENAI_API_KEY="sk-xxx"
```

OR you can also export the API key in your terminal:

``` bash
export OPENAI_API_Key = "sk-xxx"
```

### Installation

- To run the application, you will need to first create a virtual environment and install the dependencies and all
  required libraries.

MacOS:
``` bash
pip install virtualenv
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows:
``` bash
pip install virtualenv
python3.11 -m venv venv
venv/Scripts/activate.bat
pip install -r requirements.txt
```

### Starting

- To start each tutorial application, you can run the following command:

``` bash

```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contact

For any enquiry or support, you may drop an email to [Keh](mailto:chinkeh@hotmail.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Acknowledgments

Developed using [CrewAI](https://docs.crewai.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[CrewAI]: https://img.shields.io/badge/CrewAI-%23f1413d.svg?style=for-the-badge&logo=crewai&logoColor=white
[CrewAI-url]: https://www.crewai.com/
[Python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org/
[OpenAI]: https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=fff
[OpenAI-url]: https://openai.com/api/
