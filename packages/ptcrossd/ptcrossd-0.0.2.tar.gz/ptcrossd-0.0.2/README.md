![penterepTools](https://www.penterep.com/external/penterepToolsLogo.png)

# PTCROSSD
> Crossdomain.xml Testing Tool

## Installation
```
pip install ptcrossd
```

## Add to PATH
```bash
# If you cannot invoke the script in your terminal, its probably because its not in your PATH. Fix it by running commands below.
echo "export PATH=\"`python3 -m site --user-base`/bin:\$PATH\"" >> ~/.bashrc
source ~/.bashrc
```

## Usage examples
```
$ ptcrossd.py -u https://www.example.com/crossdomain.xml
$ ptcrossd.py -u https://www.example.com/
```

## Options
```
-u   --url         <url>           Connect to URL
-p   --proxy       <proxy>         Set proxy (e.g. http://127.0.0.1:8080)
-c   --cookie      <cookie>        Set cookie
-H   --headers     <header:value>  Set custom header(s)
-ua  --user-agent  <user-agent>    Set User-Agent header
-j   --json                        Output in JSON format
-v   --version                     Show script version and exit
-h   --help                        Show this help message and exit
```

## Dependencies
    - defusedxml
    - requests
    - ptlibs

## Version History
- 0.0.1 - 0.0.2
    - Alpha release

## Licence

Copyright (c) 2020 HACKER Consulting s.r.o.

ptcrossd is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

ptcrossd is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with ptcrossd. If not, see https://www.gnu.org/licenses/.

## Warning

You are only allowed to run the tool against the websites which
you have been given permission to pentest. We do not accept any
responsibility for any damage/harm that this application causes to your
computer, or your network. Penterep is not responsible for any illegal
or malicious use of this code. Be Ethical!