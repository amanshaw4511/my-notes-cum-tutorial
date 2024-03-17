# Cloud Formation (CFN)
- IAAC
- Tool to create, update and delete infra in AWS 
in consistent and repetatable way using template.
- It can be written in YAML or JSON



## Template
```yaml
AWSTemplateFormatVersion: ""

Description:
  String

Metadata:
  template metadata

Parameters:
  set of parameters

Mappings:
  set of mappings

Condition:
  set of conditions

Transform:
  set of transform

Resource:
  set of resources

Output:
  set of outputs
```

- Yaml Template => Stack (contains Logical resources) => Physical Resource (instance)
