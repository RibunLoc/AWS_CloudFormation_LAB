# AWS_CloudFormation_LAB
✅ README.md – Hướng dẫn triển khai hạ tầng với AWS CloudFormation
# AWS CloudFormation Infrastructure Deployment

Đây là hướng dẫn triển khai hạ tầng AWS bao gồm VPC, Subnets, NAT Gateway, Route Tables và Security Groups bằng CloudFormation theo mô hình module hóa.

---

## 📁 Cấu trúc thư mục

```bash
.
project/
├── modules/
│   ├── vpc.yaml                # Module VPC và subnet
│   ├── route-table.yaml        # Module Route Tables
│   ├── nat.yaml                # Module NAT Gateway
│   ├── security_groups.yaml    # Module Security Groups
│   ├── ec2.yaml                # Module EC2 Instances
├── tests/
│   └── test_templates.py       # Script kiểm tra template
├── scripts/
│   ├── deploy.sh               # Script triển khai
│   └── cleanup.sh              # Script dọn dẹp tài nguyên
├── main.yaml                   # Template chính để nối các module
└── README.md                   # Hướng dẫn sử dụng
```
🧰 Yêu cầu
Tài khoản AWS đang hoạt động

Đã cài đặt AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html

Đã cấu hình aws configure với Access Key/Secret Key hợp lệ

Một S3 bucket để chứa các file .yaml: infra-cloudformation-bucket-101

🛠️ Bước 1: Upload các template lên S3
```bash
aws s3 cp main.yaml s3://infra-cloudformation-bucket-101/
aws s3 cp modules/vpc.yaml s3://infra-cloudformation-bucket-101/
aws s3 cp modules/route-table.yaml s3://infra-cloudformation-bucket-101/
```

🚀 Bước 2: Deploy stack từ file main.yaml
```bash
aws cloudformation create-stack \
  --stack-name my-infra \
  --template-url https://s3.amazonaws.com/infra-cloudformation-bucket-101/main.yaml \
  --capabilities CAPABILITY_NAMED_IAM
```

🧹Bước 3: Xóa toàn bộ hạ tầng
```bash
aws cloudformation delete-stack --stack-name my-infra
