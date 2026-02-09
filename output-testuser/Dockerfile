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
LABEL org.opencontainers.image.title="output-testuser"
LABEL naavre.source.notebook_path="test.ipynb"
LABEL naavre.source.cell_id="bb4e46cd-fd62-4d62-a0fd-57da2c898e29"
LABEL naavre.source.deep_link="/lab?notebook=test.ipynb&cellId=bb4e46cd-fd62-4d62-a0fd-57da2c898e29"
