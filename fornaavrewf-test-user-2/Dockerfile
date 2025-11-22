FROM ghcr.io/qcdis/naavre/naavre-cell-build-python:v0.22.18 AS build
COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yaml .
RUN micromamba install -y -n venv -f environment.yaml
ARG MAMBA_DOCKERFILE_ACTIVATE=1
USER root
RUN conda-pack -p /opt/conda/envs/venv -o /tmp/env.tar && \
    mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
    rm /tmp/env.tar
RUN /venv/bin/conda-unpack

FROM ghcr.io/qcdis/naavre/naavre-cell-runtime-python:v0.22.18 AS runtime
COPY --from=build /venv /venv
WORKDIR /app
COPY . .
LABEL org.opencontainers.image.source="https://github.com/JazzleyLouisville/NaaVRE-cells.git"
LABEL org.opencontainers.image.title="fornaavrewf-test-user-2"
LABEL naavre.source.notebook_path="fornaavrewf.ipynb"
LABEL naavre.source.cell_id="8fb67f07-060b-4fbe-88e2-319a35eb45bf"
LABEL naavre.source.deep_link="/lab?notebook=fornaavrewf.ipynb&cellId=8fb67f07-060b-4fbe-88e2-319a35eb45bf"
