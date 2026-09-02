-- ============================================================
-- Kisaan_Sathi Supabase Schema
-- Run this in the Supabase SQL Editor (Dashboard -> SQL Editor)
-- ============================================================

-- 1. Daily mandi price history (real Agmarknet snapshots via data.gov.in)
CREATE TABLE IF NOT EXISTS mandi_price_history (
    id                       BIGSERIAL PRIMARY KEY,
    commodity                TEXT NOT NULL,
    state                    TEXT NOT NULL,
    district                 TEXT NOT NULL DEFAULT '',
    arrival_date             TEXT NOT NULL,           -- YYYY-MM-DD
    modal_price_rs_quintal   DOUBLE PRECISION NOT NULL,
    min_price_rs_quintal     DOUBLE PRECISION,
    max_price_rs_quintal     DOUBLE PRECISION,
    market_name              TEXT,
    created_at               TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE (commodity, state, district, arrival_date)
);
CREATE INDEX IF NOT EXISTS idx_mandi_lookup
    ON mandi_price_history (commodity, state, arrival_date DESC);

-- 2. IoT telemetry persistence (survives server restarts / serverless cold starts)
CREATE TABLE IF NOT EXISTS iot_telemetry (
    id                  BIGSERIAL PRIMARY KEY,
    device_id           TEXT NOT NULL,
    recorded_at         TIMESTAMPTZ DEFAULT NOW(),
    soil_moisture_pct   DOUBLE PRECISION,
    soil_temperature_c  DOUBLE PRECISION,
    soil_ph             DOUBLE PRECISION,
    nitrogen_kg_ha      DOUBLE PRECISION,
    phosphorus_kg_ha    DOUBLE PRECISION,
    potassium_kg_ha     DOUBLE PRECISION,
    battery_level_pct   DOUBLE PRECISION,
    moisture_status     TEXT
);
CREATE INDEX IF NOT EXISTS idx_iot_device
    ON iot_telemetry (device_id, recorded_at DESC);

-- 3. Farmer recommendation history
CREATE TABLE IF NOT EXISTS crop_recommendations (
    id                UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    device_id         TEXT,
    location_district TEXT,
    location_state    TEXT,
    district          TEXT,
    state             TEXT,
    top_crop          TEXT,
    match_score       DOUBLE PRECISION,
    soil_ph           DOUBLE PRECISION,
    soil_nitrogen     DOUBLE PRECISION,
    soil_phosphorus   DOUBLE PRECISION,
    soil_potassium    DOUBLE PRECISION,
    raw_response      JSONB,
    created_at        TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Disease scan history
CREATE TABLE IF NOT EXISTS disease_scans (
    id           UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    device_id    TEXT,
    crop         TEXT,
    disease_name TEXT,
    confidence   DOUBLE PRECISION,
    created_at   TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Keep-alive ping table (prevents Supabase idle pause)
CREATE TABLE IF NOT EXISTS app_keepalive (
    id          TEXT PRIMARY KEY DEFAULT 'kisaan_sathi_heartbeat',
    last_active TIMESTAMPTZ DEFAULT NOW(),
    app_status  TEXT DEFAULT 'healthy',
    ping_count  INT DEFAULT 1,
    pinged_at   TIMESTAMPTZ DEFAULT NOW()
);

-- Enable row-level access for the anon key to read mandi prices (public data),
-- while writes stay service-role only.
ALTER TABLE mandi_price_history ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "public read mandi" ON mandi_price_history;
CREATE POLICY "public read mandi" ON mandi_price_history
    FOR SELECT USING (true);

ALTER TABLE iot_telemetry ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "public read iot" ON iot_telemetry;
CREATE POLICY "public read iot" ON iot_telemetry
    FOR SELECT USING (true);
