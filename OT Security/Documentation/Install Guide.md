## Installation

This app can be installed directly via the Manage Apps features within Splunk.  The user attempting to install the app must have the necessary admin features to install the app.
1.  Hover over the list of apps --> Scroll down to Manage Apps
2.  Click the Install Apps from Files button on the right
3.  On the next window, either select or drop the app file for uploading.  If the app has previously been installed check the box that says to overwrite the existing app.
4.  Once complete either restart Splunk as requested, or open the app from the listed apps

## Important Data Sources

The included searches and dashboards utilize data that is tagged appropriately.  This is most likely to be achieved by using apps directly from splunkbase which already provide data type tagging.  This can also be accomplished by creating eventtypes and tagging them appropriately.  Documentation for tagging eventtypes can be found [here](https://docs.splunk.com/Documentation/SplunkCloud/latest/Knowledge/Tageventtypes)

The following is a breakdown of the data sources needed:
1. Network Traffic
2. Firewall or Perimeter Device Traffic
3. Authentication events (e.g. Windows Security Logs)
4. Registry Data


