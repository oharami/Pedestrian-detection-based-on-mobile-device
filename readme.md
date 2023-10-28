# **Deployment Process:**

## Install Aidlux

Download AidLux from my GoogleDrive link: [Aidlux](https://drive.google.com/file/d/1IYng4KFQ5JT4cE2TD5mPKnLmN_Ld39z0/view?usp=drive_link) , and install it on Android device.

Open the mobile version of AidluxAPP, the first time you enter, the system that comes with the app will be initialised.

![1698489981089](image/readme/1698489981089.png)

After initialisation is complete enter the Aidlux interface:

![1698490256257](image/readme/1698490256257.png)

## Uploading files

Click on cloud_ip in AidLux to display the network IP address

![1698490332544](image/readme/1698490332544.png)![1698490443782](image/readme/1698490443782.png)

The mobile phone can be accessed by entering the IP address in the computer browser, the mobile phone and the computer must be in the same LAN (the initial password for login is ***aidlux***)

Click on the folder to upload the code from my github

![1698490828277](image/readme/1698490828277.png)

## PC remote debugging AidLux using vscode

Install Visual Studio Code, ref: [How to Install Visual Studio Code on Windows? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-install-visual-studio-code-on-windows/)

To install Remote SSH in vscode, click on Remote SSH on the left side of Vscode against the pop-up and click Install.

![1698491147509](image/readme/1698491147509.png)

Click on the Remote Debugging button in the lower left corner, and then click on "connect to Host".

![1698491302980](image/readme/1698491302980.png)

Then click "Configure SSH Hosts...". and select the config file in the "Users" folder.

![1698491431806](image/readme/1698491431806.png)![1698491437582](image/readme/1698491437582.png)

Edit the file according to the previous ip address, the port needs to be entered as 9022

![1698491547320](image/readme/1698491547320.png)

After saving, an SSH server will be created on the left side, click "Connect to Host in New Window".

![1698491654284](image/readme/1698491654284.png)

Click on the window, the pop-up interface select "Linux", select continue, and then enter the initial password above. When "SSH Aidlux" is displayed in the lower left corner, the connection is successful.

![1698491796360](image/readme/1698491796360.png)

Click Open Folder to locate the uploaded code folder.

![1698491939660](image/readme/1698491939660.png)

Run "pedestrian_detection.py", then the system is successfully deployed on the mobile phone.

![1698492111823](image/readme/1698492111823.png)
