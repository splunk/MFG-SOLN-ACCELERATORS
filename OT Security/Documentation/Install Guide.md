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

Besides the necessary data being present in the data as detailed in the [Important Data Sources](./Data%20Management.md#important-data-sources) there are several other knowledge objects that need to be configured based on upon your environment.


### Macros

The following macros are used in the OT Solution Accelerator and need to be configured for dashboards to populate data.

**is_perimeter_device**:  This macro passes in a host and returns "true" or "false" if the host is considered a OT Perimeter Device.

**is_ot_device**:  This macro passes in a host and returns "true" or "false" if the host is considered part of the OT environment.

**is_external**:  This macro passes in a host or ip range and returns "true" or "false" on whether the host is external to an organization (e.g. a public IP for instance would be considered external in most cases)

**is_remote_access_host**:  This macro passes in a host and returns "true" or "false" depending on whether the host is considered a remote access hosts such as "jump serve".

### Lookup Files

The following lookup files should be populated with relevant data for the OT Solution Accelerator to function correctly.

**ot_protocol_definitions.csv**:  This CSV contains a mapping of application, port number, transport, description, and protocol tag.  When performing queries the port number and transport are used to identify the application.  Wildcards can also be present in the transport column to match multiple transport layer protocols (e.g. TCP, UDP, etc)
