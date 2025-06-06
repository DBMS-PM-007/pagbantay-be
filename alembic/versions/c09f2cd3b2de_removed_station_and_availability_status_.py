"""Removed Station and availability status from Assignments table

Revision ID: c09f2cd3b2de
Revises: 4adbce4fb96b
Create Date: 2025-05-14 00:51:30.431707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c09f2cd3b2de'
down_revision = '4adbce4fb96b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Volunteer Assignment', 'station')
    op.drop_column('Volunteer Assignment', 'availability_status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Volunteer Assignment', sa.Column('availability_status', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('Volunteer Assignment', sa.Column('station', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
