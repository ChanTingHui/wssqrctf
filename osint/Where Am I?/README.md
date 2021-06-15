# Where Am I ?
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description

Knowledge of basic OSINT online tools

## Requirements 

- Web Archive
- Yandex
- JWT
- Flight Stats


## Sources

- https://twitter.com/ImElonMask1


```
Lieutenant John, Mr Elon is wanted for drug traffic. We were told by an informant that he is hiding drugs on a particular plane.
Please get back to me with the flight number. His twitter account is the only information we have.
```


## Exploit
After knowing his twitter account , go to [Web Archieve](https://web.archive.org/) and there is a snapshot of the website on a particular day. The snapshot shows some deleted tweets done by Mr Mask. An important deleted tweet is a `JWT` encoded token whch can be decoded on [JWT.io](https://jwt.io/). After decoding it, the decoded text provided a departure time and departure location. The departure location will be `SEA` which is the acronyms for `Seattle-Tacoma International.Airport`. 
<br />
<br />
Next, the image on the twitter account can be put into yandex and figure out that the location is `Georgia Aquarium` which is the arrival location. In addition, a tweet states that the plane was departed on Elon's birthday and the birthdate can be found on his twitter account.
<br />
<br />
After getting the information of departure time, departure date, departure location and arrival location, go to [FlightStats](https://www.flightstats.com/) and input the information and look for the flight number.
<br />


The flag is:

```
wssqrctf{WS-7182}
```
