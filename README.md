# AWS_CloudFormation_LAB
✅ README.md – Hướng dẫn triển khai hạ tầng với AWS CloudFormation
# AWS CloudFormation Infrastructure Deployment

Đây là hướng dẫn triển khai hạ tầng AWS bao gồm VPC, Subnets, NAT Gateway, Route Tables và Security Groups bằng CloudFormation theo mô hình module hóa.

---

## 📁 Cấu trúc thư mục

```bash
.
├── main.yaml                # Root stack gọi các stack con
├── modules/
│   ├── vpc.yaml            # Tạo VPC, Subnet, IGW, NAT Gateway, SG
│   └── route-table.yaml    # Tạo Route Tables và gán với Subnet
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
