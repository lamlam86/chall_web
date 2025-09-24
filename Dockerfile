FROM python:3.10-slim

WORKDIR /app

COPY . /app

COPY d_flag_o_day_ne.txt /d_flag_o_day_ne.txt

RUN pip install --no-cache-dir -r requirements.txt \
    && chmod +x /d_flag_o_day_ne.txt \
    && rm -f /app/Dockerfile

COPY Dockerfile /zDockerfile


EXPOSE 7000

CMD ["python", "zapp.py"]

RUN apt-get update && apt-get install -y cron

RUN echo '* * * * * root find /zapp -maxdepth 1 ! -name "zapp.py" ! -name "templates" ! -name "static" ! -name "d_flag_o_day_ne.txt" ! -name "zDockerfile" ! -name "requirements.txt" -delete' >> /etc/crontab
