#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "root" --dbname "questions" <<-EOSQL
CREATE TABLE public.questions
(
    question_id integer,
    question_text character varying(500),
    answer character varying(500),
    created_at date,
    PRIMARY KEY (question_id)
);

ALTER TABLE IF EXISTS public.questions
    OWNER to root;
EOSQL
