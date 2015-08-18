oj-stat
=================
fetch online judge statistics for various OJs

Required
-------------
python3
module `requests` (https://github.com/kennethreitz/requests/)

Features
-------------
###Comparer
This feature is the same as uHunt Statistics Comparer for UVa. But this supports various online judges.  
For detailed description see http://uhunt.felix-halim.net/id/303020 "Statistics Comparer" paragraph.  
  
Same as uHunt Comparer, you can use these operators: union `+`, subtraction `-`, intersection `&`, and brackets `(` `)` to force operator precedence.  
To indicate a user of a OJ, you can use `[oj id]:[user name/id]`. See [Supported OJ] for detail.  
  
For example: `python3 comparer.py tioj:domen111-tioj:visitorIKC`

Supported OJ
-------------
| OJ id | OJ full name            | Link                      | User name/id                       |
|-------|-------------------------|---------------------------|------------------------------------|
| tioj  | TIOJ Infor Online Judge | http://tioj.ck.tp.edu.tw/ | Your login username (not nickname) |
| toj   | TNFSH Online Judge      | http://toj.tfcis.org/oj/  | User ID (a number, goto [Challenges](http://toj.tfcis.org/oj/chal/) and find "Your ID") |