project    = "klayspray"
project_id = var.project_id
gcp_region = "asia-northeast3"

name           = "klayspray-yumiel-test"
ssh_client_ips = ["0.0.0.0/0"]

image_family = "centos-stream-9"  # Change to CentOS Stream 9 image family
image_project = "centos-cloud"  # Set the image project to centos-cloud

cn_options = {
  count          = 1
  machine_type   = "e2-medium"
  boot_disk_size = 30
  # compute_disk_size = 100
}

pn_options = {
  count          = 1
  machine_type   = "e2-medium"
  boot_disk_size = 30
  # compute_disk_size = 100
}

en_options = {
  count          = 1
  machine_type   = "e2-medium"
  boot_disk_size = 30
  # compute_disk_size = 100
}

monitor_options = {
  machine_type   = "e2-medium"
  boot_disk_size = 30
  # compute_disk_size = 100
}

org_id = "YOUR_ORG_ID"  # Replace with your organization ID
billing_account = "YOUR_BILLING_ACCOUNT"  # Replace with your billing account ID
