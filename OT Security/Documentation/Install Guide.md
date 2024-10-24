## Installation

This app can be installed directly via the Manage Apps features within Splunk.  The user attempting to install the app must have the necessary admin features to install the app.
1.  Hover over the list of apps --> Click the *Manage* Button
<p align="center">
<img src="./Images/splunk_manage_apps.png">
</p>
2.  Click the *Install App from Files* button on the right
<p align="center">
<img src="./Images/splunk_install_app_from_file.png">
</p>
3.  To Upload the app perform the following steps

* Click on *Choose File* button and select the name of the OT Security Solution App
    
* If the app has previously been installed check the box that says *Update app.  Checking this will overwrite the app if it already exists*.

* Click the *Upload* button and wait for Splunk to acknowledge completion or the need to complete
<p align="center">
<img src="./Images/splunk_select_app.png">
</p>
4.  Once complete either restart Splunk as requested, or open the app from the listed apps


## Important Configuration

Besides the necessary data being present in the data as detailed in the [Data Management Guide](./Data%20Management.md) there are several other knowledge objects that need to be configured based on upon your environment.


### Macros

The following macros are used in the OT Solution Accelerator and need to be configured for dashboards to populate data.

### Lookup Files

The following lookup files should be populated with relevant data for the OT Solution Accelerator to function correctly.


