
-- Connect to jobs_db manually before running this file (you cannot switch DBs mid-script)
-- Schema and table creation for jobs_db

-- Create schema
CREATE SCHEMA IF NOT EXISTS jobs_schema;

-- Set the schema search path
SET search_path TO jobs_schema;

-- Drop table if it already exists
DROP TABLE IF EXISTS jobs_schema.jobs;

-- Create jobs table
CREATE TABLE jobs_schema.jobs (
    job_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'queued',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a trigger function to update the updated_at column
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = CURRENT_TIMESTAMP;
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Attach the trigger to the jobs table
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = CURRENT_TIMESTAMP;
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- Insert test data
INSERT INTO jobs (name, status) VALUES
('Data Import Job', 'queued'),
('Image Processing Job', 'queued'),
('Notification Sender Job', 'queued');

-- Optional: View the data
SELECT * FROM jobs_schema.jobs;