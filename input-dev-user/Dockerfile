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
LABEL org.opencontainers.image.title="input-dev-user"
LABEL naavre.source.notebook_path="temp_notebook.ipynb"
LABEL naavre.source.cell_id="ba3bd72f-e4db-4987-b480-d60244b44758"
LABEL naavre.source.deep_link="/lab?notebook=temp_notebook.ipynb&cellId=ba3bd72f-e4db-4987-b480-d60244b44758"
