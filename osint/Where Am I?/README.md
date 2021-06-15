# Where Am I ?
Author: [Xiaozhi](https://github.com/xiaoxiao69)

## Description

Knowledge of OSINT knowledge online.

## Requirements 
- Google Maps
- WiGLE
- Teledata


## Sources

- [location.zip](https://github.com/ChanTingHui/wssqrctf/blob/main/osint/Where%20Am%20I%3F/bin/location.zip)


```
Oh No! I'm standing in front of this Verizon central office building but I think I'm lost. I'm trying to connect to the wifi but I don't know the password to the networks. Whats the CLLI code of the building I am at ? Once you figure out the CLLI code, make sure to wrap it in wssqrCTF{}.
```


## Exploit

The jpeg files given shows a dark picture a Verizon central office and the other shows the list of wireless network in background near the office.

Using the WiGLE tool, it allows user to search a general geographical location by entering the BSSIDs or SSIDs. By entering the BSSIDs of CableWifi, it shows a town called Mount Airy in the Baltimore:
![image](https://user-images.githubusercontent.com/69874238/121999867-8143ba80-cde0-11eb-9a37-28b33e026f3c.png)

To get a more accurate position , google "DrCuppuccino and there will be 6 search results on google maps. Based on wigle, we can narrow down the results to the surgery located in Mount Airy town.
![image](https://user-images.githubusercontent.com/69874238/122000315-337b8200-cde1-11eb-8bb3-9a59a58b0404.png)

By viewing around the surrounding of the surgery, we can find locations stated in location(2).jpeg such as Carterque and katanasushi.
![image](https://user-images.githubusercontent.com/69874238/122000969-332fb680-cde2-11eb-843c-63776e7df3b7.png)

By using street view near the surgery, it will show a Verizon central office nearby.
![image](https://user-images.githubusercontent.com/69874238/122001127-6ffbad80-cde2-11eb-9164-5f7756bfb8d4.png)

 By clicking on the office, it will show that its address 1305 S Main St, Mt Airy, MD 21771, USA. Using Teledata, by filtering using the "Switch Listing by Zip Code", search up the zipcode 21771 from maps and it will show 5 results. This can be narrowed down as one of the 5 results is located in Mount Airy which is the flag for this challenge.
 
 ![image](https://user-images.githubusercontent.com/69874238/122001501-ffa15c00-cde2-11eb-88df-9a42cef959c4.png)






The flag is:

```
wssqrctf{MTARMDMARS1}
```
