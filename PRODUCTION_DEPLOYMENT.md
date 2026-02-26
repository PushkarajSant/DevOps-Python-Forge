# Production Deployment Guide (AWS / GCP)

Now that the application is secured and supports PostgreSQL, follow these steps to deploy DevOps Python Forge to production with a public DNS.

## Prerequisites
- A registered Domain Name (e.g., `devopsforge.com`).
- An active AWS or GCP account.
- Docker and Docker Compose (if deploying to VMs).
- `psql` client (optional) for verifying database connections.

---

## Step 1: Provision a Managed Database (PostgreSQL)

**DO NOT use SQLite in production.**
Instead of running the database locally inside a Docker container, provision a managed database. This ensures automatic backups, high availability, and scalability.

- **AWS**: Go to Amazon RDS -> Create Database -> PostgreSQL.
- **GCP**: Go to Cloud SQL -> Create Instance -> PostgreSQL.

**Action**: 
1. Create a database named `devops_forge`.
2. Secure the credentials (Username & Password).
3. Ensure the database is placed in a **Private Subnet** that is only accessible from your application servers.
4. Note down the connection string format:
   `postgresql://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/devops_forge`

---

## Step 2: Application Hosting

You can deploy the Dockerized application using a managed container service or directly on VMs.

### Option A: Fully Managed (Recommended)
This approach removes the need to manage virtual machines.

- **AWS (ECS + Fargate)**: 
  - Push your backend and frontend Docker images to Amazon ECR.
  - Create an ECS Cluster and define Task Definitions for the Backend and Frontend.
  - Expose the services via an Application Load Balancer (ALB).

- **GCP (Cloud Run)**:
  - Push Docker images to Google Artifact Registry.
  - Deploy both the frontend and backend to Cloud Run. Cloud Run automatically provides HTTPS endpoints.

### Option B: Virtual Machine (Docker Compose)
If you prefer managing the server directly:
- **AWS**: EC2 Instance (e.g., `t3.medium`).
- **GCP**: Compute Engine Instance (e.g., `e2-medium`).

Ensure the VM's security group/firewall allows inbound traffic on ports `80` (HTTP) and `443` (HTTPS).

---

## Step 3: Configuring Environment Variables

In your production environment (ECS Task Definition, Cloud Run Env Vars, or a `.env` file on a VM), you MUST set these variables:

**Backend:**
```env
DATABASE_URL=postgresql://<USERNAME>:<PASSWORD>@<HOST>:5432/devops_forge
SECRET_KEY=<generate_a_long_random_string_here>
ACCESS_TOKEN_EXPIRE_MINUTES=10080
```
> *Tip: Generate a secure SECRET_KEY using `openssl rand -hex 32`.*

**Frontend:**
```env
NEXT_PUBLIC_API_URL=https://api.yourdomain.com
```

---

## Step 4: Routing, DNS, and HTTPS (Crucial)

Never expose raw backend APIs over HTTP in production.

1. **DNS**: Go to your DNS provider (e.g., Route53, Cloudflare, GoDaddy).
   - Point `yourdomain.com` (Frontend) to your Frontend Service/VM IP.
   - Point `api.yourdomain.com` (Backend) to your Backend Service/VM IP.

2. **HTTPS / SSL**:
   - If using **AWS ALB/CloudFront** or **GCP Cloud Run**, SSL certificates are managed and provisioned automatically (e.g., via AWS Certificate Manager). Use these managed services whenever possible to automatically terminate SSL.
   - If hosting directly on a **VM**, install [Nginx](https://www.nginx.com/) as a reverse proxy on the VM, and use [Certbot (Let's Encrypt)](https://certbot.eff.org/) to generate free, automatic SSL certificates for your domain.

---

## Step 5: Security Review Checklist

Before going live, confirm the following:
- [ ] **No SQLite**: `DATABASE_URL` strictly points to PostgreSQL.
- [ ] **Strong Secret Key**: The `SECRET_KEY` in the environment differs completely from development.
- [ ] **CORS Settings**: The backend `main.py` CORS origins restrict requests to `https://yourdomain.com` (not `*`).
- [ ] **Admin Account Setup**: Log in, ensure an admin exists, and all development accounts have complex passwords. The new `is_active` model allows you to immediately neutralize malicious accounts if required.
