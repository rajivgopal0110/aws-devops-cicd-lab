# CI/CD Demo: GitHub → CodePipeline → CodeBuild → ECR → ECS Fargate

```
git push ─► CodePipeline ─► CodeBuild (docker build + push) ─► ECR ─► ECS Fargate (rolling deploy)
```

## Setup (about 10 minutes)
1. Create a GitHub repo and push these files (`app.py`, `Dockerfile`, `requirements.txt`, `buildspec.yml`) to `main`. Keep `infra.yml` out of it or in a subfolder, it doesn't matter.
2. CloudFormation → Create stack → upload `infra.yml`. Enter your repo as `owner/repo`, pick your default VPC and 2 of its subnets. Tick "I acknowledge IAM resources".
3. When the stack completes, go to Developer Tools → Settings → Connections, open the new connection (status Pending) and click **Update pending connection** to authorize GitHub.
4. CodePipeline → open the pipeline → **Release change**.
5. ECS → Cluster → Service → Tasks → open the task → copy the **public IP** → browse to `http://<ip>`.

## Live demo
Edit `VERSION` / `COLOR` in `app.py`, `git push`, watch the three stages turn green, then refresh the browser (give it 1-2 minutes).

## Talking points
- Source, Build, Deploy are separate stages; each one passes artifacts to the next.
- `buildspec.yml` is the build recipe. Image tag = git commit SHA, so every deploy is traceable.
- `imagedefinitions.json` is the hand-off telling ECS which image to run.
- ECS does a rolling deployment: starts the new task, then stops the old one.
- Rollback = re-run an older pipeline execution or redeploy an older image tag.

## Cleanup (avoid charges)
Empty the S3 artifact bucket, then delete the CloudFormation stack (the ECR repo empties itself).

## Notes
- AWS CodeCommit is closed to new customers, so GitHub is used via a CodeConnections link.
- Fargate task has a public IP and open port 80: fine for a demo, not for production (use an ALB + private subnets).
