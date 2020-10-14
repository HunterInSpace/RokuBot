# RokuBot
RokuBot is a open source discord bot which can control a RokuTV!

## Installation

Just clone this repo using:

```bash
git clone https://github.com/TurtDev/RokuBot
```
and then you will need a few python modules, to install these you can use

 ```bash
pip install roku
```
and
```bash 
pip install discord.py
```
These are the only two dependencies that RokuBot currently uses

# Setup
To setup RokuBot you will need to edit a few things in the [bot.py](https://github.com/TurtDev/RokuBot/blob/master/bot.py) file

You will need to edit the Roku_IP in 

```python
roku = Roku("Roku_IP")
```

To get the IP of your roku you will need to go to your roku, so you should start here

![](https://bit.ly/2H2akXE)

Go left until you make it here
![](https://bit.ly/3786ffA)

And then scroll down until you reach ***Settings***
![](https://bit.ly/34VAyDi)

And then go right onto ***Network***
![](https://bit.ly/34VAPGk)

And then right one more time onto ***About***
![](https://bit.ly/34WkoJX)

And then take note of the ***IP address*** which in my case in 192.168.1.56
this will now replace the Roku_IP which I showed earlier, so lets say your Roku's IP address is the same as mine 

```python
roku = Roku("Roku_IP")
```
will now become
```python
roku = Roku("192.168.1.56")
``` 
And now you will need to replace the ***Bot_Token*** in 
```python
bot.run("Bot_Token")
```

To do this you will need to 
A. Have a Discord account which I'm guessing you already have
And B. Be on the [Discord Developer Portal](https://discord.com/developers/applications)
To get a Bot Token you will need a Discord application which can be made by simply by clicking ***New Application*** 
![](https://bit.ly/375rm1P)
Giving your application a name (can be anything I just named it Roku Bot in this example)
![](https://bit.ly/2GYlXPz)
After clicking create you will be sent to this screen where you will click ***Bot***
![](https://bit.ly/34YHMGD)
Click ***Add Bot***
![](https://bit.ly/372BIzD)
And then click ***Yes, do it!***
![](https://bit.ly/34Wn0rf)
You will then be sent to this page and you will click ***Copy*** and never ***EVER*** share this token with anyone with this token anybody can control your bot 
![](https://bit.ly/352dwuJ)
After clicking ***Copy*** just replace the Bot_Token in 
```python
bot.run("Bot_Token")
```
with your new token and you are done!

Now just run the python file using 
```bash
python bot.py
```
And if everything worked you should see ***Bot is online!*** be printed in the console

![](https://bit.ly/3iUMNF3)

And now you need to invite the bot to a server, to do this head over to ***OAuth2***
![](https://bit.ly/33WffCc)

Click ***bot*** and then copy the link
![](https://bit.ly/2SVIvTu)

After going to the link you copied you will be sent here where you will pick a server for your bot to join
![](https://bit.ly/2Fy4qx0)

And you should now see that your bot joined the server you told it to join!
![](https://bit.ly/3nNLyv8)

## Usage 

Now that your bot has joined your server and you have it running You can run 

Command | Usage / Example
------------ | -------------
$home | Imitates pressing the home button on a Roku remote
$up | Imitates pressing the up control button on a Roku remote
$down | Imitates pressing the  down control button on a Roku remote
$left | Imitates pressing the left control button on a Roku remote
$right | Imitates pressing the right control button on a Roku remote
$select | Imitates pressing the center select button on a Roku remote
$back | Imitates pressing the back button on a Roku remote
$type "What you want to type" | Imitates typing on a Roku TV can be used for typing in a video name on the Youtube app for example
$backspace | Imitates pressing backspace on a Roku TV which can be used in a app such as youtube


## Do you accept Pull requests?
Heck yes! If you have any ideas at for what I should add to RokuBot please add it in a pull request.

## License
[MIT](https://choosealicense.com/licenses/mit/)