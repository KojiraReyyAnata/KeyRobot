FROM python:3.10

ENV API_ID=17250424 
ENV API_HASH=753bc98074d420ef57ddf7eb1513162b
ENV EVENT_LOGS=-1001961499248
ENV ERROR_LOGS=-1001961499248
ENV BOT_ID=6829313514
ENV BOT_USERNAME=keyxrobot
ENV BOT_NAME=Key X Robot
ENV JOIN_LOGGER=-1001961499248
ENV ARQ_API_KEY=PPJZAN-CVFHRQ-QFVBOU-CNESNO-ARQ
ENV MONGO_DB_URI=mongodb+srv://keyxrobot:gualupabanget@keyxrobot.tzyl5qp.mongodb.net/?retryWrites=true&w=majority
ENV STRING_SESSION=BQC_AFHdtxAUk-eqpQDVUHbSuTv35ijELZ1SCMvKJGUj2Uiye8vcwhKrbl4-g6mzNsY9bX6PKg7SQXUs-o7SEt9oasiYNOqAZeULaYLSrcca9Q52t28vDxC4w6kkNoBBFYaelaCq8B18UgDX2Qh3baSIVUX7NZ-WWAwJqfZtcMirxe45B6mqnKz_Eu1DHKAbBgCJ0ygvCfZraFqqreKy0XXL4pGmBrCZz3VfrEGBBMIn8cWBZpgYR4CI6-rQ1N1_T0cFqYWDvKGFm3S6oxf9jYovWMe4dyS7rQlnMbmBMFgzQ2G5xlh0D6mOmNFvRteCuvIgNgrniGzip9lsbFgqZkvxAAAAAZcPDeoB
ENV OWNER_ID=935304382
ENV OWNER_USERNAME=Galau912
ENV TOKEN=6829313514:AAGAOdhcZyUT9msB8enlkhCEsiZExP_z-j0
ENV SUPPORT_CHAT=keysupport1
ENV SQLALCHEMY_DATABASE_URI=postgres://vrswzxds:W2GA1-OCqo1KGDYWFYBJMeV12m3RXTM9@bubble.db.elephantsql.com/vrswzxds

COPY . /app

WORKDIR /app


# Installing Requirements
RUN pip3 install -U pip

RUN pip3 install --no-cache-dir -U -r requirements.txt

# If u want to use /update feature, uncomment the following and edit
#RUN git config --global user.email "your_email"
#RUN git config --global user.name "git_username"

# Copying All Source
COPY . .

# Starting Bot
CMD bash start
