-- init_jobs.sql
-- This script drops and recreates the 'jobs_db' database, then creates a 'jobs' table with test data.

-- Drop the database if it exists (must be run from a different database like 'postgres')
DROP DATABASE IF EXISTS jobs_db;

-- Create the new database
CREATE DATABASE jobs_db;