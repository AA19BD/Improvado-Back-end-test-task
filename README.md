# Improvado-Back-end-test-task

## _Improvado Back-end test task for Junior Developer: VK get friends report_

[![N|Solid](https://s.yimg.com/ny/api/res/1.2/kp0n5TiHVAQdD4Q_2Y0OBw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTQyMDtoPTEzOQ--/https://media.zenfs.com/en/globenewswire.com/b60cef7b73902c848446abd7411a270f)](https://nodesource.com/products/nsolid)
<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#bonuses">Bonuses</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#instructions">Instructions</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>

  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
* The system must be implemented as a console application
* The system should generate a report to a file, in one of several formats:
       1.  CSV
       2.  TSV 
       3.  JSON
* The system should include the following input data:
* Authorization token;
* ID of the user for whom we generate the report;
* Output file format. Default is CSV;
* Path to the output file. The default is a file named report in the current directory;
* The following fields should be present in the report (and in this order):
* Name;
* Surname;
* Country;
* City;
* Date of birth in ISO format;
* Gender;
* Report lines should be sorted by name, in alphabetical order;
* Errors should not be masked. The user should report errors as soon as possible.
   more friendly;
   Job Requirements
* Upload the finished task to Github. Send a link to the repository in a letter;
* The code must work correctly;
* The repository should have a readme file with instructions for the user. With application
   authorization instructions;
* Job code must be in accordance with PEP8

## Bonuses
* Implemented pagination. There may be many friends, they may not fit on one page, and
then the report will be incomplete;
* Accounting for a large amount of data. If there are too many friends, we may not fit in.
memory limits. We must try to spend memory wisely;
* Code extensibility. You need to think about which way the code can expand.
What if the report needs to be submitted in a YAML file? How painful will these be?
changes?
* The code is well read. When reading the code, it quickly becomes clear what is happening here;
* Code has organization. When studying the repository, it should be clear what this is about.
repository by looking at the structure of files and directories;
* In the readme file, in addition to the instructions, there is a description of how the script works, as well as
description of API endpoints that are involved in the script;
* The code is covered with tests. What happens if another person comes and changes the code so that he
stop working? How can he immediately understand that he has changed too much?
* The user should be comfortable. If you think the input data interface is bad,
you can offer your own, but you need to argue;
* There are comments in the code where they are required. For example, for narrow places, crutches and
other things;
* There are logs in the system, by which you can track the state of the system during
execution;

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started
This is an example of how you set up your project locally. To get a local copy up and running follow these simple example steps
### Prerequisites
1.Clone the repository:
```
$ git clone https://github.com/AA19BD/Improvado-Back-end-test-task.git
$ cd Improvado-Back-end-test-task
```
2. Set up the Python development environment. I recommend using a Python virtual environment
```
  $ python3 -m venv venv
  $ source venv/bin/activate
```
3. Install requirements:
```
  $ pip install -r requirements.txt
```

4. Generate Access Token
* To run most API methods you need to pass an access_token, a special access key. Token is a string of digits and latin characters and may refer to a user, community or application itself.
* There are three supported ways to receive an OAuth 2.0 token:
    * Implicit flow, Authorization code flow, Client credentials flow
* In Command Promt write 
```
  $ vkinfo token
```
* You will be redirected to blank page
<div>
  <img style="width: 100%" src="screenshots/TokenVk.png" />
</div>

* Copy the token and user-id(last part of url)
* Run the code in Command Promt
```
$ vkinfo run {access_token} {search_user_id}
```
* In case to specify path or format run:
```
Example : $ vkinfo run adk121de(token) 123456(user_id) --format json

vkinfo run [-h] [--format {csv,json,tsv}] [--path EXPORT_PATH]
                  [--log-path LOG_PATH]
                  access_token user_id

positional arguments:
  access_token          access token to use for requests
  user_id               ID of searched user

optional arguments:
  -h, --help            show this help message and exit
  --format {csv,json,tsv}
                        export forman (default: csv)
  --path EXPORT_PATH    export path (default: ./report)
  --log-path LOG_PATH   log file path (default: ./logs.log)

```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- INSTRUCTIONS -->
## Instructions
* File structure
```
 Improvado-Back-end-test-task
    assets -- > Additional configurations folder for Logging, Exceptions, DefaultConfig 
    main -- > Main Flow: fetching API, GetToken, ParsingData, Parse config/stdin arguments and set program entry point
    utils -- > Flow for save files in format [json, csv tsv] and Transforming bdate -> in ISO Format
    .gitignore -- > Specifies intentionally untracked files that Git should ignore
    requirements.txt -- > File listing all the dependencies for a specific Python project
    LICENSE -- > License, so others are free to use, change, and distribute the software
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



