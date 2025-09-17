import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY','2f3a0c442b6d9ff91e352c17c467dcb2db7a897e58b9a1df')
    SUPABASE_URL = os.environ.get('SUPABASE_URL','https://uzgugxtpmmvrevrfyejc.supabase.co')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV6Z3VneHRwbW12cmV2cmZ5ZWpjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1ODA4MjY3MiwiZXhwIjoyMDczNjU4NjcyfQ.pi_dNou9bMQ-aDgPaALqGJ0EAgxssAcoB2eqVelPa2Y')
ADMIN_EMAILS = os.environ.get('ADMIN_EMAILS', 'admin@example.com').split(',')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

