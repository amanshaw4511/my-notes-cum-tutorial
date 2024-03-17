# Virtual Private Cloud
- VPC = a Virtaul Network inside AWS
- 1 VPC is within 1 Account and 1 Region
- Private and Isolated from other VPC and Public Zone and Public Internet

## VPC Type
- Default VPC
- Custom VPC

## Default VPC
- Only one Default VPC per region
- Can be removed and recreated
- Pre-configured
- Default VPC CIDR: 172.31.0.0/16
- /20 subnet in each AZ in region
- preconfigured Internet Gateway (IGW), Security Group (SG) & Network ACL
- Subnets assing public IPv4 addresses

## Custom VPC
- Can me added as many as needed
- Custom configuration
