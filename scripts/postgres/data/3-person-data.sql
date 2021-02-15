--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2 (Debian 13.2-1.pgdg100+1)
-- Dumped by pg_dump version 13.2 (Debian 13.2-1.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: helloworld
--

COPY public.person (id, firstname, lastname) FROM stdin;
1	Demo user Bob	Smith
2	Demo user Alice	\N
\.


--
-- Name: person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: helloworld
--

SELECT pg_catalog.setval('public.person_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

