## Azure Function Node Type (Abstract)

Abstract node type that represents an blob storage hosted on the Azure cloud platform.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `AzureBlobStorage` | `radon.nodes.azure.AzureBlobStorage` | 1.0.0 | `radon.nodes.abstract.ObjectStorage` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `container` | `true` | `string` |   |   | Name of a blob container within the storage account |
| `source_file` | `false` | `string` |   |   | Source file name |
| `destination_file` | `false` | `string` |   |   | Destination file name |

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Container` | `radon.nodes.azure.AzurePlatform` | `tosca.relationships.HostedOn` |   |
| `invoker` | `radon.capabilities.Invocable` | `radon.nodes.azure.AzureFunction` | `radon.relationships.azure.Triggers`| [0, UNBOUNDED] |
