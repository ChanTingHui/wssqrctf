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
