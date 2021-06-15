# WSSQRCTF

<!-- TABLE OF CONTENTS -->
## Table of Contents
* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
* [Template](#Template)

<!-- ABOUT THE PROJECT -->
## About The Project

This is a repository to store CTF challenges to be deployed for `wssqrctf`.

## Getting Started
The following are the categories of challenges that are to be made:

- Web
- OSINT
- Crypto
- Forensics
- Reversing
- Miscellaneous

## Template

### Flag Format

- The flags must be enclosed in `wssqrctf{}`.
- They can have numbers, alphabets, `_`s, `'`s, `!`s, `.`s, `+`s, `-`s, `@`s, `#`s, `$`s, `%`s, `:`s, `>`s.
- They must be related to the challenge.
- They must not be so simple that you can guess them.

Here's a regex for the flag format.

```
/^wssqrctf{[\w_!@#?$%\.'"+:->]{5,50}}$/
```

Here's a sample flag.

```
wssqrctf{s4mpl3_fl4g'+!-.@#$%?}
```

### Directory Structure

The following are guidelines for creating challenge folders.

- Each challenge has it's own folder, which is placed in the relevant directory amongst the ones enlisted above.
- Each challenge **must** have a `README.md` file describing how to solve the challenge, along with the relevant code / files that needs to be run / deployed on the server.
- The flag must be present in the `README.md` for the challenge.
- We prefer having each challenge in it's own docker container, so that it's simple to deploy.

### Template for Challenge README

As mentioned earlier, each challenge requires a `README`. The README must be written in such a way that this can serve as an **official write-up** later. This should have the following format.

```
# Challenge Name

Author: [author](https://github.com/author)

## Description

Brief Description about challenge

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [sample.py](./sample.py)
- [sample.txt](./sample.txt)

<!-- Remove this comment, and the '\' before '```' -->
\```
Challenge description to go up on the website.

Hint 1: If any - Points 100
Hint 2: If any - Points 200
\```

## Exploit

<!-- Much more detailed description than the following. -->
Reverse `sample.py` to decrypt the flag in `sample.txt.`
<br />

The last line should be the flag.
<br />

The flag is:

\```
wssqrctf{flag}
\```
```

### challenge.yml

Every challenge must have a `challenge.yml`, in the format specified in [challenge-example.yml](./challenge-example.yml). This is **MANDATORY**, without this the challenge will not be able to deploy.
