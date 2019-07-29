
  

  

  

# CPL Object Tree Parser

  



Symantec/Bluecoat's Content-Policy-Language (CPL) parser to return trees paths given a node.

Used to track objects and their sub/super objects throughout a CPL File

  
#### Dependencies
* [Python 3+] - Install Python on your machine

* [PiP] - package installer for python (needed for any dependencies)
  
### Usage:
 `cpl_parse.py [OPTIONS] DOMAIN_FILE CPL_FILE`
  

  

  

### Domain File
comma separated file (no spaces) with any number of domains or initial "node" objects to track:


ex.

`github.io,github.com,bitbucket.org,sliderocket.com,mirror.math.princeton.edu`


### CPL File

content policy language file to parse and track object trees in



  ### Output

`cpl_parse.py` will create a file called `cpl_domain_trees.txt` in its same directory with trees for every "node" passed in to the domain input file


 
