## Configuring the App

The required data sources necessary to leverage the OT Security Solution Accelerator is defined in the section [Important Data Sources](./Data%20Management.md#important-data-sources) in the Data Management Guide.  

In addition, there are several other knowledge objects that need to be configured based on upon your environment.

### Macros

The following macros are used in the OT Solution Accelerator and need to be configured for dashboards to populate data.

**is_perimeter_device**:  This macro passes in a host and returns "true" or "false" if the host is considered a OT Perimeter Device.

**is_ot_device**:  This macro passes in a host and returns "true" or "false" if the host is considered part of the OT environment.

**is_external**:  This macro passes in a host or ip range and returns "true" or "false" on whether the host is external to an organization (e.g. a public IP for instance would be considered external in most cases)

**is_remote_access_host**:  This macro passes in a host and returns "true" or "false" depending on whether the host is considered a remote access hosts such as "jump serve".


### Lookup Files

The following lookup files should be populated with relevant data for the OT Solution Accelerator to function correctly.

**ot_protocol_definitions.csv**:  This CSV contains a mapping of application, port number, transport, description, and protocol tag.  When performing queries the port number and transport are used to identify the application.  Wildcards can also be present in the transport column to match multiple transport layer protocols (e.g. TCP, UDP, etc)