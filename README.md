
# Akamai ARL Hack

<small>**Update 2021-08-06** : An [Akamai notice](https://community.akamai.com/customers/s/article/WebPerformanceV1V2ARLChangeStartingFebruary282021?language=en_US) \[[backup](https://archive.is/SWQjV)\] posted some months after our publication suggests this ARL issue will stop working globally 2021-08-10. They also wrote an explicit vuln explainer. \[[gated link](https://community.akamai.com/customers/s/article/V1-ARL-vulnerability)\]</small>

Script to test open Akamai ARL vulnerability.

When successful, you can more or less load arbitrary Akamai-hosted content from the target subdomain.

## Usage

```
python arl.py <subdomain>

python arl.py list_of_subdomains.txt
```

Where the latter is a text file of line-delimited targets.

## More info on ARL attacks

*Chronological*

https://www.youtube.com/watch?v=ekUQIVUzDX4

https://www.slideshare.net/a4202655/black-hat-usa2015bypasssurgery6aug2015

http://securityhorror.blogspot.com/2019/04/hacking-temporal-locality.html

https://warandcode.com/post/akamai-arl-hack/

https://community.akamai.com/customers/s/article/WebPerformanceV1V2ARLChangeStartingFebruary282021?language=en_US

https://community.akamai.com/customers/s/article/V1-ARL-vulnerability
