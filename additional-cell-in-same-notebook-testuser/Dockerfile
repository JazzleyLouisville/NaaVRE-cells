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
LABEL org.opencontainers.image.source="https://github.com/JazzleyLouisville/NaaVRE-cells"
LABEL org.opencontainers.image.title="additional-cell-in-same-notebook-testuser"
LABEL naavre.source.notebook_path="lidar-digital-twin-experiment/02_preprocess_lidar.ipynb"
LABEL naavre.source.cell_id="5d9366db-2cf8-4b07-af00-30edd5902400"
LABEL naavre.source.deep_link="/lab?notebook=lidar-digital-twin-experiment/02_preprocess_lidar.ipynb&cellId=5d9366db-2cf8-4b07-af00-30edd5902400"
