# Track Him Till You Find Him
Author: [Ting Hui](https://github.com/ChanTingHui)

## Description

Github and Sherlock Knowledge

## Requirements 

- Github
- Sherlock

## Sources

- [hbxxlvjqsuhxlreg](https://github.com/hbxxlvjqsuhxlreg)


```
hbxxlvjqsuhxlreg is destroying the world with a virus.
```


## Exploit

You need to search all accounts on the internet using the username `hbxxlvjqsuhxlreg` using the tool [Sherlock](https://github.com/sherlock-project/sherlock). Once you land on the github account, you see there is one repository named `-a-zA-Z0-9---.-.-a-zA-Z-2-4`. In this repository, on the branch `dev`, there are many folders made up of random codes that does not make sense. After looking through the commit history, it can be seen that  `.gitignore` file has been modified and updated twice. 
<br />

When you open this commit, you find out that the user had mistakenly pushed his `.env` file with the flag and had forgotten to add `.env` to the `.gitignore` file. 
<br />


The flag is:

```
wssqrctf{@n@ccid3nt+m!sT@k3}
```
