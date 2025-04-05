"""Add a column

Revision ID: 942b2242e4ad
Revises: b2bf66475721
Create Date: 2025-04-05 10:38:33.589979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '942b2242e4ad'
down_revision = 'b2bf66475721'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')
