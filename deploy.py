import os
from prefect import flow

GITHUB_REPO = os.environ.get("GITHUB_REPO", "https://github.com/reinaldocm-prof/prefect-distribuido-github.git")

if __name__ == "__main__":
    flow.from_source(
        source=GITHUB_REPO,
        entrypoint="flows/clima.py:analise_clima_multiplas_cidades",
    ).deploy(
        name="clima-github",
        work_pool_name="lab-pool",
        cron="0 8 * * *",
        tags=["distribuido", "github"],
    )
    print(f"Deployment registrado (código vem de {GITHUB_REPO})")