got to the page
https://puzzled.challs.cybersecuritychallenge.ro/

saw that error. imagined something like `$_GET['show%00code#<script>$x="%00";</script>aaa=']`

got to

https://puzzled.challs.cybersecuritychallenge.ro/?show%2500code%23%3Cscript%3E$x%3d%22%2500%22%3b%3C/script%3Eaaa=1234&stop=

then

https://puzzled.challs.cybersecuritychallenge.ro/?show%2500code%23%3Cscript%3E$x%3d%22%2500%22%3b%3C/script%3Eaaa=1234&stop=&flag_token_sada3edewdc32dwq=123

no luck. tried the file. got redirect.

https://puzzled.challs.cybersecuritychallenge.ro/flag_token_sad123a3edewdc32dwasd22343qds.php/

flag is in js
```
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL /resize/flag_token_sad123a3edewdc32dwasd22343qds.php/ was not found on this server.</p>
<hr>
<address>Apache/2.4.29 (Ubuntu) Server at localhost Port 443</address>
</body></html>
<script type="text/javascript">ECSC{3400e9d1deef6a35d288c2ec8b8ddc03b4830eaba12c26b6f8bca9adcd83b9ef}</script>
```
