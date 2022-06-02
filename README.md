# Apache Log Parser
This is a very simple commond line python script which allows you to parse data from Apache Log files.

# Usage
<pre></code>
usage: apacheLogParser.py [-h] -l  [-i] [-u] [-p] [-m] [-s]

Apache Log parser Tool

options:
  -h, --help      show this help message and exit
  -l , --log      Apache Log Parser
  -i , --ip       enter IP address
  -u , --url      enter the URL
  -p , --path     enter the path or endpoint of the URL
  -m , --method   enter HTTP request method
  -s , --status   enter the resposne status code
</code></pre>

# Examples
<pre><code>
./apacheLogParser.py -l apache_logs.txt -i 93.114.45.13
./apacheLogParser.py -l apache_logs.txt -m GET
./apacheLogParser.py -l apache_logs.txt -s 200 - 93.114.45.13
</code></pre>
