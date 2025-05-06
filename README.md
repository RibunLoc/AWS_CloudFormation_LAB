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

Một S3 bucket để chứa các file .yaml:
```bash
aws s3api create-bucket \
  --bucket my-cloudformation-bucket-111 \
  --region us-west-1
```
🛠️ Bước 1: Upload các template lên S3
- Upload thư mục module
```bash
aws s3 cp path/to/modules s3://my-cloudformation-bucket-111/modules --region us-west-1 --recursive
```
- Upload file main.yaml
```bash
aws s3 cp path/to/main.yaml s3://my-cloudformation-bucket-111/main.yaml --region us-west-1
```

🚀 Bước 2: Deploy stack từ file main.yaml
```bash
aws cloudformation create-stack \
  --stack-name my-cloudformation-template-bucket-111 \
  --template-url https://s3.amazonaws.com/my-cloudformation-bucket-111 \
  --capabilities CAPABILITY_NAMED_IAM
```

🧹Bước 3: Xóa toàn bộ hạ tầng
```bash
aws cloudformation delete-stack --stack-name my-infra
```

###
### Cách 2: CHẠY FILE deploy.sh và clean.sh

✅ Bước 1: Tạo biến môi trường .env trong thư mục scripts
```bash
BUCKET_NAME="Tên Bucket của bạn"
REGION="Region mà bạn muốn triển khai"
MODULES_DIR="./modules"
MAIN_TEMPLATE="main.yaml"
MAIN_STACK_NAME="tên stack bạn muốn đặt trên cloudformation"
```
=> Sửa lại các giá trị cho phù hợp.

✅ Bước 2: Cấp quyền thực thi cho script
```bash
chmod +x deploy.sh
chmod +x clean.sh
```
Bước 3: Tạo key-pair 📌

👉 Thực hiện tạo keypair trên AWS Console có tên là `my-keypair`

🚀Bước 4: Chạy script 
```bash
./deploy.sh
```
🧹Bước 5: Xóa toàn bộ hạ tầng
```bash
./clean.sh
```