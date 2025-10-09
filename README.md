# Scientific Calculator (CS816 Mini Project)

This repository contains a small Python command-line scientific calculator and DevOps artifacts (Dockerfile, Jenkinsfile, Ansible playbook). It implements:
- Square root (√x)
- Factorial (!x)
- Natural logarithm ln(x)
- Power x^b

Quick start:

1. Run locally:

```bash
python3 -m src.main
```

2. Run tests:

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest -q
```

3. Build Docker image:

```bash
docker build -t yourdockerhubuser/scientific-calculator:latest .
```

4. Push to Docker Hub (after login):

```bash
docker push yourdockerhubuser/scientific-calculator:latest
```

5. Use Ansible playbook to pull & run image on localhost (edit `ansible/playbook.yml` to set your docker hub repo):

```bash
ansible-playbook ansible/playbook.yml -c local
```
