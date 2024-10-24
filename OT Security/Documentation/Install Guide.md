## Installation 

The OT Security Solution Accelerator can be installed on a single instance or distributed Splunk environment and should be installed on a Search Head.

> [!IMPORTANT]  
> It is recommended to use Splunkbase apps that automatically provide tagging for data sources such as network traffic and authentication.

## Installation Instructions

This app can be installed directly via the Manage Apps features within the Splunk User Interface.  The user attempting to install the app must have the necessary admin capabilities to install the app.
1.  Hover over the list of apps --> Click the *Manage* Button
<p align="left">
<img src="./Images/splunk_manage_apps.png" height="150px">
</p>

2.  Click the *Install App from Files* button on the right
<p align="left">
<img src="./Images/splunk_install_app_from_file.png" width="200px">
</p>

3.  To Upload the app perform the following steps

* Click on *Choose File* button and select the name of the OT Security Solution App
    
* If the app has previously been installed check the box that says *Update app.  Checking this will overwrite the app if it already exists*.

* Click the *Upload* button and wait for Splunk to acknowledge completion or the need to complete
<p align="left" >
<img src="./Images/splunk_select_app.png" width="400px">
</p>

4.  Once complete either restart Splunk as requested, or open the app from the listed apps
