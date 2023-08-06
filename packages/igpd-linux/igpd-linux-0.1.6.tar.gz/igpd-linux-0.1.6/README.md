# igpd-linux

**Note**: This package works only on linux operating system

This  package  helps you to download the following from instagram

1. Posts (Reels,IGTV)

2. Story

3. Highlights

4. Entire profile

<hr />

## Installation

Run the following to install:

```python
pip install igpd-linux
```
<hr />

## Usage

Open in terminal and type the following command

```python
python3 -m igpd_l
```

## Things to Remember 

* **Please enter the url in with a forward slash at the end** **when you wanna download a post** 
  **Example**: https://www.instagram.com/reel/CbfbXuCg5lf/" 

* **If you want to download a private user's post story and etc choose option 1**
* **If you want to download a public user's post/Igtv/EntireProfile choose option 2** 
*  **If you want to download a public user's story/reels/hightlights choose option 1, because these can't be downloaded without login** 

## **Most important thing**: 

When you enter your **username and password**  for the first time, the data is stored in a folder in home called **.igpd/user_data/**. The data is  stored  in order to prevent you from tying the data again and agin. 

## **The problem**

 Even if you have entered a wrong username or password the data gets stored since the bad credentials **exception handling feature is not available yet**.  Since the data gets stored, when you run the tool for the next time it asks to validate your login by typing **yes**, but you won't be able to login since wrong data is stored.

## **How to fix it** 

Run the program, type in username and the following prompt will be shown and type in **no** when it appers to reset your username and password.

<img src = "https://i.imgur.com/Cq8JzPg.png" height="200" width="600">  

