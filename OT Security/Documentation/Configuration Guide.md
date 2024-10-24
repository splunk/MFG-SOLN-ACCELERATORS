## Configuring the App

The required data sources necessary to leverage the OT Security Solution Accelerator is defined in the section [important Data Sources](./Data%20Management.md#important-data-sources) in the Data Management Guide.  

In addition, there are several other knowledge objects that need to be configured based on upon your environment which are outlined below.

### Macros

The following macros are used in the OT Solution Accelerator and need to be configured for dashboards to populate data.

<u>is_perimeter_device</u>:

This macro passes in a host and returns "true" or "false" if the host is considered an OT Perimeter Device.

<u>is_ot_device</u>:  

This macro passes in a host and returns "true" or "false" if the host is considered part of the OT environment.

<u>is_external</u>:  

This macro passes in a host and returns "true" or "false" on whether the host is external to an organization (e.g. a public IP for instance would be considered external in most cases)

<u>is_remote_access_host</u>:  

This macro passes in a host and returns "true" or "false" depending on whether the host is considered a remote access hosts such as "jump servers".


### Lookup Files

The following lookup files should be populated with relevant data for the OT Solution Accelerator to function correctly.

<u>ot_protocol_definitions.csv</u>:  

This lookup contains a mapping of application, port number, transport, description, and protocol tag.  When performing queries the port number and transport are used to identify the application.  Wildcards can also be present in the transport column to match multiple transport layer protocols (e.g. TCP, UDP, etc) and entries are not case sensative.  By default it contains a small list of industrial protocols which can be updated or augmented based on your environment.