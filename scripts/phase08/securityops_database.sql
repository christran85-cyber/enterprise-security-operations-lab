-- ============================================================
-- Phase 8 - Security Automation & Response
-- SecurityOps PostgreSQL Database Schema
-- ============================================================

-- Incident table
CREATE TABLE incident (
    incident_id SERIAL PRIMARY KEY,
    incident_type VARCHAR(100) NOT NULL,
    source_ip VARCHAR(45),
    destination_ip VARCHAR(45),
    severity VARCHAR(20),
    incident_status VARCHAR(30),
    detected_by VARCHAR(50),
    description TEXT,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Automation audit log
CREATE TABLE automation_log (
    log_id SERIAL PRIMARY KEY,
    incident_id INTEGER NOT NULL,
    previous_status VARCHAR(30),
    new_status VARCHAR(30),
    action_taken VARCHAR(100),
    process_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
