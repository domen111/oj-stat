oj-stat
=================
fetch online judge statistics for various OJs

Required
-------------
python3  
module `requests` (https://github.com/kennethreitz/requests/)  
module `flask`  

Run Web Server
-------------
###On Linux (Ubuntu 14.04)
1. Install pip for python3: `sudo apt-get install python3-pip`
2. Install required modules: `sudo pip3 install flask` `sudo pip3 install requests`
3. Run `web.py`: `python3 web.py`
4. 
###On Linux (CentOS 7)
1. Install python3: `sudo yum install python3`
2. Install pip for python3: `sudo yum install python3-pip`
3. Install required modules: `sudo python3-pip install flask` `sudo python3-pip install requests`
4. Run `web.py`: `python3 web.py`

###On Windows
1. Make sure you've installed python3 and pip
2. Install required modules: `pip install requests` `pip install flask` 
3. Run `web.py`: `py web.py`

Features
-------------
###Comparer
This feature is the same as uHunt Statistics Comparer for UVa. But this supports various online judges.  
For detailed description see http://uhunt.felix-halim.net/id/303020 "Statistics Comparer" paragraph.  
  
Same as uHunt Comparer, you can use these operators: union `+`, subtraction `-`, intersection `&`, and brackets `(` `)` to force operator precedence.  
To indicate a user of a OJ, you can use `[oj id]:[user name/id]`. See [Supported OJ] for detail.  
  
For example: `tioj:domen111-tioj:visitorIKC`

Supported OJ
-------------
| OJ id | OJ full name            | Link                        | User name/id                       |
|-------|-------------------------|-----------------------------|------------------------------------|
| tioj  | TIOJ Infor Online Judge | http://tioj.ck.tp.edu.tw/   | Your login username (not nickname) |
| toj   | TNFSH Online Judge      | http://toj.tfcis.org/oj/    | User ID (a number, goto [Challenges](http://toj.tfcis.org/oj/chal/) and find "Your ID") |
| HOJ   | HSNU Online Judge       | http://hoj.twbbs.org/judge/ | User ID (a number, see the url of [your information page](http://hoj.twbbs.org/judge/user/view/146)) |
| cf    | Codeforces              | https://codeforces.com/     | Your codeforces handle (username)  |
