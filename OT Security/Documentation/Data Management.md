## Data Management in OT

Within OT environments there are often restrictions in gathering data due to vendor restrictions and concerns around safety and reliablity.   This section covers broadly the important data sources for the OT Security Solutions Accelerator and Methods to collect this data.  All examples given are based on actual customer implementations.

## Important Data Sources

The included searches and dashboards utilize data that is tagged appropriately.  This is most likely to be achieved by using apps directly from splunkbase which already provide data type tagging.  This can also be accomplished by creating eventtypes and tagging them appropriately.  Documentation for tagging eventtypes can be found [here](https://docs.splunk.com/Documentation/SplunkCloud/latest/Knowledge/Tageventtypes)

The following is a breakdown of the data sources needed in the OT Security Solutions Accelerator:
1. Network Traffic
2. Firewall or Perimeter Device Traffic
3. Authentication events (e.g. Windows Security Logs)
4. Registry Data

## Methods to Collect Data from OT Environments

This section includes informations of how data can be collected in the OT environment based on real world use cases.  While not exhaustive, it can help identity passive and active methods of collecting this data.  Data sources mentioned as part of the OT Security Solution Accelerator are in ***bold italics.***

| Method        | Data Source       | Notes       | Access Type       |
|:--------------|:------------------|:------------------|:----------------- |
| Universal Forwarder | Host bases logs including ***Windows authentication events***, ***registry data,*** applications installed, service configuration, ICS logs, performance monitoring | More versatility and control is data types collected from hosts | Agent based |
| Existing agents | Depending on agent but could include malware, security events, and asset information | Examples include (but not limited to) Snare, Endpoint Protection, WhatsUp Gold, SCCM, and SCOM | Agent based |
| SFTP/FTP | Typically text based logs | SFTP (preferred) and FTP can be used to export logs periodically to systems using a Universal Forwarder to forward the logs | Agent based |
| Windows Event Forwarding | Windows Events including ***Authentication events*** | Can be used to collect Security, System, Application, or other specific windows events | Configuration |
| Syslog | ***Network and firewall logs***, netflow, security alerts from other products | Best practice to leverage a syslog server rather than sending directly to Splunk | Configuration |
| Zeek | ***Network traffic*** | Zeek can collect information on network activity such as network traffic and in some cases may support industrial protocols | Configuration|
| OT Security Solutions | asset information, alerts, vulnerabilities | Most OT Security Solutions have the ability to send asset, alerts, and vulnerability information to Splunk but may change as capabilities mature.  In most cases they provide this information via syslog and REST API's | Remote |
| REST API's | Depending on application but could include malware, security events, vulnerability information, and asset information | Common mechanism leveraged by OT Security Products to collect alerts, asset info, and vulnerabilities | Remote |
| DBConnect | ICS Logs, Alarm Information, Configuration, Patching Info, Host Based Information | Leveraged by data historians, patching solutions, ICS systems, and other systems | Remote |
| WMI Collector | OS components, process & service information, applications, user accounts, security settings | Consideration should be given to scaling of WMI for large environments| Remote |
| HTTP Event Collector (HEC) | System health and state information | Newer products are providing methods to collect via HEC but depends on the application | Remote |

For more general information about indexing data in Splunk Enterprise and Splunk Cloud, please refer to the following documentation: [Getting Data In](https://docs.splunk.com/Documentation/Splunk/latest/Data/WhatSplunkcanmonitor).​
