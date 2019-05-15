FROM python:3.7-alpine3.9

# WORKDIR /usr/src/app
ARG USER_ID=1000
ARG USER_NAME=gitlab-runner
ARG GROUP=savemyprint
ARG GROUP_ID=1000

ENV USER_ID=1000
ENV USER_NAME=gitlab-runner
ENV GROUP=savemyprint
ENV GROUP_ID=1000

# RUN groupadd -r ${GROUP} && useradd -r -g ${GROUP} ${GROUP_ID}
# RUN addgroup --gid ${GROUP_ID} ${GROUP} && \
    # adduser --disabled-password --uid ${USER_ID} ${USER_NAME}
RUN addgroup -S ${GROUP} -g ${GROUP_ID} \
  && adduser -S -g ${GROUP} -u ${GROUP_ID} ${USER_NAME}

COPY requirements.txt /
RUN mkdir /app
WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]