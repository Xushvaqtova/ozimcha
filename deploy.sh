#!/bin/bash

echo "📥 Kodni yangilash"
git pull origin main

echo "🐍 Virtual environment aktivatsiya"
source venv/bin/activate

echo "📦 Paketlarni yangilash"
pip install -r requirements.txt

echo "🧱 Migratsiya qo'llash"
alembic upgrade head

echo "🔄 Server restart"
sudo systemctl restart fastapi2

echo "✅ Deploy tugadi"
