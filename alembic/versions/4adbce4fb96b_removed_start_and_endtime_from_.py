"""Removed start and endtime from Assignments table, also changed Date type from Datetime to Date

Revision ID: 4adbce4fb96b
Revises: 1214a2ecb556
Create Date: 2025-05-14 00:39:10.855050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4adbce4fb96b'
down_revision = '1214a2ecb556'
branch_labels = None
depends_on = None


def upgrade():
    # Remove shift time columns from Volunteer Assignment
    op.drop_column('Volunteer Assignment', 'shift_end_time')
    op.drop_column('Volunteer Assignment', 'shift_start_time')

    # Change Event.date column from DateTime to Date
    op.alter_column(
        'Event',
        'date',
        existing_type=sa.DateTime(),
        type_=sa.Date(),
        existing_nullable=False
    )


def downgrade():
    # Revert Event.date column back from Date to DateTime
    op.alter_column(
        'Event',
        'date',
        existing_type=sa.Date(),
        type_=sa.DateTime(),
        existing_nullable=False
    )

    # Re-add shift time columns to Volunteer Assignment
    op.add_column('Volunteer Assignment', sa.Column('shift_start_time', sa.TIMESTAMP(), nullable=False))
    op.add_column('Volunteer Assignment', sa.Column('shift_end_time', sa.TIMESTAMP(), nullable=False))

