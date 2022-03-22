import os

print(os.environ.get('DATABASE_USER'), os.environ.get('DATABASE_PASSWORD'))
print(os.environ.get('STRIPE_SECRET_KEY'))
