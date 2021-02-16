
# If a secret key is set, cryptographic components can use this to sign cookies and other things. Set this to a complex random value when you want to use the secure cookie for instance.
# Randomly generated value
SECRET_KEY = b'2\xe2\xb6/\x9a\x17x\x89\x82C\x87\xd3R\xe8v\xf8'

# If you want to test with SQLite instead of PostgreSQL
# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite'

# This is an example URI and it works with the docker-composy.yml
# with the correct structure for the postgresql connection URL
#
# Note that to implement proper security more work would be needed here, 
# but I didn't have the time to look into the correct way to do this.
# It is probably best to look into Docker Secrets for this.
SQLALCHEMY_DATABASE_URI = 'postgresql://helloworld:example@postgres/helloworld'

# Setting SQLALCHEMY_TRACK_MODIFICATIONS suppresses a deprecation message from SQLAlchemy.
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True

