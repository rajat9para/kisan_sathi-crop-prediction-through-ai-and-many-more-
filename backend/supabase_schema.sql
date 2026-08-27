-- =========================================================
-- Kisaan_Sathi Supabase PostgreSQL Schema & Anti-Sleep Tables
-- Paste this script into your Supabase Dashboard -> SQL Editor
-- =========================================================

-- 1. Anti-Sleep Heartbeat Table (Prevents Supabase from pausing)
CREATE TABLE IF NOT EXISTS public.app_keepalive (
    id TEXT PRIMARY KEY DEFAULT 'kisaan_sathi_heartbeat',
    last_active TIMESTAMPTZ DEFAULT NOW(),
    app_status TEXT DEFAULT 'healthy',
    ping_count INT DEFAULT 1
);

-- 2. Farmer Recommendation History
CREATE TABLE IF NOT EXISTS public.crop_recommendations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    location_district TEXT,
    location_state TEXT,
    top_crop TEXT,
    match_score NUMERIC(5, 2),
    soil_ph NUMERIC(4, 2),
    soil_nitrogen NUMERIC(6, 2),
    soil_phosphorus NUMERIC(6, 2),
    soil_potassium NUMERIC(6, 2),
    raw_response JSONB
);

-- 3. Leaf Disease Diagnostic Scans
CREATE TABLE IF NOT EXISTS public.disease_scans (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    crop TEXT,
    disease_name TEXT,
    confidence NUMERIC(5, 2),
    severity TEXT
);

-- 4. Insert initial keep-alive row
INSERT INTO public.app_keepalive (id, last_active, app_status, ping_count)
VALUES ('kisaan_sathi_heartbeat', NOW(), 'healthy', 1)
ON CONFLICT (id) DO UPDATE SET last_active = NOW();

-- Enable Row Level Security (RLS) with public read/write for demo
ALTER TABLE public.app_keepalive ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.crop_recommendations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.disease_scans ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow public all on app_keepalive" ON public.app_keepalive FOR ALL USING (true);
CREATE POLICY "Allow public all on crop_recommendations" ON public.crop_recommendations FOR ALL USING (true);
CREATE POLICY "Allow public all on disease_scans" ON public.disease_scans FOR ALL USING (true);
